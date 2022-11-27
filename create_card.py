import os 
import sys
import cv2
from database import User
from PIL import Image

def create_card(me):

    cur_dir = os.path.dirname(sys.argv[0])
    file_path = os.path.join(cur_dir, 'static/card_background/card_background1.jpeg')  # 背景選択
    img = cv2.imread(file_path)

    cv2.putText(
        img,
        text=me.name,
        org=(10, 340),
        fontFace=cv2.FONT_HERSHEY_TRIPLEX,
        fontScale=3,  # フォントサイズ
        color=(0, 0, 0),  # 色決める
        thickness=2
    )

    cv2.putText(
        img,
        text=me.belong,
        org=(10, 50), # 左上を調べる
        fontFace=cv2.FONT_HERSHEY_TRIPLEX,
        fontScale=1.5,  # フォントサイズ
        color=(0, 0, 0),  # 色決める
        thickness=2
    )

    cv2.putText(
        img,
        text=me.position,
        org=(10, 120), # nameの下を位置を調べる
        fontFace=cv2.FONT_HERSHEY_TRIPLEX,
        fontScale=1.2,  # フォントサイズ
        color=(0, 0, 0),  # 色決める
        thickness=1
    )

    cv2.putText(
        img,
        text=me.tel,
        org=(10,580), # centerを調べる
        fontFace=cv2.FONT_HERSHEY_TRIPLEX,
        fontScale=1.2,  # フォントサイズ
        color=(0, 0, 0),  # 色決める
        thickness=1
    )

    cv2.putText(
        img,
        text=me.email,
        org=(10,630), # telの下の位置を調べる
        fontFace=cv2.FONT_HERSHEY_TRIPLEX,
        fontScale=1.2,  # フォントサイズ
        color=(0, 0, 0),  # 色決める
        thickness=1
    )

    # cv2.putIcon(
    #     img,
    #     file=icon,
    #     org=(680, 10) # centerを調べる
    #     # thickness=3
    # )

    cv2.imwrite("static/name_card/" + me.create_id + ".png", img)
    # cv2.waitKey(10000)

def resize(me):
    file_path = "static/icon/" + me.create_id + ".png"
    im = cv2.imread(file_path)
    w, h, ch = im.shape

    scale_ratio = 200 / w
    resized_im = cv2.resize(im, dsize=(round(h * scale_ratio), 200))

    output_file = "static/icon_resize/resize_" + me.create_id + ".png"
    cv2.imwrite(output_file, resized_im)


def paste(me):
    img_path = "static/name_card/" + me.create_id + ".png"
    pic_path = "static/icon_resize/resize_" + me.create_id + ".png"
    output_path = "static/pic_name_card/picname_" + me.create_id + ".png"

    img = cv2.imread(img_path)
    pic = cv2.imread(pic_path)

    print(img.shape)
    print(pic.shape)

    # img.paste(pic, (0, 0), pic.split()[3])
    img[20:200 + 20, 800:150 + 800] = pic

    cv2.imwrite(output_path, img)
     # waitKey(0)で画像上で何かしらのキーを押せば閉じられるようにする
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # img.save(output_path)