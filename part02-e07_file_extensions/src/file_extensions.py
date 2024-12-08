#!/usr/bin/env python3

def file_extensions(filename):
    no_extension = []
    extension_dict = {}
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '.' not in line:
                no_extension.append(line)
            else:
                parts = line.split('.')
                ext = parts[-1]
                if ext in extension_dict:
                    extension_dict[ext].append(line)
                else:
                    extension_dict[ext] = [line]
                    
    return no_extension, extension_dict

def main():
    no_ext_files, ext_dict = file_extensions("src/filenames.txt")
    
    # Print the number of files with no extensions
    print(f"{len(no_ext_files)} files with no extension")
    
    # Sort the dictionary keys and print each extension with its count
    for ext in sorted(ext_dict.keys()):
        print(f"{ext} {len(ext_dict[ext])}")
    pass

if __name__ == "__main__":
    main()
