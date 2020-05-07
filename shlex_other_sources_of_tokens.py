import shlex

text = """This text says to source quotes.txt before continuing."""
print(('ORIGINAL:', repr(text)))
print()

lexer = shlex.shlex(text)
lexer.wordchars += '.'
lexer.source = 'source'

print('TOKENS:')
for token in lexer:
    print((repr(token)))
