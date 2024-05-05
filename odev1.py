import cv2
import numpy as np
import matplotlib.pyplot as plt

# Sigmoid fonksiyonu
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Standart S-Curve metodu
def standard_s_curve(image):
    # Görüntüyü 0 ile 1 arasında normalize et
    normalized_image = image.astype(float) / 255.0
    # Sigmoid fonksiyonunu uygula
    transformed_image = sigmoid((normalized_image - 0.5) * 10)
    # 0-255 arasında yeniden ölçekle
    transformed_image = (transformed_image * 255).astype(np.uint8)
    return transformed_image

# Yatay kaydırılmış S-Curve metodu
def shifted_s_curve(image, shift_amount):
    normalized_image = image.astype(float) / 255.0
    transformed_image = sigmoid((normalized_image - 0.5 + shift_amount) * 10)
    transformed_image = (transformed_image * 255).astype(np.uint8)
    return transformed_image

# Eğimli S-Curve metodu
def sloped_s_curve(image, slope):
    normalized_image = image.astype(float) / 255.0
    transformed_image = sigmoid((normalized_image - 0.5) * slope)
    transformed_image = (transformed_image * 255).astype(np.uint8)
    return transformed_image


# Özgün kontrast artırma fonksiyonu
def custom_contrast_enhancement(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    # Yüzey düzeltme (CLAHE) filtresi ile histogram eşitleme
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    enhanced_image = clahe.apply(image)
    return enhanced_image

# Görüntüyü yükle ve gri tonlamalıya çevir
image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
first =cv2.imread("image.jpg")
# Standart S-Curve uygula
standard_result = standard_s_curve(image)

# Yatay kaydırılmış S-Curve uygula
shifted_result = shifted_s_curve(image, 0.2)

# Eğimli S-Curve uygula
sloped_result = sloped_s_curve(image, 20)


# Kontrast artırma işlemi uygula
enhanced_result = custom_contrast_enhancement(image)

# Sonuçları görselleştir
plt.figure(figsize=(16, 12))

plt.subplot(3, 3, 1)
plt.imshow(first, cmap='gray')
plt.title('Orjinal Görüntü')

plt.subplot(3, 3, 2)
plt.imshow(standard_result, cmap='gray')
plt.title('Standart S-Curve')

plt.subplot(3, 3, 3)
plt.imshow(shifted_result, cmap='gray')
plt.title('Yatay Kaydırılmış S-Curve')

plt.subplot(3, 3, 4)
plt.imshow(sloped_result, cmap='gray')
plt.title('Eğimli S-Curve')


plt.subplot(3, 3, 6)
plt.imshow(enhanced_result, cmap='gray')
plt.title('Özel Kontrast Artırma')

plt.show()
