import numpy as np
import matplotlib.pyplot as plt
import matrizes as mt
import callback as cb

# Hexagono
hx = np.array([[2,1,1],
                [1,2,1],
                [2,3,1],
                [3,3,1],
                [4,2,1],
                [3,1,1]])

# Triângulo
#hx = np.array([[2,2,1], [4,2,1], [3,4,1]])

# Quadrado
hx = np.array([[1,1,1], [1,2,1], [2,2,1], [2,1,1]])

po = np.transpose(hx)

xmin = np.amin(po[0,:])
xmax = np.amax(po[0,:])

ymin = np.amin(po[1,:])
ymax = np.amax(po[1,:])

xcentro = ( xmin + xmax)/2
ycentro = ( ymin + ymax)/2

#plt.figure(figsize=(xmax*3, ymax*3))

plt.close('all')            # Fecha todas as figuras abertas
fig, ax = plt.subplots()    # Instancia objetos: figura e eixos correspondentes
ax.cla() 

cid = fig.canvas.mpl_connect('button_press_event', cb.on_press)
cid = fig.canvas.mpl_connect('key_press_event', cb.on_key)

cx = 1.0
cy = 1.0
aumenta = True
cb.end_loop = False

while not cb.end_loop:
    for theta in range(0, 361, 5):
        
        if cb.end_loop == True:
            break
        
        theta_rad = (theta/180)*np.pi
        
        tr_1 = np.matmul(mt.matriz_rotacao(theta_rad), mt.matriz_translacao_origem(xcentro, ycentro))
        tr_2 = np.matmul(mt.matriz_escala(cx, cy), tr_1)
        tr_3 = np.matmul(mt.matriz_translacao_volta(xcentro, ycentro), tr_2)    
        
        matriz_final = np.matmul(tr_3, po)
        
        matriz_transl = np.matmul(mt.matriz_rotacao(theta_rad), matriz_final)
        
        plt.clf()
        plt.xlim((-xmax*4, xmax*4)), plt.ylim((-ymax*4, ymax*4))
       # plt.axhline(linewidth=1), plt.axvline(linewidth=1)
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



