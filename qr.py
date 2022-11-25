import qrcode
from PIL import Image


# このQRを読み取るとIDからその人の名刺を取得できるようにする
# IDをつなげるようにやり方調べる

qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,
    border=8


# qr.add_data('リンクの部分')
# qr_img = qrcode.make('QR作成')
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("data/qr/my_qr.png")