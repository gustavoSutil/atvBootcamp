def classificacao(valorEntrada):
    if valorEntrada < 0:
        print('O valor não pode ser negativo')
        return 'Erro'
    elif valorEntrada < 1001:
        return 'Ferro' 
    elif valorEntrada < 2001:
        return 'Bronze'
    elif valorEntrada < 5001:
        return 'Prata'
    elif valorEntrada < 7001:
        return 'Ouro'
    elif valorEntrada < 8001:
        return 'Platina'
    elif valorEntrada < 9001:
        return 'Ascendente'
    elif valorEntrada < 10001:
        return 'Imortal'
    elif valorEntrada > 10001:
        return 'Radiante'

def main():
    loop = 1
    while(loop!=2):
        loop = int(input('''
1-repetir
2-sair
'''))
        if loop == 2:
            break
        nome = input('Qual o nome do Heroi?\nr:')
        xp = int(input('Qual seu XP?\nr:'))
        nivel = classificacao(xp)
        if (nivel != 'Erro'):
            print(f'O Herói de nome {nome} está no nível de {nivel}')

main()