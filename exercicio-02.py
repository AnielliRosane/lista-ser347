# -*- coding: utf-8 -*-

# Lista de exercicio 06

# Exercicio 2

# importando as bibliotecas
import matplotlib as plt
import matplotlib.pyplot as plt

# informacoes da tabela relativas aos dados feminino

idade = ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54",
         "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100"]

feminino = [6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407,
            4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989]

# contruindo o grafico de barra vertical

dist_pop_femi = [x for x in range(len(idade))]

plt.figure(figsize=(8, 8))

# Definindo o grafico vertical

plt.bar(dist_pop_femi, feminino, align='center', color='purple', linewidth=0.5, edgecolor='black')

# Alterando os eixos y,x

plt.yticks([0, 1000000, 3000000, 6000000, 9000000],
           ["0", "1 milhão", "3 milhões", "6 milhões", "9 milhões"])
plt.xticks(dist_pop_femi, idade, rotation=45)

# informações que vão no grafico
plt.title("Distribuição da população feminina no Brasil em 2010", fontsize=20)
plt.xlabel("Idade", fontsize=16)
plt.ylabel("Estimativa", fontsize=16)

# mostrando o grafico
plt.show();
