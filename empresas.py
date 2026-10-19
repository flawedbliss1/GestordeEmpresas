from data_save import salvar_dados, carregar_dados

dados = carregar_dados()
def adicionar_peso(dados):
    nome = input("Nome da empresa: ").strip()
    peso = float (input("Insira o peso: "))
    dados[nome] = peso
    salvar_dados(dados)
    print(f"\nPeso {peso} salvo para {nome}!\n")
def listar(dados):
    carregar_dados()
    print("- - - - - - - - - - - - - -")
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome} (peso: {dados[nome]:.2f})" "")
    print("- - - - - - - - - - - - - -")

def mudar_peso(dados):
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome} (peso: {dados[nome]:.2f})")
    print("\nEscolha a empresa que você quer mudar os dados: ")
    escolha = int(input().strip()) - 1

    peso = nomes[escolha]
    novo_peso = float(input("Insira o peso: "))
    dados[peso] = novo_peso
    salvar_dados(dados)
    print(f"\nPeso de {peso} atualizado para {novo_peso}!")

def remover_empresa(dados):
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome} (peso: {dados[nome]:.2f})")
    print("\nEscolha a empresa que você quer remover (escreva 0 para não remover): ")

    escolha = int(input().strip()) - 1

    if escolha < 0 or escolha >= len(nomes):
        return
    else:
        remocao = nomes[escolha]
        dados.pop(remocao)
        salvar_dados()
        print(remocao, "removido com sucesso.\n")

def multiplicar(dados):
    if not dados:
        print("\nEmpresa não cadastrada")
        return
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print (f"{i}. {nome} (peso: {dados[nome]:.2f})")
    print("\nEscolha uma empresa: ")
    escolha = int(input().strip()) - 1

    nome = nomes[escolha]
    peso = dados[nome]
    quantidade = float(input("Quantidade: "))
    total = quantidade * peso
    print(f"Total: {total:.2f}\n")