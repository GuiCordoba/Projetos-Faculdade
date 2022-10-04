''' Enunciado: Imagina-se que você está desenvolvendo um software de controle de estoque para uma mercearia. Este software deve ter o seguinte menu e opções:
1.Cadastrar Produto
2.Consultar Produto(s)
  1)Consultar Todas as Produto
  2)Consultar Produto por Código
  3)Consultar Produto(s) por Fabricante
  4)Retornar 
3.Remover Produto
4.Sair

Elabore um programa em Python que:
1.Deve-se codificar uma função cadastrarProduto (código) (EXIGÊNCIA 1);
   -Essa função recebe como parâmetro um código exclusivo para cada produto cadastrado (DICA: utilize um contador como parâmetro) 
   -Dentro da função perguntar o nome do produto;
   -Dentro da função perguntar o fabricante do produto;
   -Dentro da função perguntar o valor do produto
   -Cada produto cadastrado deve ter os seus dados armazenados num DICIONÁRIO (DICA: Conferir material escrito da p. 22 até p24  da AULA 06)
2.Deve-se codificar uma função consultarProduto(EXIGÊNCIA 2);
   -Dentro da função ter um menu com as seguintes opções:
     -Consultar Todos os Produtos
     -Consultar Produtos por Código
     -Consultar Produtos por Fabricante
     -Retornar
3.Deve-se codificar uma função chamada removerProduto (EXIGÊNCIA 3);
  -Dentro da função perguntar qual o código do produto que se deseja remover do cadastro (da lista de dicionário)
'''

listaProdutos = []        # lista no qual tera o dicionario com as informações dos produtos

#- Começo função cadastroProdutos ------------------------------------------------------------------------------------------------------------------
def cadastrarProdutos(codigo):    # código é uma variavel de uma funçáo local, portanto pode ter nome diferente de uma função global
    print('>>>>>Cadastro de Produtos')
    print(f'CÓDIGO do produto: {codigo}')           # o código de cada produto sera gerado altomaticamente
    nome = input('Qual o NOME do produto: ')
    fabricante = input('Qual o FABRICANTE do produto: ')
    valor = float(input('Qual o VALOR do produto (R$): '))
    adicionarProduto = {'Código' : codigo,                  # dicionario onde ira ficar armazenado as informações dos prdutos
                         'Nome' : nome,
                         'Fabricante' : fabricante,
                         'Valor' : valor}
    listaProdutos.append(adicionarProduto.copy())           # adicionando uma copia da  dicionarioProduto (dicionarioProduto.copy) na  listaProdutos

#- Fim função cadastroProdutos -----------------------------------------------------------------------------------------------------------------------

#- Começo função consultaProdutos --------------------------------------------------------------------------------------------------------------------
def consultarProdutos():
    while True:
        try:
            print('>>>>>Consulta de Produtos')
            consultar = int(input('Escola a opção desejada:\n'
                                  '1 - Consultar todos os produtos\n'
                                  '2 - Consultar produtos por código\n'
                                  '3 - Consultar produtos por fabricante\n'
                                  '4 - Retornar\n>>'))
            if consultar == 1:
                print('>>Consultar todos os produtos<<')
                for produto in listaProdutos:              # selecionar cada dicionario na minha lista (cada produto na lista de produtos)
                    for key, value in produto.items():     # selecionada cada conjunto chave : valor (ex: 'codigo' : codigo)
                        print(f'{key} : {value}')  # impressão dos valores de key e value
            elif consultar == 2:
                print('>>Consultar por código<<')
                entrada = int(input('Insira o código do produto: '))
                for produto in listaProdutos:
                    if (produto['Código'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif consultar == 3:
                print('>>Consultar por fabricante<<')
                entrada = input('Insira o fabricante do produto: ')
                for produto in listaProdutos:
                    if (produto['Fabricante'] == entrada):
                        for key, value in produto.items():
                            print(f'{key} : {value}')
            elif consultar == 4:
                return                                      # esse return volta no menu principal
            else:
                print('Opção inválida. Tente novamente!')
                continue
        except ValueError:
            print('Opção inválida. Tente novamente!')

#- Fim função consultaProdutos -----------------------------------------------------------------------------------------------------------------------

#- Comeco função removerProdutos ---------------------------------------------------------------------------------------------------------------------
def removerProdutos():
    print('>>>>>Remoção de Produtos')
    entrada = int(input('Insira o código do produto: '))
    for produto in listaProdutos:
        if (produto['Código'] == entrada):
            listaProdutos.remove(produto)                  # o produto que tiver o código digitado na entrada sera removido

#- Fim função removerProdutos -------------------------------------------------------------------------------------------------------------------------


#- Comeco MAIN ---------------------------------------------------------------------------------------------------------------------------------------
print('Bem vindo ao controle de estoque Supermercado Guilherme Mota Cordoba Lopes RU:4235924')
codigoProduto = 0                                          # variavel responsavel por receber um código exclusivo para cada produto
while True:
    try:                                                   # caso o valor digitado nao seja inteiro, cai no except
        opcao = int(input('Escolha a opção desejada:\n1 - Cadastrar produto\n2 - Consultar produto(s)\n3 - Remover produtos\n4 - Sair\n>>'))
        if opcao == 1:
            codigoProduto += 1                             # contador dos códigos de cada produto, ira acumular os produtos cadastrados
            cadastrarProdutos(codigoProduto)
        elif opcao == 2:
            consultarProdutos()
        elif opcao == 3:
            removerProdutos()
        elif opcao == 4:
            break
        else:
            print('Opção inválida, tente novamente!')
            continue
    except ValueError:
        print('Opção inválida, tente novamente!!!')
#- Fim  MAIN ------------------------------------------------------------------------------------------------------------------------------------------
