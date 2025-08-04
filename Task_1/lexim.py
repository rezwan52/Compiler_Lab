import re

keywords = {'int', 'float', 'char', 'if', 'else', 'for', 'while', 'do', 'void', 'return'}
arithmetic_operators = {'+', '-', '*', '/', '='}
logical_operators = {'>', '>=', '<', '<=', '==', '!='}
punctuation = {';', ',', ':'}
parenthesis = {'(', ')', '{', '}', '[', ']'}
string_pattern = r"'[^']*'"

def classify_token(token):
    if token in keywords:
        return 'Keyword'
    elif re.match(r'^\d+(\.\d+)?$', token):
        return 'Constant'
    elif re.match(string_pattern, token):
        return 'Constant'
    elif token in arithmetic_operators:
        return 'Arithmetic Operator'
    elif token in logical_operators:
        return 'Logical Operator'
    elif token in punctuation:
        return 'Punctuation'
    elif token in parenthesis:
        return 'Parenthesis'
    elif re.match(r'^[a-zA-Z_]\w*$', token):
        return 'Identifier'
    return None

def remove_comments(code):
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.S)
    return code

def tokenize_code(code):
    code = remove_comments(code)
    pattern = r"(>=|<=|==|!=|[+\-*/=<>;,:(){}\[\]]|'[^']*'|\d+\.\d+|\d+|[a-zA-Z_]\w*)"
    tokens = re.findall(pattern, code)
    return tokens

def lexical_analyzer(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    tokens = tokenize_code(code)

    token_map = {
        'Keyword': set(),
        'Identifier': set(),
        'Constant': set(),
        'Arithmetic Operator': set(),
        'Logical Operator': set(),
        'Punctuation': set(),
        'Parenthesis': set()
    }

    for token in tokens:
        token_type = classify_token(token)
        if token_type:
            token_map[token_type].add(token)

    for category in token_map:
        if token_map[category]:
            sorted_tokens = sorted(token_map[category])
            print(f"{category} ({len(sorted_tokens)}): {', '.join(sorted_tokens)}")

if __name__ == "__main__":
    print(" ")
    print("Sample Output of input_1 file:\n")
    lexical_analyzer("input_1.c")
    print(" ")
    print("Sample Output of input_2 file:\n")
    lexical_analyzer("input_2.c")
