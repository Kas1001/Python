# Process Easier to Ask for Permission (EAFP)

p = 'C:/Users'

try:
    print('Try to process file')
except OSError as e:
    print(f'Error: {e}')