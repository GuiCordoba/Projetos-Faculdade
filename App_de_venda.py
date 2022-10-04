'''Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X 
que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade conforme a tabela abaixo:
---------------------------------------
|Quantidades 	      | Desconto      |
|Até 4	              | 0% na unidade |
|Entre 5 e 19	      | 3% na unidade |
|Entre 20 e 99	      | 6% na unidade |
|Maior ou igual a 100 |	10% na unidade|
---------------------------------------
Elabore um programa em Python que:
1.	Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
2.	Entre com a quantidade desse produto;
3.	O programa deve retornar o valor total sem desconto;
4.	O programa deve retornar o valor total após o desconto;
5.	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
'''


print('Bem-vindo a loja Guilherme Mota Cordoba Lopes RU:4235924!')

valor_unitario = float(input('Insira o valor unitario do produto: R$'))
quantia = int(input('Quantas unidades deseja comprar:'))

sem_desc = valor_unitario * quantia
print('Valor sem o desconto: R${:.2f}'.format(sem_desc))

if (quantia <= 4):
    print('Aplicamos desconto a partir de 5 unidades!')   # coloquei uma mensagem caso o numero de produtos seja menor que 5
elif ( 4 < quantia <= 19):
    com_desc = sem_desc - (sem_desc * 0.03)               # aprlicando o desconto de acordo com a quantidade
    print('Valor com deconto: R${:.2f}.    (desconto 3%)'.format(com_desc))
elif (19 < quantia <= 99):
    com_desc = sem_desc - (sem_desc * 0.06)
    print('Valor com desconto: R${:.2f}.   (desconto 6%)'.format(com_desc))
else:
    com_desc = sem_desc - (sem_desc * 0.1)             
    print('Valor com desconto: R${:.2f}.   (desconto 10%)'.format(com_desc))
