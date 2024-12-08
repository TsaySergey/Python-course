#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    pattern = r'\[\s*([+-]?\d+)\s*\]'
    final_finds = re.findall(pattern, s)
    result = [int(match) for match in final_finds]
    return result

def main():
    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))
    pass

if __name__ == "__main__":
    main()
