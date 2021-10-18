# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:59:30 2021

@author: luisc
"""

# Exemplos de call-backs do Matplotlib para a interação com o usuário
# Para terminar o programa, pressione a tecla 'a'

import numpy as np
import matplotlib.pyplot as plt
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
    if event.key == 'q': 
        end_loop = True
    elif event.key == 'up':
        velocidade_rotacao += 0.5
    elif event.key == 'down':
        velocidade_rotacao -= 0.5
    elif event.key == 'left':
        velocidade_translacao += 0.05
    elif event.key == 'right':
        velocidade_translacao -= 0.05
    
