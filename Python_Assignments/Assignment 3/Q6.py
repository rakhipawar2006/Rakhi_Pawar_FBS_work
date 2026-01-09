cost_price = float(input('Enter Cost Price: '))
selling_price = float(input('Enter Selling Price: '))

if(selling_price > cost_price):
    profit = selling_price - cost_price
    print(f'Profit = {profit} Rs.')
else:
    loss = cost_price - selling_price
    print(f'Loss = {loss} Rs.')