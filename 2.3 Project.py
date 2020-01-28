first_name = input()
last_name = input()

print('Hello, friend what is your name?')

print('Nice to meet you',first_name, last_name)

favorite_place = input()

print('What is your favorite place to eat?\n',favorite_place)

if favorite_place == Chipotle:
   print('Wow, that is mine too!')
elif favorite_place == Chickfila:
   print('Not a bad choice.')
elif favorite_place == Dominos:
   print('I love pizza!.')
elif favorite_place == Panera:
   print('I do not enjoy their food.')
else:
   print('Maybe I should check it out!')
