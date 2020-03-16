What = input('что вы хотите купить?')
#text1 = 
NumberOfPizza = eval(input(f'Сколько {What} вы хотите?'))
CostOfPizza = eval(input(f'какая стоимость {What}?'))
Cost = NumberOfPizza * CostOfPizza
print(f'Спасибо за покупку {NumberOfPizza} {What} с вас {Cost}!!! ')
if  Cost > 1000000:
    print('Ха, вы разорены!')
