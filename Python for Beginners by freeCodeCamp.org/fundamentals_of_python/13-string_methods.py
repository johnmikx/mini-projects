print('xortex'.upper())  # Convert to uppercase
print('XORTEX'.lower())  # Convert to lowercase
print('xortex'.title())  # Convert to title case
print('xortex handsome'.title())  # Convert to title case
print('xortex HAndsome'.islower()) # False, Check if all characters are lowercase
print('xortex handsome'.isupper()) # False, Check if all characters are uppercase
print('XORTEX HANDSOME'.isupper()) # True, Check if all characters are uppercase
print('xortex'.startswith('xo'))      # True, checks if string starts with 'xo'
print('xortex'.endswith('tex'))       # True, checks if string ends with 'tex'
print('xortex handsome'.replace('handsome', 'cool'))  # Replace 'handsome' with 'cool'
print('xortex handsome'.split())      # Split string into list by whitespace
print('   xortex   '.strip())         # Remove leading and trailing whitespace
print('-'.join(['xortex', 'handsome'])) # Join list into string with '-'
print('xortex handsome'.find('hand')) # Find index of substring 'hand'
print('xortex'.isalpha())   # True, all characters are alphabetic
print('xortex123'.isalnum()) # True, all characters are alphanumeric
print('12345'.isdecimal())   # True, all characters are decimal digits
print(' '.join('xortex'))  # Join characters with space
print('xortex handsome'.count('o'))  # Count occurrences of 'o'
print('xortex handsome'.index('handsome'))  # Find index of substring 'handsome'
print('xortex handsome'.rfind('o'))  # Find last index of 'o'
print('xortex handsome'.rindex('o'))  # Find last index of 'o
print('xortex handsome'.center(30))  # Center string within 30 characters
print('xortex handsome'.ljust(30))   # Left justify string within 30
print('xortex handsome'.rjust(30))   # Right justify string within 30
print('xortex handsome'.zfill(30))   # Pad string with zeros to length 30
print('xortex handsome'.capitalize()) # Capitalize first character
print('xortex handsome'.casefold())  # Case insensitive comparison
print('xortex handsome'.encode())    # Encode string to bytes
print('xortex handsome'.expandtabs()) # Expand tabs to spaces
print('xortex handsome'.format(name='Kortex')) # Format string with named argument
print('xortex handsome'.format_map({'name': 'Kortex'})) # Format string with mapping
print('xortex handsome'.isprintable()) # Check if all characters are printable
print('xortex handsome'.partition('handsome')) # Partition string at 'handsome'
print('xortex handsome'.rpartition('handsome')) # Partition string at last 'handsome'
print('xortex handsome'.removeprefix('xortex ')) # Remove prefix 'xortex '
print('xortex handsome'.removesuffix(' handsome')) # Remove suffix ' handsome'
print('xortex handsome'.translate(str.maketrans('x', 'y'))) # Translate characters
print('xortex handsome'.swapcase()) # Swap case of characters
print('xortex handsome'.isidentifier()) # Check if string is a valid identifier
print('xortex handsome'.isnumeric()) # Check if all characters are numeric
print('xortex handsome'.isdecimal()) # Check if all characters are decimal
print('xortex handsome'.isprintable()) # Check if all characters are printable
print('xortex handsome'.isascii()) # Check if all characters are ASCII
print('xortex handsome'.lstrip()) # Remove leading whitespace
print('xortex handsome'.rstrip()) # Remove trailing whitespace
print('xortex handsome'.removeprefix('xortex ')) # Remove prefix 'xortex '
print('xortex handsome'.removesuffix(' handsome')) # Remove suffix ' handsome'

name = 'Yortex'
print(len(name))  # Length of the string
print("or" in name)  # Check if substring is in string
print("x" not in name)  # Check if substring is not in string