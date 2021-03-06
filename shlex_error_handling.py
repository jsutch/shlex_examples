import shlex

text = """This line is ok.
This line has an "unfinished quote.
This line is ok, too.
"""

print(('ORIGINAL:', repr(text)))
print()

lexer = shlex.shlex(text)

print('TOKENS:')
try:
    for token in lexer:
        print((repr(token)))
except ValueError as err:
    first_line_of_error = lexer.token.splitlines()[0]
    print(('ERROR:', lexer.error_leader(), str(err), 'following "' + first_line_of_error + '"'))
