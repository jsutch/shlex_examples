import shlex
import sys

if len(sys.argv) != 2:
    print('Please specify one filename on the command line.')
    sys.exit(1)

filename = sys.argv[1]
body = open(filename, 'rt').read()
print(('ORIGINAL:', repr(body)))
print()

print('TOKENS:')
lexer = shlex.shlex(body)
for token in lexer:
    print((repr(token)))
