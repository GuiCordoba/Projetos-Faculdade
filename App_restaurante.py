'''Enunciado: Imagina-se que você e sua equipe foram contratados por um restaurante que serve feijoada para desenvolver a solução de software. 
Você ficou encarregado da parte de retirar pedido por parte do cliente. O valor que a empresa cobra por feijoada é dado pela seguinte equação:
total=(volume*opção)+adional(is)
Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:
1- Volume x Valor
---------------------------------------                  
|Volume (ml)	        |  Valor (R$) |
|volume < 300	        |Não é aceito |
|300  <= volume <= 5000	|volume * 0.08|
|volume > 5000	        |Não é aceito |
---------------------------------------
2 - Opção x Multiplicador
---------------------------------------------------------------------------------------------------------
|Peso(kg)	                                                                              |Multiplicador|
|b - Básica (Feijão + paiol + costelinha) 	                                              |    1.00     |
|p - Premium (Feijão + paiol + costelinha + partes de porco)	                          |    1.25     |
|s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)|    1.50     |
---------------------------------------------------------------------------------------------------------
3- Acompanhamento x Valor
------------------------------------------------------------------
|Aconpanhamento	                                      |Valor (R$)|
|0- Não desejo mais acompanhamentos (encerrar pedido) |   0,00   |
|1- 200g de arroz	                                  |   5,00   |
|2- 150g de farofa especial	                          |   6,00   |
|3- 100g de couve cozida                              |   7,00   |
|4- 1 laranja descascada	                          |   3,00   |
------------------------------------------------------------------

'''
#- INICIO DA FUNÇÃO VOLUME -------------------------------------------------------------------------------------------
def volumeFeijoada():  # funão para o calculo do valor referente ao volume da feijoada
    while True:
        try:                                       # caso o usuário insira valores não numéricos
            print('>>MENU VOLUME FEIJOADA<<')
            vol = float(input('Qual a quantidade desejada (ml): '))
            if (vol >= 300) and (vol <= 5000):
                return (vol * 0.08)
            else:
                print('**Não aceitamos quantidades menores que 300ml, ou maiores de 5000ml**')
                continue
        except ValueError:                         # erro referente as valores não numéricos
            print('**Insire apenas valores numéricos**')
            continue
#- FIM DA FUNÇÃO VOLUME -----------------------------------------------------------------------------------------------


#- INICIO DA FUNÇÃO OPCÃO ---------------------------------------------------------------------------------------------
def opcaoFeijoada():   # função para o calculo do multiplicador opção
    while True:
        print('''>>>MENU OPÇÃO FEIJOADA<<<
        Qaul opção deseja?
        b - Básica  (Feijão + Paiol + Costelinha)
        p - Premium (Feijão + Paiol + Costelinha + Partes do porco)
        s - Supreme (Feijão + Paiol + Costelinha + Partes do porco + charque + calabresa + bacon)
        ''')
        op = input('>>')
        if (op == 'b'):
            return 1
        elif (op == 'p'):
            return 1.25
        elif (op == 's'):
            return 1.5
        else:
            print('**Você não digitou uma opção válida. Tente novamente**')
            continue
#- FIM DA FUÇÃO OPCAO ---------------------------------------------------------------------------------------------------

#- INICIO DA FUNÇÃO ACOMPANHAMENTO --------------------------------------------------------------------------------------
def acompanhamentoFeijoada():   # função valor dos adicionais
    acompanhamento = 0          # acumulador dos acompanhamentos
    while True:
        print('''>>>MENU ACOMPANHAMENTO<<<
        Deseja mais algum acompanhamento?
        0 - Não desejo mais acompanhamento (encerrar pedido)
        1 - 200g de arroz
        2 - 150g de farofa especial
        3 - 100g de couve cozida
        4 - 1 laranja descacada
        ''')
        acomp = int(input('>>'))
        if (acomp == 0):
            return acompanhamento
        elif (acomp == 1):
            acompanhamento += 5
        elif (acomp == 2):
            acompanhamento += 6
        elif (acomp == 3):
            acompanhamento += 7
        elif (acomp == 4):
            acompanhamento += 3
        else:
            print('***Valor invalido. Tente novamente***')
            continue
#- FIM DA FUNÇÃO ACOMPANHAMENTO ----------------------------------------------------------------------------------------

#- INICIO DO MAIN-------------------------------------------------------------------------------------------------------
print('Bem-vindo ao programa de feijoada Guilherme Mota Cordoba Lopes RU:4235924!')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acomp = acompanhamentoFeijoada()
total = (volume * opcao) + acomp
print(f'O valor total a ser pago será: R${total}. (Volume = {volume} * opcao = {opcao} + acompanhamneto = {acomp}) ')
#- FIM DO MAIN-----------------------------------------------------------------------------------------------------------
 
