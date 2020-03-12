primeiro = int(input('Informe o 1º termo: '))
razao = int(input('Informe a razão: '))
decimo = primeiro + 9 * razao

for i in range (primeiro, decimo, razao):
    print(f'{i}', end=' -> ')

print('ACABOU')