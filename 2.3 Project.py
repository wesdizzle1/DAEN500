print ('Hello and welcome!')
user_name = input('What is your name?')


print('\n Hello ', user_name, '. How are you feeling about learning today?')


set_loop = True
while set_loop == True:
    user_day = input("'ready' or 'not'?\n")
    
    if (user_day == 'not'):
        print('\n Im sorry to hear that, lets try to work on it together!\n')
        set_loop = False
    if (user_day == 'ready'):
        print('\n That is awesome!\n')
        set_loop = False


print("Now lets begin.\n")
print('Has learning Python been easy for you?')

set_loop = True
while set_loop == True:
    user_day = input("'yes' or 'no'?\n")
    
    if (user_day == 'no'):
        print('\n I feel the same way, but just keep trying!\n')
        set_loop = False
    if (user_day == 'yes'):
        print('\n That is great to hear, I think Phython is fun to learn!\n')
        set_loop = False
               
print('Has learning R been easy for you?')

set_loop = True
while set_loop == True:
    user_day = input("'yes' or 'no'?\n")
    
    if (user_day == 'no'):
        print('\n I feel the same way, but just keep trying!\n')
        set_loop = False
    if (user_day == 'yes'):
        print('\n That is great, I think R is fun to learn!\n')
        set_loop = False       
        
print('Do you like learning with DataCamp')

set_loop = True
while set_loop == True:
    user_day = input("'yes' or 'no'?\n")
    
    if (user_day == 'no'):
        print('\n Well we all have different learning styles for sure.\n')
        set_loop = False
    if (user_day == 'yes'):
        print('\n I think DataCamp is great!\n')
        set_loop = False       
 
print('Do you know what GitHub is?')

set_loop = True
while set_loop == True:
    user_day = input("'yes' or 'no'?\n")
    
    if (user_day == 'no'):
        print('\n Maybe a good Lynda video will help!\n')
        set_loop = False
    if (user_day == 'yes'):
        print('\n You are on the path to success!\n')
        set_loop = False   

       
print("Good luck on your studies", user_name,"!")
