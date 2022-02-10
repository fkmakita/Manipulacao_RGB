# -*- coding: utf-8 -*-
# Imagens Biomédicas 2021.1
# Laboratório 1 - Fabio Kenji Makita 120369

#%% 5. Bibliotecas utilizadas

import numpy as np
import matplotlib.pyplot as plt
import cv2 # OpenCV
import skimage
import skimage.exposure

#%% 6. Armazenamento dos dados da imagem em uma matriz i0

i0 = cv2.imread('raioXTorax.pgm', 0) # Gray
i1 =  cv2.imread('Lamina-biopsia.jpg', 1) # Color

#%% 7. Normalização entre 0 e 1, convertendo a intensidade para tipo float

im0 = skimage.img_as_float(i0)
im1 = skimage.img_as_float(i1)

#%% 8. Obtenção das dimensões da matriz que representa a imagem

(M0, N0) = np.shape(im0) # M0 linhas e N0 colunas
(M1, N1, D1) = np.shape(im1) # M1 linhas, N1 colunas e D1 camadas

#%% 10. Identificação e armazenamento de valores de interesse

max0 = np.max(im0)
min0 = np.min(im0)
mean0 = np.mean(im0)
std0 = np.std(im0)

max1 = np.max(im1)
min1 = np.min(im1)
mean1 = np.mean(im1)
std1 = np.std(im1)

#%% 11. Plot gráfico das imagens
plt.figure()
plt.ylabel('Linhas - M0')
plt.xlabel('Colunas - N0')
plt.title('image0 - raioXTorax')
plt.imshow(im0, cmap = 'gray') # cmap = 'jet' <- mapa de calor
plt.colorbar() # Mostra o gradiente de cores e respectivos valores normalizados

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1 - Lamina-biopsia RGB')
plt.imshow(im1, cmap = 'jet') # cmap = 'jet' <- mapa de calor RGB
plt.colorbar()

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1.0 - Lamina-biopsia Blue')
plt.imshow(im1[:,:,0], cmap = 'Blues') # cmap = 'Blues' <- mapa de calor B
plt.colorbar()
plt.savefig('Lamina-biopsia-Blue')

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1.1 - Lamina-biopsia Green')
plt.imshow(im1[:,:,1], cmap = 'Greens') # cmap = 'Greens' <- mapa de calor G
plt.colorbar()
plt.savefig('Lamina-biopsia-Green')

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1.2 - Lamina-biopsia Red')
plt.imshow(im1[:,:,2], cmap = 'Reds') # cmap = 'Reds' <- mapa de calor R
plt.colorbar()
plt.savefig('Lamina-biopsia-Red')