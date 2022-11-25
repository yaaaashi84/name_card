import os

from dotenv import load_dotenv

# .envを環境変数として読み込む
# .envが存在しない場合でもエラーにはならない
load_dotenv()

print(os.environ['SECRET'])  # 存在しなかった場合はKeyError
print(os.environ.get('SECRET'))  # 存在しなかった場合はNone