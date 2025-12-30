import json
import re
from pathlib import Path


def parse_vocabulary_to_dict(md_path: str) -> dict:
    """Parse vocabulary.md and return structured data."""
    content = Path(md_path).read_text(encoding='utf-8')
    
    result = {}
    current_letter = None
    
    for line in content.splitlines():
        line = line.strip()
        
        # Match section header like "# A"
        if re.match(r'^#\s+([A-Z])$', line):
            current_letter = line[-1].lower()
            result[current_letter] = {}
            continue
        
        # Skip empty lines
        if not line or current_letter is None:
            continue
        
        # Match vocabulary entry: "english chinese" or "english (xxx) chinese"
        # Format: word/phrase followed by Chinese translation
        match = re.match(r'^(.+?)\s+([\u4e00-\u9fff].*)$', line)
        if match:
            english = match.group(1).strip()
            chinese = match.group(2).strip()
            result[current_letter][english] = chinese
    
    return result


def main():
    script_dir = Path(__file__).parent
    md_path = script_dir / 'vocabulary.md'
    json_path = script_dir / 'vocabulary.json'
    
    vocabulary = parse_vocabulary_to_dict(str(md_path))
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False, indent=2)
    
    print(f"Saved to {json_path}")


if __name__ == '__main__':
    main()
