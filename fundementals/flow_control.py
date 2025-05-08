#Flow Control

#In ifel statement one of 2 possible blocks to execute the staement
password = "swordfish"
if password == 'swordfish': #Colon : means new block
    print('Access granted')
else:
    print('Wrong password')

#elif statements allows one of many possible blocks to execute the staement
name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, jit')
elif age < 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not ALice grannie')