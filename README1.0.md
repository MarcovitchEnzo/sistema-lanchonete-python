# Sistema de Pedido - Lanchonete (Python)
## Sobre o Projeto
Este é um projeto simples desenvolvido em Python com o objetivo de praticar conceitos básicos da linguagem, como:
* Variáveis
* `input()` e `print()`
* Condicionais (`if`)
* Operações matemáticas
* Conversão de tipos (`int()`)

O sistema simula um pedido em uma lanchonete, permitindo que o usuário escolha um produto, defina a quantidade, selecione a forma de pagamento e revise o pedido antes da confirmação.
O programa executa as seguintes etapas:

### 1. Identificação do Cliente
* Solicita o nome do cliente antes de iniciar o pedido.

### 2. Exibição do Cardápio
O sistema apresenta três opções:
* Cod1 - Hambúrguer → R$ 15
* Cod2 - Pizza → R$ 25
* Cod3 - Refrigerante → R$ 8

### 3. Escolha do Produto
* O usuário deve digitar o código do produto (ex: `Cod1`).
* O sistema associa o código ao nome do produto e ao preço correspondente.

### 4. Quantidade
* O cliente informa quantas unidades deseja.

### 5. Cálculo do Valor Total
* O sistema calcula o valor total com base no preço e na quantidade.

### 6. Forma de Pagamento
O usuário pode escolher entre:
* Crédito → Acréscimo de 10% no valor total.
* Pix → Desconto de 10% no valor total.

### 7. Revisão do Pedido
O sistema exibe:
* Nome do cliente
* Produto escolhido
* Quantidade
* Forma de pagamento
* Total a pagar

### 8. Confirmação Final
O cliente deve confirmar se o pedido está correto:
* Se responder "Não", o sistema orienta a fazer um novo pedido.
* Se responder "Sim", o sistema finaliza com uma mensagem de agradecimento.
  
## Instruções Importantes
Para o funcionamento correto do sistema:
* O usuário deve respeitar a grafia dos códigos (ex: `Cod1`, `Cod2`, `Cod3`).
* A forma de pagamento deve ser digitada exatamente como:
  * `Crédito`
  * `Pix`
* A confirmação final deve ser:
  * `Sim`
  * `Não`
O sistema é sensível a maiúsculas, minúsculas e acentuação.

## Objetivo do Projeto
Este projeto foi criado com fins educacionais para reforçar:
* Lógica de programação
* Organização de código em etapas
* Estruturação de um pequeno sistema interativo
* Evolução gradual do código conforme novos conceitos são aprendidos

## Autor
Enzo Marcovitch Lêdo Espírito Santo
