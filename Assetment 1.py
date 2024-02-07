import cv2
import numpy as np

selected_contour = None
selected_contour_area = 0

def click_event(event, x, y, flags, param):
    global selected_contour, selected_contour_area, contours
    if event == cv2.EVENT_LBUTTONDOWN:
        for contour in contours:
            if cv2.pointPolygonTest(contour, (x, y), False) >= 0:
                selected_contour = contour
                selected_contour_area = cv2.contourArea(contour)
                x_rect, y_rect, width, height = cv2.boundingRect(contour)
                print("Selected object dimensions (Width x Height):", width, "x", height)
                break
        
        if selected_contour is not None:
            print("Selected object size:", selected_contour_area)

image = cv2.imread('D:/Prabu developement/python open cv/RECT.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 30, 200)

contours, _ = cv2.findContours(edged.copy(),
                               cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_NONE)

print("Number of Contours found =", len(contours))

cv2.imshow('Original Image', image)

cv2.setMouseCallback('Original Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
