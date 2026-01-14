import sys
import re
from pathlib import Path

def modify_torch_version(file_path, old_version, new_version):
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return False
    
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    content = re.sub(rf'torch>={re.escape(old_version)},<2\.\d+', f'torch>={new_version},<2.9', content)
    content = re.sub(rf'torch{re.escape(old_version)}', f'torch{new_version}', content)
    
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"Modified: {file_path}")
        return True
    else:
        print(f"No changes needed: {file_path}")
        return False

def main():
    base_dir = Path(__file__).parent
    
    files_to_modify = [
        base_dir / 'setup.py',
        base_dir / 'pyproject.toml',
        base_dir / 'setup.cfg',
    ]
    
    old_version = '2.7'
    new_version = '2.8'
    
    print(f"Modifying torch version from {old_version} to {new_version}...")
    
    modified_count = 0
    for file_path in files_to_modify:
        if modify_torch_version(file_path, old_version, new_version):
            modified_count += 1
    
    print(f"\nModified {modified_count} file(s)")

if __name__ == '__main__':
    main()
