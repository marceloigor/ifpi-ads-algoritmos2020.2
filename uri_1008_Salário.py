def main():
    # Entrada
    n_funcionario = int(input('Digite seu número: ')) 
    h_trabalhadas = int(input('Digite seu número de horas trabalhadas: '))
    valor_hora = float(input('Digite o valor que recebe por hora trabalhada: '))
    # Processamento
    salario = valor_hora * h_trabalhadas
    # Saída
    print(f'NUMBER = {n_funcionario} \nSALARY = U$ {salario:.2f}')


main()