print('It a very small exercise')
weight = float(input('Weight '))
weightIn = input('(K)g ir (L)bs: ')

if weightIn.lower() == 'k':
    weight = weight * 2.205
    print('Weight in Pounds: ', weight)
elif weightIn.lower() == 'l':
    weight = weight / 2.205
    print('Weight in Kg: ', weight)



# Print F on consolechar
charF = [5,2,5,2,2]
for char in charF:
    print('X' * char)


# Remove duplicates
numbers = [1,2,1,2,3,4,5,6,7,3,2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
