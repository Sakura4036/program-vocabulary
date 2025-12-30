import json
import os
import re
from pathlib import Path


def parse_md_file(file_path: str) -> dict:
    """解析单个markdown文件，返回 {英文: 译文}"""
    result = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    if len(lines) < 3:
        return result
    
    # 第一行是英文单词
    english = lines[0].strip()
    # 第三行包含译文
    if len(lines) >= 3:
        translation_line = lines[2].strip()
        # 移除前缀 ":    " 和音标部分
        translation = re.sub(r'^:\s+', '', translation_line)
        
        if english and translation:
            result[english] = translation
    
    return result


def process_v3_directory(v3_path: str) -> dict:
    """处理v3目录下所有子文件夹中的md文件"""
    result = {}
    
    v3_dir = Path(v3_path)
    
    # 遍历所有字母文件夹 (A-Z)
    for letter_dir in sorted(v3_dir.iterdir()):
        if not letter_dir.is_dir():
            continue
        
        letter = letter_dir.name
        if not re.match(r'^[A-Z]$', letter):
            continue
        
        result[letter] = {}
        
        # 遍历该字母文件夹下的所有md文件
        for md_file in letter_dir.glob('*.md'):
            # 跳过字母标题文件 (如 A.md, B.md)
            if md_file.stem == letter:
                continue
            
            word_data = parse_md_file(str(md_file))
            result[letter].update(word_data)
    
    return result


if __name__ == '__main__':
    v3_path = os.path.dirname(os.path.abspath(__file__))
    vocabulary = process_v3_directory(v3_path)
    
    output_file = os.path.join(v3_path, 'vocabulary.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False, indent=2)
    
    print(f'处理完成，结果已保存到 {output_file}')
