done = True
print('yes' if done else 'no')

done = False
print('yes' if done else 'no')

done = -1
print('yes' if done else 'no')

done = 'zy'
print('yes' if done else 'no')

done = ''
print('yes' if done else 'no')

done = True
print(type(done) == bool)  # Check if variable is of boolean type

done = 'xy'
print(type(done) == bool)

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read]) # True if any book is read
read_all_books = all([book_1_read, book_2_read]) # True if all books are read

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked]) # True if all conditions are met
print(ready_to_serve)