from data_save import carregar_dados
from calcData import calcularData
from catchInfo import xmlInfo
from empresas import multiplicar, adicionar_peso, remover_empresa, listar, mudar_peso
def menu():
    dados = carregar_dados()
    while True:
        print("1. Multiplicar peso")
        print("2. Adicionar empresa")
        print("3. Remover empresa")
        print("4. Lista de empresas")
        print("5. Mudar peso")
        print("6. Somar dias")
        print("7. Listar informações de uma NFe")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            multiplicar(dados)
        elif opcao == "2":
            adicionar_peso(dados)
        elif opcao == "3":
            remover_empresa(dados)
        elif opcao == "4":
            listar(dados)
        elif opcao == "5":
            mudar_peso(dados)
        elif opcao == "6":
            calcularData()
        elif opcao == "7":
            xmlInfo()