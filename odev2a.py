import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('a1.jpg')

# Gri tonlamalı görüntüye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenar tespiti için Canny algoritmasını uygula
edges = cv2.Canny(gray, 50, 150)

    # Gürültüyü azaltmak için Gaussian blur uygula
blurred = cv2.GaussianBlur(gray, (5, 5), 0)


# Hough Çizgi Dönüşümü ile çizgileri tespit et
lines = cv2.HoughLinesP(edges, rho=2, theta=np.pi/180, threshold=90, minLineLength=150, maxLineGap=30)


# Tespit edilen çizgileri görüntü üzerine çiz
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)

# Görüntüyü matplotlib ile göster
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Detected Lanes')
plt.axis('off')
plt.show()
