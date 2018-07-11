Order_size = str()
size = float()
total = float()
topping = float()
choose = str()
topping_Select = str()

print('welcome to Mac N Cheese')
print('*************************')
print('small   = $4.00')
print('Medium  = $4.00') 
print('Large   = $4.00')
print('*************************')

Order_size = input("Enter the size of your order (S = Small, M = Medium, L = Large): ")

if (Order_size =='s'):
    size=4.00
elif (Order_size == 'm'):
    size = 5.00
elif (Order_size == 'l'):
    size = 6.00

if(size>0):
    print('\nB= Bacon =$1.50')
    print('O= Grilled Onions = $1.00')
    print('C= Grilled Chicken =$2.50')
    print('L= Lobster = $5.00')
    print("\nEnter your choice:")
    print('====================================')
    topping_Select = input()

    if(topping_Select == 'b'):
        topping = 1.50
    elif(topping_Select =='o'):
        topping = 1.00
    elif(topping_Select == 'c'):
        topping == 2.50
    elif(topping_Select == 'l'):
        topping = 5.00
    else:
        topping =0.0

    total =size + topping 
    print('\nOrder Summary')
    print('====================================')
    print('Base Cost   $',format(size,'.2f'))
    print('Add On Cost $',format(topping,'.2f'))
    print('Total Cost  $',format(total,'.2f'))
    print('\n\t\t\t thank you for your business!!')
else:
    print('No order founded !!')
