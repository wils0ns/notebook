# Conditionals

if 'son' in 'Wilson':
    print('🎁')
elif 'ipe' in 'Filipe':
    print('💩')
else:
    print('💋')

# For Loop

for i in range(5):
    print(f'{i},', end='')  # Default `end` value is '\n'

print()

for i in 'Sample Name':  # For each char in string
    print(f'{i}*', end='')

print()

x = {'x': 1, 'y': 2}

for i in x:  # for each key in dict
    print(i, x[i])

for k, v in x.items():  # for each key in dict
    print(k, v)


has_multiple_of_3 = False
for i in [1, 2, 4]:
    if i == 1:
        continue
    print(i)
    if i % 3 == 0:
        has_multiple_of_3 = True
        break

if not has_multiple_of_3:
    print('No multiple of 3 found.')

for i in [1, 2, 3, 4]:
    if i == 1:
        continue
    print(i)
    if i % 3 == 0:
        break
else:
    # Executed if nothing interrupts the for loop (break or return)
    print('No multiple of 3 found.')

x = 5
while x > 0:
    print('*'*x)
    x -= 1
