#Creates an automatically list for you

people = ['Christoper', 'Susan']

for name in people:
    print(name)

#When dealing with while loops need some sort of counter 
#When doing a while loop put in the change first; Incrementing index is confusing sometimes 
index = 0
while index < len(people):
    print(people[index])
    index = index + 1           #change