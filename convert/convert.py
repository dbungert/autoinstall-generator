
# assumptions:
#  can process one line at a time
#  whitespace-only lines and comments should pass thru

def convert(line):
    trimmed = line.strip()
    tokens = trimmed.split(' ')
    if len(tokens) > 3 and tokens[0] == 'd-i':
        locale = tokens[3]
        return f'''Welcome:\n  lang: {locale}'''

    return line