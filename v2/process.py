import json
import re

def parse_vocabulary(file_path: str) -> dict:
    result = {}
    current_letter = None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # 匹配字母标题 h2. X
            letter_match = re.match(r'^h2\.\s+([A-Z])$', line)
            if letter_match:
                current_letter = letter_match.group(1)
                result[current_letter] = {}
                continue
            
            # 跳过表头和空行
            if not line or line.startswith('| *') or not line.startswith('|'):
                continue
            
            # 解析表格行
            parts = [p.strip() for p in line.split('|')]
            # parts[0] 是空的，parts[1] 是英文，parts[2] 是译法1
            if len(parts) >= 3 and current_letter and parts[1]:
                english = parts[1].strip()
                translation = parts[2].strip()
                if english and translation:
                    result[current_letter][english] = translation
    
    return result

if __name__ == '__main__':
    vocabulary = parse_vocabulary('vocabulary.md')
    with open('vocabulary.json', 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False, indent=2)
