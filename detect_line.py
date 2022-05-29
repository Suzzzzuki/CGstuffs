import cv2
import os
import numpy as np

img = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/coin_illust.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


edges = cv2.Canny(img, 150, 300, L2gradient=True)


lines = cv2.HoughLines(edges, 0.777, 2.35 / 180, 112)


def draw_line(img, theta, rho):
    h, w = img.shape[:2]
    if np.isclose(np.sin(theta), 0):
        x1, y1 = rho, 0
        x2, y2 = rho, h
    else:
        calc_y = lambda x: rho / np.sin(theta) - x * np.cos(theta) / np.sin(theta)
        x1, y1 = 0, calc_y(0)
        x2, y2 = w, calc_y(w)

    x1, y1, x2, y2 = list(map(int, [x1, y1, x2, y2]))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


for rho, theta in lines.squeeze(axis=1):
    draw_line(img, theta, rho)





cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
