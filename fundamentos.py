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

in0 = skimage.img_as_float(i0)
in1 = skimage.img_as_float(i1)

#%% 8. Obtenção das dimensões da matriz que representa a imagem

(M0, N0) = np.shape(in0) # M0 linhas e N0 colunas
(M1, N1, D1) = np.shape(in1) # M1 linhas, N1 colunas e D1 camadas

#%% 10. Identificação e armazenamento de valores de interesse

maximo0 = np.max(in0)
minimo0 = np.min(in0)
media0 = np.mean(in0)
dP0 = np.std(in0)

maximo1 = np.max(in1)
minimo1 = np.min(in1)
media1 = np.mean(in1)
dP1 = np.std(in1)

#%% 11. Plot gráfico das imagens
plt.figure()
plt.ylabel('Linhas - M0')
plt.xlabel('Colunas - N0')
plt.title('image0 - raioXTorax')
plt.imshow(in0, cmap = 'gray') # cmap = 'jet' <- mapa de calor
plt.colorbar() # Mostra o gradiente de cores e respectivos valores normalizados

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1 - Lamina-biopsia RGB')
plt.imshow(in1, cmap = 'jet') # cmap = 'jet' <- mapa de calor RGB
plt.colorbar()

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1.0 - Lamina-biopsia Blue')
plt.imshow(in1[:,:,0], cmap = 'gray') # cmap = 'Blues' <- mapa de calor B
plt.colorbar()

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1.1 - Lamina-biopsia Green')
plt.imshow(in1[:,:,1], cmap = 'gray') # cmap = 'Greens' <- mapa de calor G
plt.colorbar()

plt.figure()
plt.ylabel('Linhas - M1')
plt.xlabel('Colunas - N1')
plt.title('image1.2 - Lamina-biopsia Red')
plt.imshow(in1[:,:,2], cmap = 'gray') # cmap = 'Reds' <- mapa de calor R
plt.colorbar()