import os

def search_keyword_in_file(file_path, keyword):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if keyword.lower() in line.lower():
                    print(f"'{keyword}' in {file_path} line {line_number}: {line.strip()}")
    except (UnicodeDecodeError, PermissionError) as e:
        print("Could not read")

def scan_directory(directory, keyword):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            search_keyword_in_file(file_path, keyword)

if __name__ == "__main__":
    directory_to_scan = '' # the directory to scan
    keyword_to_search = "" # the keyword you want to find

    print('{directory_to_scan}')
    scan_directory(directory_to_scan, keyword_to_search)
    print("Done.")
