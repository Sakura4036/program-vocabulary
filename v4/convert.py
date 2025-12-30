import json
import os

def convert_vocabulary():
    json_path = os.path.join(os.path.dirname(__file__), 'vocabulary.json')
    english_txt = os.path.join(os.path.dirname(__file__), 'vocabulary_english.txt')
    mixed_txt = os.path.join(os.path.dirname(__file__), 'vocabulary_mixed.txt')

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Collect all words and their translations
    all_words = {}
    for letter in data:
        for word, info in data[letter].items():
            # Use dictionary to handle deduplication naturally, preserving the last translation seen
            # or you can add logic here to merge if necessary.
            all_words[word] = info['translation']

    # Sort words alphabetically (case-insensitive)
    sorted_words = sorted(all_words.keys(), key=str.lower)

    english_lines = sorted_words
    mixed_lines = []
    for word in sorted_words:
        mixed_lines.append(word)
        translation = all_words[word]
        # Only append translation if it's different from the word (case-insensitive check)
        if translation.lower() != word.lower():
            mixed_lines.append(translation)

    with open(english_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(english_lines))

    with open(mixed_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(mixed_lines))

    print(f"Successfully converted to:\n1. {english_txt}\n2. {mixed_txt}")

if __name__ == "__main__":
    convert_vocabulary()
