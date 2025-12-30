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

    english_lines = []
    mixed_lines = []

    # Sort keys to ensure consistent order
    for letter in sorted(data.keys()):
        words_dict = data[letter]
        for word, translation in words_dict.items():
            english_lines.append(word)
            mixed_lines.append(word)
            mixed_lines.append(translation)

    with open(english_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(english_lines))

    with open(mixed_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(mixed_lines))

    print(f"Successfully converted to:\n1. {english_txt}\n2. {mixed_txt}")

if __name__ == "__main__":
    convert_vocabulary()
