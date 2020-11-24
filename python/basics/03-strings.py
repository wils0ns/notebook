# Strings

x = 'Sample value'  # Single quotes prefered.
x = "Sample value"
x = "'Quoted text'"
x = '\'Quoted text\''

x = b'Binary text'  # binanry string
x = u'\u9829'  # unicode string. prefix optional on python3
x = r'\nText\n'  # raw string. it scapes special chars


# Slices of string
# Format: [start:end:step]
# Default values: x[0:len(x):1]

x = 'Sample value'
print(x[0])  # S
print(x[-1])  # e
print(x[:3])  # Sam
print(x[7:])  # value
print(x[3:6])  # ple
print(x[::-1])  # eulav elpmaS

# Strings are immutable

try:
    x[0] = 1
except TypeError as e:
    # This would run
    print(e)

# String formatting
print(f'Value of x is: {x}')  # called f-string. It is the prefered format
print('Value of x is: {var}'.format(var=x))
print('{0} == {0}'.format(x))
print('{} > {}'.format(2, 1))

# String methods examples
x = 'Sample value'
print(x.lower())  # sample value
print(x.upper())  # SAMPLE VALUE
print(x.capitalize())  # Sample value
print(x.casefold())  # sample value
print(','.join(['Apple', 'Banana', 'Berries']))  # Apple,Banana,Berries

# String operations

print(x + ' Concat')  # Sample value Concat
print('*' * 3)  # ***

# Heredoc

x = '''
This is a Heredoc
    and it takes the string text as is.
Respecting the format completely.
Including          spaces.
'''
print(x)

chess = chr(9814)

print(chess)
