import json
import os
from collections import defaultdict

def sort_vocabulary():
    json_path = os.path.join(os.path.dirname(__file__), 'vocabulary.json')
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Flatten all entries
    all_entries = {}
    for letter_group in data.values():
        if isinstance(letter_group, dict):
            for word, translation in letter_group.items():
                all_entries[word] = translation

    # Re-group by first letter
    new_data = defaultdict(dict)
    for word, translation in all_entries.items():
        first_letter = word[0].upper()
        if not first_letter.isalpha():
            # Handle non-alpha first characters if any (e.g. symbols)
            # For this specific dictionary, we'll keep them or put them in '#' 
            # but usually it's A-Z. Let's just use the first char.
            new_data[first_letter][word] = translation
        else:
            new_data[first_letter][word] = translation

    # Sort top-level keys and inner keys
    sorted_data = {}
    for letter in sorted(new_data.keys()):
        # Sort words case-insensitively
        words = sorted(new_data[letter].keys(), key=lambda s: s.lower())
        sorted_data[letter] = {word: new_data[letter][word] for word in words}

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully sorted {json_path}")

if __name__ == "__main__":
    sort_vocabulary()
