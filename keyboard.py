import cv2
import mediapipe as mp
import math
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

cv2.namedWindow('Virtual Keyboard', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Virtual Keyboard', 1600, 900)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.8, max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Keyboard layout
keys = [["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L",";"],
        ["Z","X","C","V","B","N","M",",",".","/"]]

class Button():
    def __init__(self, pos, text, size=[50,50]):
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []

x_start = 100
y_start = 250

# Create letter buttons
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        x = x_start + j * 60
        y = y_start + i * 60
        buttonList.append(Button([x, y], key))

# Space + Backspace
buttonList.append(Button([x_start + 120, y_start + 180], "Space", [300, 50]))
buttonList.append(Button([x_start + 450, y_start + 180], "Back", [120, 50]))

# Text output
final_text = ""

clicked = False
delay_counter = 0

def drawAll(img, buttonList, hovered, clicked_btn):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        color = (255,255,255)

        if button == hovered:
            color = (200,200,200)
        if button == clicked_btn:
            color = (0,255,0)

        cv2.rectangle(img, (x,y), (x+w,y+h), color, cv2.FILLED)
        cv2.rectangle(img, (x,y), (x+w,y+h), (50,50,50), 2)

        font_scale = 1.5 if button.text == "Space" else 1
        text_size = cv2.getTextSize(button.text, cv2.FONT_HERSHEY_PLAIN, font_scale, 2)[0]

        text_x = x + (w - text_size[0]) // 2
        text_y = y + (h + text_size[1]) // 2

        cv2.putText(img, button.text, (text_x, text_y),
                    cv2.FONT_HERSHEY_PLAIN, font_scale, (0,0,0), 2)

    return img

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    hovered_button = None
    clicked_button = None

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            h, w, c = img.shape
            x1 = int(handLms.landmark[8].x * w)   # index
            y1 = int(handLms.landmark[8].y * h)
            x2 = int(handLms.landmark[4].x * w)   # thumb
            y2 = int(handLms.landmark[4].y * h)

            distance = math.hypot(x2 - x1, y2 - y1)

            # Detect hover
            for button in buttonList:
                bx, by = button.pos
                bw, bh = button.size
                if bx < x1 < bx + bw and by < y1 < by + bh:
                    hovered_button = button
                    break

            # Draw fingers
            color = (255,255,255)
            if distance < 40:
                color = (0,255,0)

            cv2.circle(img, (x1,y1), 10, color, cv2.FILLED)
            cv2.circle(img, (x2,y2), 10, color, cv2.FILLED)
            cv2.line(img, (x1,y1), (x2,y2), color, 3)

            # Click logic
            if hovered_button and distance < 40 and not clicked:
                clicked_button = hovered_button

                if hovered_button.text == "Space":
                    final_text += " "
                elif hovered_button.text == "Back":
                    final_text = final_text[:-1]
                else:
                    final_text += hovered_button.text

                clicked = True
                delay_counter = 0

    # Draw keyboard
    img = drawAll(img, buttonList, hovered_button, clicked_button)

    # Draw text box
    cv2.rectangle(img, (50, 50), (1230, 150), (0,0,0), cv2.FILLED)
    cv2.rectangle(img, (50, 50), (1230, 150), (255,255,255), 2)

    cv2.putText(img, final_text, (60, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), 2)

    # Click delay
    if clicked:
        delay_counter += 1
        if delay_counter > 12:
            clicked = False

    cv2.imshow("Virtual Keyboard", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()