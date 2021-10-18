import numpy as np

def matriz_rotacao(theta):
    theta_rad = (theta/180)*np.pi
    
    return np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                               [np.sin(theta_rad),  np.cos(theta_rad), 0],
                               [0, 0, 1]])

def matriz_escala(cx, cy):
    return np.array([[cx, 0, 0],
                     [0, cy, 0],
                     [0, 0, 1]])

def matriz_translacao_origem(xcentro, ycentro):
    return np.array([[1, 0, -xcentro],
                     [0, 1, -ycentro],
                     [0, 0, 1]])

def matriz_translacao_volta(xcentro, ycentro):
    return  np.array([[1, 0, xcentro],
                      [0, 1, ycentro],
                      [0, 0, 1]])

