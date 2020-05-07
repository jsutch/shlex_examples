import shlex

text = """|Col 1||Col 2||Col 3|"""
print(('ORIGINAL:', repr(text)))
print()

lexer = shlex.shlex(text)
lexer.quotes = '|'

print('TOKENS:')
for token in lexer:
    print((repr(token)))
