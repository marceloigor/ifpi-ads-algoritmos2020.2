def main():
    # Entrada
    cod, num, valor_u = map(float,input().split(' '))
    cod2, num2, valor_u2 = map(float,input().split(' '))
    # Processamento
    valor_total = (num * valor_u) + (num2 * valor_u2)
    # Saída
    print(f'VALOR A PAGAR: R$ {valor_total:.2f}')


main()