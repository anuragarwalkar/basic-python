print('It a very small exercise')
weight = float(input('Weight '))
weightIn = input('(K)g ir (L)bs: ')

if weightIn.lower() == 'k':
    weight = weight * 2.205
    print('Weight in Pounds: ', weight)
elif weightIn.lower() == 'l':
    weight = weight / 2.205
    print('Weight in Kg: ', weight)

