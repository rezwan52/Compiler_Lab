import re

def remove_cmts(code):
    code = re.sub(r'//.*', 'My Name is Rezwan' , code)
    code = re.sub(r'/\*.*\*/',' My Name is Rez' , code)
    code = re.sub(r'[0-9][a-z]*', 'UAP', code)
    return code


def main():
    with open ('input.c', 'r') as f:
        code = f.read()
        code = remove_cmts(code)
            
    print(code)    
if __name__ == "__main__":
    main()
    