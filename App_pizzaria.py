'''Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma pizzaria. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Pizzaria possui seguinte tabela de sabores de pizzas listados com sua descrição, códigos e valores:

|Codigo| Descrição  | Pizza Média | Pizza Grande |
|  21  | Napolitano |   R$20,00   |   R$26,00    |
|  22  | Margherita |   R$20,00   |   R$26,00    |
|  23  | Calabresa  |   R$25,00   |   R$32,50    |    
|  24  | Toscana    |   R$30,00   |   R$39,00    |
|  25  | Portuguesa |   R$30,00   |   R$39,00    |

Elabore um programa em Python que:
1.	Entre com o tamanho da pizza
2.	Entre com o código do produto desejado;
3.	Pergunte se o cliente quer pedir mais alguma coisa (se sim repetir a partir do item 1.  Caso contrário ir para próximo passo); 
4.	Encerre a conta do cliente com o valor total;
5.	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 3);
6.	Se a pessoa digitar um TAMANHO de pizza e/ou   NÚMERO diferente dos da tabela printar na tela: ‘opção inválida’ e voltar para o menu (EXIGÊNCIA 2 de 3);
7.	Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);
o	(DICA: utilizar o continue dentro else que verifica a opção inválida)
o	(DICA: utilizar o break dentro if que verifica a opção sair)

'''

print('Bem-vindo a pizzaria Guilherme Mota Cordoba Lopes RU:4235924!')
print('''---------------------Cardápio----------------------
|Código| Descrição  | Pizza Média | Pizza Grande |
|  21  | Napolitano |   R$20,00   |   R$26,00    |
|  22  | Margherita |   R$20,00   |   R$26,00    |
|  23  | Calabresa  |   R$25,00   |   R$32,50    |    
|  24  | Toscana    |   R$30,00   |   R$39,00    |
|  25  | Portuguesa |   R$30,00   |   R$39,00    |''')

total = 0 #Acumulador para fazer a soma total das pizzas

while True: # Laco de repeticao
    tamanho = (input('Qual tamanho deseja (M - Média, G - Grande): '))
    if (tamanho == 'M' or  tamanho == 'G'): # Valida se o tamanho esta correto
      codigo = int(input('Isira o código do sabor: '))
      if (tamanho == 'M' and codigo == 21): # Valida os dados de tamanho e sabor 
        total = total + 20
        sabor = 'Pizza Napolitana'
        valor = 'R$20,00' 
      elif (tamanho == 'G' and codigo == 21):
        total = total + 26
        sabor = 'Pizza Napolitana'
        valor = 'R$26,00' 
      elif (tamanho == 'M' and codigo == 22):
        total = total + 20
        sabor = 'Pizza Margherita'
        valor = 'R$20,00' 
      elif (tamanho == 'G' and codigo == 22):
        total = total + 26
        sabor = 'Pizza Margherita'
        valor = 'R$26,00' 
      elif (tamanho == 'M' and codigo == 23):
        total = total + 25
        sabor = 'Pizza Calabresa'
        valor = 'R$25,00' 
      elif (tamanho == 'G' and codigo == 23):
        total = total + 32.50
        sabor = 'Pizza Calabresa'
        valor = 'R$32,50'
      elif (tamanho == 'M' and codigo == 24):
        total = total + 30
        sabor = 'Pizza Toscana'
        valor = 'R$30,00'
      elif (tamanho == 'G' and codigo == 24):
        total = total + 39
        sabor = 'Pizza Toscana'
        valor = 'R$39,00' 
      elif (tamanho == 'M' and codigo == 25):
        total = total + 30
        sabor = 'Pizza Portuguesa'
        valor = 'R$30,00'   
      elif (tamanho == 'G' and codigo == 25):
        total = total + 39
        sabor = 'Pizza Portuguesa'
        valor = 'R$39,00'
      else:
        print('Opção invalida!') 
        continue  
      print('Você pediu uma {} no valor de {}'.format(sabor, valor)) # Exibe na tela oque foi pedido
    else:
      print('Opcao invalida!')
      continue
    novopedido = int(input('Deseja algo mais? [1 - Sim / 0 - Não]')) # Verifica se deseja pedir algo mais
    if (novopedido == 1):
      continue 
    elif (novopedido == 0):
      print('O total do seu pedido ficou: {:.2f}'.format(total))
      break
    else:
      print('Opção invalida!')
      continue
print('Obrigado pela preferência!')