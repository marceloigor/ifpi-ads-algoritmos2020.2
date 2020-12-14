def main():
    # Entrada
    a = float(input('digite o valor de A: '))    
    b = float(input('digite o valor de B: '))
    c = float(input('digite o valor de C: '))    
    # Processamento
    media = ((a*2) + (b*3) + (c*5)) / (2 + 3 + 5)
    # Saída
    print(f'MEDIA = {media:.1f}')


main()