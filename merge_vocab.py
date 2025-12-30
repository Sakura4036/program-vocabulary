import json
import os
import re

def load_json(filepath):
    if not os.path.exists(filepath):
        print(f"Warning: File not found: {filepath}")
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def split_translation(text):
    if not text:
        return []
    # Split by common separators: commas, chinese commas, slashes, dunhao
    parts = re.split(r'[,\uff0c/\u3001]', text)
    # Clean whitespace and empty strings
    return [p.strip() for p in parts if p.strip()]

def merge_vocab():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    v1_path = os.path.join(base_dir, 'v1', 'vocabulary.json')
    v2_path = os.path.join(base_dir, 'v2', 'vocabulary.json')
    v4_path = os.path.join(base_dir, 'v4', 'vocabulary.json')

    data_v1 = load_json(v1_path)
    data_v2 = load_json(v2_path)
    data_v4 = load_json(v4_path)

    merged = {}

    # Helper to process an entry
    def add_entry(key, translation_str):
        if not key or not translation_str:
            return
        
        # Normalize key for sorting/grouping, but keep original for display if needed
        # We will use the lowercase key as the primary index to merge
        key_lower = key.lower().strip()
        
        # If we encounter this key for the first time, initialize
        if key_lower not in merged:
            merged[key_lower] = {
                "display_key": key.strip(),
                "translations": set()
            }
        
        # Heuristic: if the new key has uppercase letters and the existing one doesn't,
        # or if the new key looks "better" (e.g. standard capitalization), update display_key.
        # For now, let's prefer the one from v4 if available, or just keep the first one/most capitalized one.
        # Actually, v4 has good casing (e.g. "AJAX"), v1/v2 vary.
        # Let's simple preference: if current display is all lower, and new has upper, replace.
        if merged[key_lower]["display_key"].islower() and any(c.isupper() for c in key):
            merged[key_lower]["display_key"] = key.strip()

        # Add translations
        if isinstance(translation_str, list):
             for t in translation_str:
                 merged[key_lower]["translations"].add(t.strip())
        else:
            trans_list = split_translation(translation_str)
            for t in trans_list:
                merged[key_lower]["translations"].add(t)

    # Process v1 (Nested by letter -> key: value)
    for letter, content in data_v1.items():
        for k, v in content.items():
            add_entry(k, v)

    # Process v2 (Nested by letter -> key: value)
    for letter, content in data_v2.items():
        for k, v in content.items():
            add_entry(k, v)

    # Process v4 (Nested by letter -> key: { translation: "", keywords: [] })
    for letter, content in data_v4.items():
        for k, v in content.items():
            if isinstance(v, dict):
                add_entry(k, v.get("translation", ""))
            else:
                # specific fallback content logic if v4 structure varies
                add_entry(k, str(v))

    # Remove irrelevant words
    # Current simplistic filter: remove if no chinese chars in translation (likely garbage or untranslated)
    # AND remove if the key itself is super short (<2 chars) unless it's a known acronym? relative.
    
    final_dict = {}
    
    # Sort keys
    sorted_keys = sorted(merged.keys())
    
    for k in sorted_keys:
        item = merged[k]
        display_k = item["display_key"]
        trans_set = item["translations"]
        
        # Filter: Remove keys that are likely not useful
        if not trans_set:
            continue
            
        # Simplistic "Computer domain" check? 
        # It's hard to strict filter. Let's trust the sources but remove obviously empty translations.
        
        # Convert set to sorted list for consistency
        trans_list = sorted(list(trans_set))
        
        # Determine grouping letter
        first_char = display_k[0].lower()
        if not first_char.isalpha():
            first_char = '#'
            
        if first_char not in final_dict:
            final_dict[first_char] = {}
            
        final_dict[first_char][display_k] = trans_list

    # Ensure output is sorted by letter key
    final_sorted_output = {k: final_dict[k] for k in sorted(final_dict.keys())}
    
    output_path = os.path.join(base_dir, 'vocabulary_merged.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_sorted_output, f, ensure_ascii=False, indent=2)
    
    print(f"Merged vocabulary saved to {output_path}")

if __name__ == '__main__':
    merge_vocab()
