import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Görüntüyü yükle ve RGB formatına dönüştür
image = cv2.imread('say.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Koyu yeşil için renk eşik değerlerini belirle
lower_green = np.array([0, 100, 0], dtype='uint8')
upper_green = np.array([50, 255, 50], dtype='uint8')

# Mask oluştur
mask = cv2.inRange(image_rgb, lower_green, upper_green)

# Bağlantılı bileşenleri tespit et
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Konturları çiz (mavi renkte)
result = image_rgb.copy()
cv2.drawContours(result, contours, -1, (0, 0, 255), 2)

# Görüntüleri göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap='gray')
plt.title('Maske')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(result)
plt.title('Bağlantılı Bileşenler')
plt.axis('off')

plt.show()

# Görüntüyü tekrar yükle ve Gri formatına dönüştür
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# DataFrame oluştur
df = pd.DataFrame(columns=['No', 'Center', 'Length (px)', 'Width (px)', 'Diagonal (px)', 'Energy', 'Entropy', 'Mean', 'Median'])

# Her bir koyu yeşil alan için özellikleri hesapla ve DataFrame'e ekle
for idx, cnt in enumerate(contours, start=1):
    # MinAreaRect ile dikdörtgeni al
    rect = cv2.minAreaRect(cnt)
    center, size, angle = rect
    width, height = size
    diagonal = np.sqrt(width ** 2 + height ** 2)

    # Maske oluştur
    mask_temp = np.zeros_like(mask)
    cv2.drawContours(mask_temp, [cnt], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Maskeyi uygula ve gri tonlamalı hale dönüştür
    masked_gray_temp = cv2.bitwise_and(image_gray, image_gray, mask=mask_temp)

    # Enerji hesapla
    energy = np.sum(masked_gray_temp ** 2)

    # Entropi hesapla
    histogram = cv2.calcHist([masked_gray_temp], [0], mask_temp, [256], [0, 256])
    histogram = histogram / histogram.sum()  # Normalize histogram
    entropy = -np.sum(histogram * np.log2(histogram + 1e-10))  # Avoid log(0) with small epsilon

    # Ortalama ve Medyan hesapla
    mean_value = np.mean(masked_gray_temp[masked_gray_temp > 0])
    median_value = np.median(np.sort(masked_gray_temp[masked_gray_temp > 0]))  # Sıfır olmayan piksellerin medyanını hesapla

    # DataFrame'e ekle (Piksel cinsinden özellikler)
    df.loc[idx] = [idx, center, max(width, height), min(width, height), diagonal, energy, entropy, mean_value, median_value]

# DataFrame'i Excel dosyasına yaz
df.to_excel('output.xlsx', index=False)
print("Excel dosyası başarıyla oluşturuldu.")
