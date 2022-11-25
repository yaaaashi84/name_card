from PIL import Imgae
import cv2
import matplotlib.pyplot as platform
import matplotlib

# 先にリサイズする
# これ実行できなかった
# ここをその人の写真を指定できるようにする(pic.pyにてIDを指定できるように？)
img_path = "data/temp/pic_0.jpg"


img = Image.open(img_path)
resized_frame = frame.resize((img.width // 2, img.height // 2))
resized_frame_lanczos.save('data/resized/resized_pic.jpg')







# matplotlib inline
matplotlib.rcParams['image.cmap'] = 'gray'