import matplotlib.pyplot as plt

#variáveis para região e custo
regioes = ["São Paulo", "Virgínia do Norte"]
custos = [17.38, 10.13]

#Grafico

plt.figure(figsize=(6,5), facecolor="whitesmoke") #define o tamanho (largura, altura)

barras = plt.bar(regioes, custos, color=["turquoise", "lime"], width=0.6) #cria o grafico de barra e adiciona cor

for barra in barras:
    altura = barra.get_height() #pega o valor da barra
    plt.text(barra.get_x() + barra.get_width()/2, altura, f"{altura:.2f} USD", ha="center", va="bottom") #coloca os valores centralizados em cima da barra

plt.title("Gráfico Representativo") #título
plt.xlabel("Regiões") #nome do x
plt.ylabel("Custo mensal (USD)") #nome do y
plt.margins(x=0.2)


plt.savefig("assets/imagens_entrega2/grafico_custo.png", dpi=300) #salva como imagem
plt.show() #mostra o grafico

