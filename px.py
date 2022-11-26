from PIL import Image

def calcPx(img):
    image = Image.open(img)
    (x, y) = image.size
    multi = 100 / x
    return multi

# この結果をyにかければOK
