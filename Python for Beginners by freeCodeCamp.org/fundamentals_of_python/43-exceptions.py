#    try:
        # some lines of code
#    except <ERROR1>: 
        # handler <ERROR1>
#    except <ERROR2>:
        # handler <ERROR2>
#    else:
        # no exceptions were raised, the code ran successfully
#    finally:
        # do something in any case

# Key Notes:
# sometimes you might get `E0FError` which means "end of file error"
# sometimes you might get `ZeroDivisionError` which means "you divide a certain number by zero"
# result = 2 / 0
# print(result) # ZeroDivisionError: division by zero

# sometimes you might get `TypeError` which means "you might have a type conversion issue"
# sometimes you might get `ValueError` which means "it has received an argument of the correct data type but with an inappropriate or invalid value"

try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1

print(result) # 1

try:
    raise Exception('An error!')
except Exception as error:
    print(error)

class DogNotFoundException(Exception):
    print('inside')
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')