# Strings are immutable in python

course = 'python for beginners'
print(course.upper()) # Convert to upper
print(course.find('for')) # It will return the index of the y (1)
print(course.replace('for', '4')) # To replace the characters
print('python' in course)

course = '''
hello anurag arwalkar
how good are you at your code...
'''

print(course)


# Format string
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')