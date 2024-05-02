#This program says hello and asks for my name

print('Hello world!')

print('What is your name?') #ask for thier name
myName = input ()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') #ask for thier age

myAge = input() # Input function always returns a string value and can't do math with a string

#Have to get an integer value to do calculations
print('You will be ' + str(int(myAge) + 1) + ' in a year') #Can't do string catconation on integer

#print() displays the value passed to it
#input() lets user type in a value
#len() takes a string value and returns and integer value of the string's length
#int(), str(), and float() convert values' data type