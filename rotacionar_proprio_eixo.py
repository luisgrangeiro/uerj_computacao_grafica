import numpy as np
import matplotlib.pyplot as plt

po = np.array([[1,1,1], [1,2,1], [2,2,1], [2,1,1]])
po = np.transpose(po)

xmin = np.amin(po[0,:])
xmax = np.amax(po[0,:])

ymin = np.amin(po[1,:])
ymax = np.amax(po[1,:])

xcentro = ( xmin + xmax)/2
ycentro = ( ymin + ymax)/2

plt.figure(figsize=(10,10))

matriz_translacao_origem = np.array([[1, 0, -1.5],
                                    [0, 1, -1.5],
                                    [0, 0, 1]])
                                    
matriz_translacao_volta = np.array([[1, 0, 1.5],
                                   [0, 1, 1.5],
                                   [0, 0, 1]])                                          

cx = 1.0
cy = 1.0
aumenta = True

for theta in range(0, 361, 6): 
    
    
        
    matriz_rotacao = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                               [np.sin(theta_rad), np.cos(theta_rad), 0],
                               [0, 0, 1]])
    
    matriz_escala = np.array([[cx, 0, 0],
                              [0, cy, 0],
                              [0, 0, 1]])
    
    
    rot_origem = np.matmul(matriz_rotacao, matriz_translacao_origem)
    
    rot_origem_escala = np.matmul(matriz_escala, rot_origem)
    
    transformacao_2 = np.matmul(matriz_translacao_volta, rot_origem_escala)
    
    matriz_final = np.matmul(transformacao_2, po)
    
    matriz_transl = np.matmul(matriz_rotacao, matriz_final)
    
    plt.clf()
    plt.xlim((-10, 10)), plt.ylim((-10, 10))
    plt.axhline(linewidth=1), plt.axvline(linewidth=1)
    xlist = np.append(matriz_transl[0, :], matriz_transl[0, 0])
    ylist = np.append(matriz_transl[1, :], matriz_transl[1, 0])
    plt.plot(xlist, ylist, '-r',)
    plt.fill_between(xlist, ylist)
    plt.show()
    plt.pause(0.001)

    
    if aumenta:
        cx += 0.1
        cy += 0.1
    else:
        cx -= 0.1
        cy -= 0.1
    
    if(cx >= 2):
        aumenta = False
    if(cx <= 0.5):
        aumenta = True




