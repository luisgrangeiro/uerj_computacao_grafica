
import numpy as np
import matplotlib.pyplot as plt
import matrizes as mt
import callback as cb
from matplotlib.backend_bases import MouseButton

escala_lim_sup = 1
escala_lim_inf = escala_lim_sup/2

# Função que gerencia eventos do mouse
def on_press(event):
    print('Você pressionou o botão do mouse:', event.button, event.xdata, event.ydata)
    global escala_lim_sup
    
    if event.button is MouseButton.LEFT:
        escala_lim_sup = 1.5 * escala_lim_sup
    elif event.button is MouseButton.RIGHT:
        escala_lim_sup = escala_lim_sup*0.75

# Função que gerencia eventos do teclado
def on_key(event):
    global end_loop
    global velocidade_rotacao
    global velocidade_translacao
    global escala
    
    print('Você pressionou a tecla: "', event.key, '"', event.xdata, event.ydata)
    if event.key == 'escape': 
        end_loop = True
    elif event.key == 'up':
        velocidade_rotacao += 0.5
    elif event.key == 'down':
        velocidade_rotacao -= 0.5
    elif event.key == 'left':
        velocidade_translacao += 0.5
    elif event.key == 'right':
        velocidade_translacao -= 0.5
    

def matriz_rotacao(theta):
    theta_rad = (theta/180)*np.pi
    
    return np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                               [np.sin(theta_rad),  np.cos(theta_rad), 0],
                               [0, 0, 1]])

def matriz_escala(cx, cy):
    return np.array([[cx, 0, 0],
                     [0, cy, 0],
                     [0, 0, 1]])

def matriz_translacao_origem(centro_eixo_x, centro_eixo_y):
    return np.array([[1, 0, -centro_eixo_x],
                     [0, 1, -centro_eixo_y],
                     [0, 0, 1]])

def matriz_translacao_volta(centro_eixo_x, centro_eixo_y):
    return  np.array([[1, 0, centro_eixo_x],
                      [0, 1, centro_eixo_y],
                      [0, 0, 1]])

matriz = np.array([[2,2,1], [4,2,1], [3,4,1]])

po = np.transpose(matriz)

xmin = np.amin(po[0,:])
xmax = np.amax(po[0,:])

ymin = np.amin(po[1,:])
ymax = np.amax(po[1,:])

centro_eixo_x = ( xmin + xmax)/2
centro_eixo_y = ( ymin + ymax)/2


plt.close('all')            
fig, ax = plt.subplots()
ax.cla() 

cid = fig.canvas.mpl_connect('button_press_event', on_press)
cid = fig.canvas.mpl_connect('key_press_event', on_key)

cx = 1.0
cy = 1.0
aumenta = True
end_loop = False

velocidade_rotacao = 1
velocidade_translacao = 1

while not end_loop:
    for theta in range(0, 361, 5):      
        
        
        escala_lim_inf = escala_lim_sup/2
        
        if end_loop == True:
            break
        
        theta_rad = theta*velocidade_rotacao
        
        theta_2 = theta*velocidade_translacao
        
        if(theta_2 > 360):
            continue        
        
        theta_rad = (theta/180)*np.pi
        
        rotaciona = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                                   [np.sin(theta_rad),  np.cos(theta_rad), 0],
                                   [0, 0, 1]])
        
        tr_1 = np.matmul(rotaciona, mt.matriz_translacao_origem(centro_eixo_x, centro_eixo_y))
        tr_2 = np.matmul(mt.matriz_escala(cx, cy), tr_1)
        tr_3 = np.matmul(mt.matriz_translacao_volta(centro_eixo_x, centro_eixo_y), tr_2)    
        
        matriz_final = np.matmul(tr_3, po)
        
        matriz_transl = np.matmul(mt.matriz_rotacao(theta_2), matriz_final)       
        
        
        plt.xlim((-xmax*4, xmax*4)), plt.ylim((-ymax*4, ymax*4)) # MUDAR
        
        
        xlist = np.append(matriz_transl[0, :], matriz_transl[0, 0])
        ylist = np.append(matriz_transl[1, :], matriz_transl[1, 0])
        plt.plot(xlist, ylist, '-r',)
        plt.show()
        plt.pause(0.001)
        plt.clf()
        
        if aumenta:
            cx = cx + 0.03
            cy = cy + 0.03
        else:
            cx = cx - 0.03
            cy = cy - 0.03
        
        if(cx >= escala_lim_sup):
            aumenta = False
        if(cx <= escala_lim_inf):
            aumenta = True