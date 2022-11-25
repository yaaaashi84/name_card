import sys
from PIL import Image
import pyocr
import pyocr.builders

# これは会社名や名前を読み取る操作が時間かかりそうだからやめる



tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# 推奨している順で読み込むので、配列の最初に推奨順の1つ目がはいる
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# 例: Will use tool 'Tesseract (sh)'

txt = tool.image_to_string(
    Image.open('images/sparta_camp_eng.png'),  # OCRする画像
    lang='eng',  # 学習済み言語データ
    builder=pyocr.builders.TextBuilder()  # 期待される出力のタイプを指定
)

# print(txt)

with open('text.txt', mode="w") as f:
    f.writelines(txt)