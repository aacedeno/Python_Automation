#Modules are a group of functions grouped together to be used elsewhere 
    #Modules= python file with functions, classes and other components 

#We use modules to break code down into reusable structures 
#Can use the modules by importing them as packages

#helpers.py
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print (message)


#import module as namespace 
import helpers
helpers.display('Not a warning')

#import all into current namespace
from helpers import *
display('Not a warning')

#import specific items into current namespace
from helpers import display
display('Not a warning')



#Packages are published collections of modules

#requirements.txt is a text file that has all of the packages that I want to use 


