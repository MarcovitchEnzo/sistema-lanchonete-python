#Pedido Simples Lanchonete

#Divisão em Etapas:
#1-Perguntar o nome do cliente
#2-Exibir o Cardápio
#3-Perguntar qual opção o cliente deseja
#4-Perguntar a quantidade
#5-Calcular o Valor Total
#6-Perguntar a Forma de Pagamento
#7-Revisar o Pedido
#8-Confirmar se o Pedido está correto
#9-Mensagem de conclusão

#1
print("AVISO: PARA UTILIZAR O SISTEMA CORRETAMENTE, RESPEITE A GRAMÁTICA UTILIZADA!")
nome=input("Olá, antes de começar seu pedido, como você se chama?")
print("Olá",nome,",o que você deseja pedir?")

#2
print("Cod1-Hambúrguer = R$15")
print("Cod2-Pizza = R$25")
print("Cod3-Refrigerante = R$ 8")

op1=15
op2=25
op3=8

pe1="Hambúrguer"
pe2="Pizza"
pe3="Refrigerante"

#3
pedido=input("Para escolher uma opção, digite o código referente ao que deseja pedir (Ex: Cod1)")
if pedido=="Cod1":
    pedido=op1
    pe=pe1
if pedido=="Cod2":
    pedido=op2
    pe=pe2
if pedido=="Cod3":
    pedido=op3
    pe=pe3

#4
quantia=input("Quantos você vai querer?")

#5
vt=int(pedido)*int(quantia)

#6
pgt=input("Qual será a forma de pagamento?")
print("(As opções são Crédito e Pix)")

if pgt=="Crédito":
    print("No crédito, é adicionado uma taxa de 10% no valor total!")
    vt=int(vt)+int((vt/100)*10)
if pgt=="Pix":
    print("No pix, você ganha um desconto de 10% no valor total!")
    vt=int(vt)-int((vt/100)*10)


#7
print("REVISAR PEDIDO:")
print("Cliente:", nome)
print("Produto Escolhido:", pe)
print("Quantidade Pedida:", quantia)
print("Forma de Pagamento:", pgt)
print("Total a Pagar:", vt)

#8

rev=input("Seu pedido está correto? (Responda com Sim ou Não)")
if rev=="Não":
    print("Por favor, faça um novo pedido!")
if rev=="Sim":
    print("Agradecemos o seu pedido", nome)
    print("Volte sempre!")