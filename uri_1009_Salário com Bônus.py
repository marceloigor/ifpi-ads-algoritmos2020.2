def main():
    # Entrada
    nome = input('Digite o nome do vendedor: ')
    salario_fixo = float(input('Digite o seu salário fixo: '))
    total_vendas = float(input('Digite o total de vendas efetuadas no mês: '))
    # Processamento
    comissao = (total_vendas / 100) * 15
    total = salario_fixo + comissao
    # Saída
    print(f'TOTAL = R$ {total:.2f}')


main()