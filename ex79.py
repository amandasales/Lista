lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado não será adicionado...')
    c = str(input('Deseja continuar? [S/N]')).upper()
    if c == 'N':
        break
    if c != 'S':
        print('Tente novamente.')
print('Programa encerrado.')
lista.sort()
print(f'Você digitou os valores {lista}')
