import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fotoğrafı yükle
image = cv2.imread('arabablur.jpg')

# Gri tonlamalı görüntüye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenarları belirginleştirmek için Laplacian filtresi uygula
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Keskinleştirilmiş görüntüyü elde etmek için orijinal görüntü ile filtrelenmiş görüntüyü birleştir
sharpened = cv2.addWeighted(gray, 1.5, laplacian, -0.5, 0, dtype=cv2.CV_64F)

# Gri tonları kaldırmak için renkli görüntüyü kullan
color_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Sonucu göster
plt.imshow(color_image)
plt.title('Color Image without Gray Tones')
plt.axis('off')
plt.show()
