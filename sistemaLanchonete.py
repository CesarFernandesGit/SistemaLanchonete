# SISTEMA DE LANCHONETE QUE ANOTA E CALCULA O PREÇO DOS ALIMENTOS

import time

cardapioAlimentos = ["Cachorro Quente", "Hambúrguer", "Batata Frita", "Pastel"]
cardapioBebidas = ["Suco", "Refrigerante"]
escolhaAdicionar = ["Não", "Sim"]
precoAlimentos = [9.50, 15.00, 8.00, 10.00]
precoBebidas = [5.00, 6.00]
formaPagamento = ["Dinheiro", "Crédito", "Débito", "PIX"]

print('Olá, seja bem-vindo a lanchonete PyLunch! Basta aguardar que já te trazemos o cardápio.\n')

time.sleep(2)
print('CARREGANDO O CARDÁPIO...\n')
time.sleep(3)

for i in range(len(cardapioAlimentos)):
    print(f"{i} - {cardapioAlimentos[i]} - R${precoAlimentos[i]:.2f}")
    
try:
    escolhaAlimentos = int(input('Digite o número do item desejado para continuar: '))

    if 0 <= escolhaAlimentos < len(cardapioAlimentos):
        quantidade = int(input(f"Você selecionou {cardapioAlimentos[escolhaAlimentos]}, quantos gostaria de adicionar no pedido? \n"))
    else:
        print('Valor inválido! Por favor, digite uma das opções descritas.')
except:
    print('Valor inválido! Por favor, digite uma das opções descritas.')


for i in range(len(escolhaAdicionar)):
    print(f"{i} - {escolhaAdicionar[i]}\n")

escolha = int(input('Gostaria de adicionar alguma bebida no seu pedido? Digite 1 para Sim ou 0 para Não: \n'))

for i in range(len(cardapioBebidas)):
    print(f"{i} - {cardapioBebidas[i]} - R${precoBebidas[i]:.2f}\n")

if escolha == 0:
    print('Certo, estamos somando o total do seu pedido, por favor aguarde um instante')
else:
    escolhaBebidas = int(input('Digite o número do item desejado para continuar: '))
    quantidade = int(input(f"Você selecionou {cardapioBebidas[escolhaBebidas]}, quantos gostaria de adicionar no pedido? \n"))

print('CALCULANDO O VALOR TOTAL DO PEDIDO...\n')
time.sleep(3)

valorTotalAlimentos = quantidade * precoAlimentos[escolhaAlimentos]
valorTotalBebidas = quantidade * precoBebidas[escolhaBebidas]
valorTotal = valorTotalBebidas + valorTotalAlimentos

print('O total do seu pedido ficou em R${:.2f}\n'.format(valorTotal))

for i in range(len(formaPagamento)):
    print(f"{i} - {formaPagamento[i]}\n")

escolhaPagamento = int(input('Qual será a forma de pagamento? \n'))

if escolhaPagamento == 0:
    pagamentoUsuario = float(input('Por favor, informe o valor a pagar: \n'))

    if pagamentoUsuario < valorTotal:
        print('O valor inserido é insuficiente. Por favor, informe novamente: \n')
    elif pagamentoUsuario > valorTotal:
        trocoDinheiro = float(pagamentoUsuario - valorTotal)
    print('Aqui está o seu troco: {:.2f}\n'.format(trocoDinheiro))
    print('Muito obrigado por comprar na PyLunch, volte sempre <3')
else:
    print('Tudo certo com o seu pagamento!\n')
    print('Muito obrigado por comprar na PyLunch, volte sempre <3')
