import shlex

text = """This text has "quoted parts" inside it."""
print(('ORIGINAL:', repr(text)))
print()

print('TOKENS:')
print((shlex.split(text)))
