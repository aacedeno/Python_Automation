#Functions are mini-programs in your program


#Use a function if you're copying and pasting code frequently 

#Parameter allow for more flexibility in funcitons

#When using the return componenet it returns a value, since the function is returning a value it has to be stored somewhere 
def get_initial(name):
    initial = name[0:1].upper()
    return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name) #The input is being returned to the first_name_initiail variable using the return value in get_initial

# last_name = input('Enter your last name: ')
# last_name_initial = get_initial(last_name) #When you call the function you have to have a place to be it

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

#The input given by the user is being passed into the function as a parameter
print('Your initials are: ' \
      + get_initial(first_name) \
      + get_initial(last_name) 
)


