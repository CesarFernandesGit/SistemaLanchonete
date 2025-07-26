# SISTEMA DE LANCHONETE QUE ANOTA E CALCULA O PREÇO DOS ALIMENTOS

import time
import locale

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

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
    print(f"{i} - {cardapioAlimentos[i]} - R${precoAlimentos[i]:.2f}\n")
    
while True:
    try:
        escolhaAlimentos = int(input('Digite o número do item desejado para continuar: '))
        if 0 <= escolhaAlimentos < len(cardapioAlimentos):
            quantidade = int(input(f"Você selecionou {cardapioAlimentos[escolhaAlimentos]}, quantos gostaria de adicionar no pedido? "))
            break
        else:
            print('Valor inválido! Por favor, digite uma das opções descritas.')
    except:
        print('Valor inválido! Por favor, digite uma das opções descritas.')

print()

for i in range(len(escolhaAdicionar)):
    print(f"{i} - {escolhaAdicionar[i]}\n")

while True:
    try:
        escolha = int(input('Gostaria de adicionar alguma bebida no seu pedido? Digite 1 para Sim ou 0 para Não: '))

        if escolha == 0:
            print('Certo, estamos somando o total do seu pedido, por favor aguarde um instante.')
            break

        elif escolha == 1:
            while True: 
                try:
                    for i in range(len(cardapioBebidas)):
                        print(f"{i} - {cardapioBebidas[i]} - R${precoBebidas[i]:.2f}\n")

                    escolhaBebidas = int(input('Digite o número do item desejado para continuar: '))

                    if 0 <= escolhaBebidas < len(cardapioBebidas):
                        quantidade = int(input(f"Você selecionou {cardapioBebidas[escolhaBebidas]}, quantos gostaria de adicionar no pedido? "))
                        print()
                        break
                    else:
                        print('Valor inválido! Por favor, digite uma das opções descritas.')
                except:
                    print('Valor inválido! Por favor, digite uma das opções descritas.')
            break
        else:
            print('Valor inválido! Por favor, digite 1 para Sim ou 0 para Não.')
    except:
        print('Valor inválido! Por favor, digite uma das opções descritas.')
   
print('CALCULANDO O VALOR TOTAL DO PEDIDO...\n')
time.sleep(3)

valorTotalAlimentos = quantidade * precoAlimentos[escolhaAlimentos]
valorTotalBebidas = quantidade * precoBebidas[escolhaBebidas]
valorTotal = valorTotalBebidas + valorTotalAlimentos

print('O total do seu pedido ficou em {}\n'.format(locale.currency(valorTotal, grouping=True)))

for i in range(len(formaPagamento)):
    print(f"{i} - {formaPagamento[i]}\n")

escolhaPagamento = int(input('Qual será a forma de pagamento? '))

if escolhaPagamento == 0:
    pagamentoUsuario = float(input('Por favor, informe o valor a pagar: '))

    if pagamentoUsuario < valorTotal:
        print('O valor inserido é insuficiente. Por favor, informe novamente: ')
        print()
    elif pagamentoUsuario > valorTotal:
        trocoDinheiro = float(pagamentoUsuario - valorTotal)
    print('Aqui está o seu troco: {}\n'.format(locale.currency(trocoDinheiro, grouping=True)))
    print('Muito obrigado por comprar na PyLunch, volte sempre <3')
else:
    print('Tudo certo com o seu pagamento!\n')
    print('Muito obrigado por comprar na PyLunch, volte sempre <3')
