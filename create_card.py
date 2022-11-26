import os 
import sys
import cv2
from app import User

cur_dir = os.path.dirname(sys.argv[0])
file_path = os.path.join(cur_dir, 'data/card_background/card_background1.jpeg')  # 背景選択

img = cv2.imread(file_path)

cv2.putName(
    img,
    text=name,
    org=(,) # centerを調べる
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=18,  # フォントサイズ
    color=()  # 色決める
    thickness=3
)

cv2.putBelong(
    img,
    text=belong,
    org=(,) # 左上を調べる
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=14,  # フォントサイズ
    color=()  # 色決める
    thickness=3
)

cv2.putPosition(
    img,
    text=position,
    org=(,) # nameの下を位置を調べる
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=10,  # フォントサイズ
    color=()  # 色決める
    thickness=3
)

cv2.putTel(
    img,
    text=name,
    org=(,) # centerを調べる
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=8,  # フォントサイズ
    color=()  # 色決める
    thickness=3
)

cv2.puMail(
    img,
    text=mail,
    org=(,) # telの下の位置を調べる
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=18,  # フォントサイズ
    color=()  # 色決める
    thickness=3
)

cv2.putIcon(
    img,
    text=icon,
    org=(,) # centerを調べる
    thickness=3
)