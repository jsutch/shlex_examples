import shlex

for s in [ 'Do"Not"Separate',
           '"Do"Separate',
           'Escaped \e Character not in quotes',
           'Escaped "\e" Character in double quotes',
           "Escaped '\e' Character in single quotes",
           r"Escaped '\'' \"\'\" single quote",
           r'Escaped "\"" \'\"\' double quote',
           "\"'Strip extra layer of quotes'\"",
           ]:
    print('ORIGINAL :', repr(s))
    print('non-POSIX:', end=' ')

    non_posix_lexer = shlex.shlex(s, posix=False)
    try:
        print(repr(list(non_posix_lexer)))
    except ValueError as err:
        print('error(%s)' % err)

    
    print('POSIX    :', end=' ')
    posix_lexer = shlex.shlex(s, posix=True)
    try:
        print(repr(list(posix_lexer)))
    except ValueError as err:
        print('error(%s)' % err)

    print()
