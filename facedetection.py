import cv2
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
face_cascade = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
image = cv2.imread('face_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image)
for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x+w, y+h), (8, 255, 0), 2)
plt.imshow(image, cmap="gray")
plt.title('Face Detected Image')
plt.show()

