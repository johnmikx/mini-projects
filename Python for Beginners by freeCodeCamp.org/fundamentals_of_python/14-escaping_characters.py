name = "Yor\"tex"
print(name) # Output: Yor"tex, escaping a character with a backslash

name = 'Yor\"tex'
print(name)

second_derivative = "f'\'(x)"
print(second_derivative) # Output: f''(x), escaping single quotes inside double quotes

dollar_sign = "This book costs \n 100$"
print(dollar_sign) # Output: This book costs
                   #          100$, newline character

name = 'Yor\\tex'
print(name) # Output: Yor\tex, escaping the backslash itself