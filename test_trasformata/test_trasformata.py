# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:03:06 2021

@author: davide notaro
"""

import matplotlib.image as mpimg #libreria per mostrare immagini e grafici
import matplotlib.pyplot as plt #per visualizzare
from numpy.fft import fft2, fftshift, ifft2, ifftshift #ifft2 trasformata di fourier inversa
import numpy as np #pachetto di calcolo numerico
import random as rnd

numero_stampe = 0 #numero di plot attivi

im_base = mpimg.imread("nyc.jpg").astype(float)

mask_1 = mpimg.imread("mask_1.jpg")
mask_2 = mpimg.imread("mask_2.jpg")
mask_3 = mpimg.imread("mask_3.jpg")
mask_4 = mpimg.imread("mask_4.jpg")
mask_5 = mpimg.imread("mask_5.jpg")
mask_6 = mpimg.imread("mask_6.jpg")
mask_7 = mpimg.imread("mask_7.jpg")
mask_8 = mpimg.imread("mask_8.jpg")
mask_9 = mpimg.imread("mask_9.jpg")
mask_10 = mpimg.imread("mask_10.jpg")

filt_1 = mpimg.imread("nyc_filt_1.jpg")
filt_2 = mpimg.imread("nyc_filt_2.jpg")
filt_3 = mpimg.imread("nyc_filt_3.jpg")
filt_4 = mpimg.imread("nyc_filt_4.jpg")



def stampa_immagine(im):
    
    global numero_stampe #deve essere dichiarata come variabile globale
    
    plt.figure(numero_stampe)
    plt.imshow(im, cmap = 'gray')
    numero_stampe += 1


def applica_maschera(im, msk): #funzione che applica la maschera in input

    im = im.astype(float)
    msk = msk.astype(float)
    
    stampa_immagine(msk)
    
    ft_im = fftshift(fft2(im))
    prodotto = ifftshift(ft_im[:,:]*msk[:,:])
    im_msk = ifft2(prodotto)
    
    return np.abs(im_msk)
    

def applica_fase(im, fase): #funzione che sfasa la foto, angoli in gradi

    im = im.astype(float)
    fase = np.deg2rad(float(fase))
    
    fattore_fase = np.cos(fase) + (1j)*np.sin(fase)
    
    ft_im = fftshift(fft2(im))
    prodotto = ifftshift(ft_im[:,:]*fattore_fase)
    im_msk = ifft2(prodotto)
    
    return im_msk.astype(float)


def applica_funzione(im, f):
    
    im = im.astype(float)
    xv = len(im)
    yv = len(im[0])
    
    x = np.linspace(-.5,.5, xv)
    y = np.linspace(-.5,.5, yv)
    
    x_mask, y_mask = np.meshgrid(x, y)
    
    ft_im = fftshift(fft2(im))
    
    msk = f(x_mask,y_mask)
    
    stampa_immagine(msk)
    
    prodotto = ifftshift(ft_im[:,:]*msk[:,:])
    im_msk = ifft2(prodotto)
            
    return im_msk.astype(float)       
            
            
def gaussiano(x,y):
    
    sigma = 0.02
    return np.exp(-(x**2+y**2)/sigma**2) 

def gaussiano_inverso(x,y):
    
    sigma = 0.02
    return -np.exp(-(x**2+y**2)/sigma**2) + 1

def random_phase(im):
    
    im = im.astype(float)
    ft_im = fft2(im)
    k = 2*np.pi #fattore di sfasamento (da 0 a 2pi)
    
    rand_matrix = [[k*rnd.random() for x in range(len(im))] for y in range(len(im[0]))] 
    
    rand_matrix = np.asarray(rand_matrix) #converte la lista in un array numpy
    
    prodotto = ft_im[:,:]*np.exp(1j*rand_matrix[:,:])

    return np.abs(ifft2(prodotto))
    
    

def cosin(x,y):
    
    return (np.cos(100*x)**2 + np.sin(100*y)**2)

def ricava_filtro(im, im_filt):
    
    im = im.astype(float)
    im_filt = im_filt.astype(float)
    
    ft_im = fftshift(fft2(im))
    ft_im_filt = fftshift(fft2(im_filt))
    
    msk = ft_im_filt[:,:]/ft_im[:,:]
    
    return msk.astype("float")
    


# maschere = [mask_1, mask_2, mask_3, mask_4, mask_5, mask_6, mask_7, mask_8, 
#             mask_9, mask_10]
# funzioni = [gaussiano, gaussiano_inverso, cosin]

# filtri = [filt_1, filt_2, filt_3, filt_4]


# for mask in maschere:
#     stampa_immagine(applica_maschera(im_base, mask))

# for funz in funzioni:
#     stampa_immagine(applica_funzione(im_base, funz))

# for filt in filtri:
#     stampa_immagine(filt)
#     out = ricava_filtro(im_base, filt)
#     stampa_immagine(applica_maschera(im_base, out))



# random_phase(im_base)

stampa_immagine(random_phase(im_base))
            

