def main():
    # Entrada
    a = float(input('Digite a nota A: '))
    b = float(input('Digite a nota B: '))
    # Processamento
    media = ((a*3.5) + (b*7.5)) / (3.5 + 7.5)
    # Saída
    print(f'MEDIA = {media:.5f}')

main()