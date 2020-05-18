# -*- coding: utf-8 -*-

# Lista de exercicio 06

# Exercicio 4

# importando as bibliotecas

import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

# informacoes da tabela relativas aos dados masculino e feminino (IBGE)

idade = np.array(
    ["0 a 4 anos", "5 a 9 anos", "10 a 14 anos", "15 a 19 anos", "20 a 24 anos", "25 a 29 anos",
     "30 a 34 anos", "35 a 39 anos", "40 a 44 anos", "45 a 49 anos", "50 a 54 anos", "55 a 59 anos",
     "60 a 64 anos", "65 a 69 anos", "70 a 74 anos", "75 a 79 anos", "80 a 84 anos", "85 a 89 anos",
     "90 a 94 anos", "95 a 99 anos", "100 anos e mais"])

feminino = np.array([6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407,
                     4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989])

masculino = np.array([7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995,
                      3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247])

pop = [x for x in range( len(idade) ) ]

# Configuracao do grafico

plt.figure(figsize=(10, 8))

plt.suptitle('Distribuição da População por sexo segundo os grupos de idade – Brasil – 2010', fontsize=18)

plt.rc('axes.spines', **{'bottom': True, 'left': False, 'right': False, 'top': False})  # remove as linhas da figura

# Subplot masculino
plt.subplot(221)
plt.barh(idade, masculino, align='center', color='blue', linewidth=0.5, label='Masculino')
plt.xticks([0, 2000000, 4000000, 6000000, 8000000], ["", "", "4000000"])

plt.legend(loc='upper left') # legenda

plt.subplots_adjust(left=0.15, wspace=0.4)  # coloca espaco entre os graficos

plt.gca().invert_xaxis()  # inverte

plt.yticks([])  # remove o eixo y

# colocando linhas
plt.axvline(8000000, color='grey', alpha=0.15)
plt.axvline(6000000, color='grey', alpha=0.15)
plt.axvline(4000000, color='grey', alpha=0.15)
plt.axvline(6000000, color='grey', alpha=0.15)
plt.axvline(2000000, color='grey', alpha=0.15)
plt.axvline(0, color='black', alpha=0.20)

# subplot feminino
plt.subplot(222)
plt.barh(idade, feminino, align='center', color='orange', linewidth=0.5, label='Feminino')
plt.xticks([0, 2000000, 4000000, 6000000, 8000000], ["0", "", "4000000"], )

plt.legend(loc='upper right') # legenda

# colocando linhas
plt.axvline(8000000, color='grey', alpha=0.15)
plt.axvline(6000000, color='grey', alpha=0.15)
plt.axvline(4000000, color='grey', alpha=0.15)
plt.axvline(6000000, color='grey', alpha=0.15)
plt.axvline(2000000, color='grey', alpha=0.15)
plt.axvline(0, color='black', alpha=0.30)

plt.show();
