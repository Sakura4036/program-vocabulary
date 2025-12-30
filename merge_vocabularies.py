import json
import os

def merge_vocabularies(base_file, abbr_file):
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return
    if not os.path.exists(abbr_file):
        print(f"Error: {abbr_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        vocabulary = json.load(f)

    with open(abbr_file, 'r', encoding='utf-8') as f:
        abbreviations = json.load(f)

    for letter, words in abbreviations.items():
        if letter not in vocabulary:
            vocabulary[letter] = {}
        
        for word, translations in words.items():
            if word in vocabulary[letter]:
                # Merge lists and remove duplicates while preserving order
                current_translations = vocabulary[letter][word]
                merged = current_translations + [t for t in translations if t not in current_translations]
                vocabulary[letter][word] = merged
            else:
                vocabulary[letter][word] = translations

    # Sort keys alphabetically within each letter
    for letter in vocabulary:
        sorted_words = dict(sorted(vocabulary[letter].items(), key=lambda x: x[0].lower()))
        vocabulary[letter] = sorted_words

    # Sort letters
    sorted_vocabulary = dict(sorted(vocabulary.items()))

    with open(base_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_vocabulary, f, ensure_ascii=False, indent=2)

    print("Merge completed successfully.")

if __name__ == "__main__":
    merge_vocabularies('vocabulary.json', 'vocabulary_abbreviations.json')
