print('{:=^40}'.format('TABUADA'))
num = int(input('Escolha um número: '))

for i in range (1, 11):
    tab = num*i
    print(f'{num} x {i} = {tab}')

print(f'Essa é a tabuada de {num}.')
