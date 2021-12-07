import imutils
import cv2

# Height(Rows) and Widht (Columns)

image = cv2.imread("room1.jpeg")
(h, w, d) = image.shape
print(f"Width={w}, height={h}, depth={d}")

(B, G, R) = image[100, 50]
print(f"R={R}, G={G}, B={B}")

cv2.imshow("image", image)
cv2.waitKey(0)
