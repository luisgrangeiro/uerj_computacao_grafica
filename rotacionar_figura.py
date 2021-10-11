"""
Cria uma matriz representando os pontos de um quadrado,
e utiliza a matriz de rotação para fazer a figura realizar
um movimento de translação em volta da origem.
"""

import numpy as np
import matplotlib.pyplot as plt

p = np.array([[0,0], [0,1], [1,1], [1,0]])
p = np.transpose(p)

print(p)

plt.figure(figsize=(5,5))

theta = 0.0

for i in range(180):
    plt.clf()
    theta_rad = (theta/180)*np.pi # Converte o angulo para radiano
    
    # Cria a matriz de transformação para o movimento de rotação
    T = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                  [np.sin(theta_rad), np.cos(theta_rad)]])
    
    pT = np.matmul(T, p)
    
    plt.xlim(-5,5), plt.ylim(-5,5)
    plt.axhline(linewidth=1), plt.axvline(linewidth=1)
    
    xline = np.append(pT[0,:], pT[1,0])
    yline = np.append(pT[1,:], pT[0,0])
    
    plt.plot(xline, yline, '-ro')
    
    plt.show()
    theta += 2



