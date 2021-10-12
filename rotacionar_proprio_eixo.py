import numpy as np
import matplotlib.pyplot as plt

po = np.array([[1,1,1], [1,2,1], [2,2,1], [2,1,1]])
po = np.transpose(po)

plt.figure(figsize=(5,5))

matriz_translacao_origem = np.array([[1, 0, -1.5],
                                    [0, 1, -1.5],
                                    [0, 0, 1]])
                                    
matriz_translacao_volta = np.array([[1, 0, 1.5],
                                   [0, 1, 1.5],
                                   [0, 0, 1]])            
                                   
for theta in range(0, 361, 8):
    
    theta_rad = (theta/180)*np.pi
                       
    matriz_rotacao = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                               [np.sin(theta_rad), np.cos(theta_rad), 0], 
                               [0, 0, 1]])
    
    transformacao_1 = np.matmul(matriz_rotacao, matriz_translacao_origem)
    transformacao_2 = np.matmul(matriz_translacao_volta, transformacao_1)
    
    matriz_final = np.matmul(transformacao_2, po)
    
    plt.clf()
    plt.xlim((-5,5)), plt.ylim((-5,5))
    plt.axhline(linewidth=1), plt.axvline(linewidth=1)
    xlist = np.append(matriz_final[0,:], matriz_final[0,0])
    ylist = np.append(matriz_final[1,:], matriz_final[1,0])
    plt.plot(xlist, ylist, '-ro')
    plt.show()
    plt.pause(0.001)
    



