import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi yükle
image_path = 'brown-eyes.jpeg'
image = cv2.imread(image_path)

# Hata kontrolü
if image is None:
    print("Error: Image not found or cannot be read.")
    exit()

# Göz tespiti için bir Cascade Classifier kullanarak gözleri tespit et
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Gözleri işaretle
for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Gözün içerisinde gözbebeği tespiti yap
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    circles = cv2.HoughCircles(roi_gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=5, maxRadius=20)

    # Gözbebeğini işaretle
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x_eye, y_eye, r_eye) in circles:
            cv2.circle(roi_color, (x_eye, y_eye), r_eye, (255, 0, 255), 2)

# OpenCV'nin görüntü formatından matplotlib'in formatına dönüştürme
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Görüntüyü göster
plt.imshow(image_rgb)
plt.axis('off')  # Eksenleri kapat
plt.show()





