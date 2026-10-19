import xmltodict
import pathlib
def xmlInfo():
    
    xmls = list(pathlib.Path(r'C:\Users\USER\Downloads').glob('*.xml'))
    for i, xml in enumerate(xmls, start=1):
        print(f"{i}. {xml}")

    escolha = int(input("\nEscolha a XML: ").strip()) - 1
    caminho = xmls[escolha]
    dadosNF = xmltodict.parse(open(caminho, 'rb'))
    numero_NF = dadosNF['nfeProc'] ['NFe'] ['infNFe'] ['ide'] ['nNF']
    itens = dadosNF['nfeProc']['NFe']['infNFe']['det']
    valorTotal = dadosNF['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF']
    chaveNFe = dadosNF['nfeProc']['protNFe']['infProt']['chNFe']
    pesoBruto = dadosNF['nfeProc']['NFe']['infNFe']['transp']['vol']['pesoB']
    print("\nNFº:", numero_NF)
    print("Chave NFe:", chaveNFe)
    for i, item in enumerate(itens, start=1):
        produto = item['prod']['xProd']
        quantidade = item['prod']['qCom']
        valor = item['prod']['vUnCom']
        print(f"{i}. {produto} +  ZINCADO" + " / " + "Q:", quantidade + " / " + "V: ", valor)
    print("Valor total: ", "R$ " + valorTotal)
    print("\nPeso bruto: " + pesoBruto)
    input("Aperte qualquer botão para voltar ao menu.")
    return