import math

# 必要な署名数の計算  参考: https://www.soumu.go.jp/main_content/000451016.pdf
def calc_signatures(voters:int):  

  # 有権者が80万人以上の場合
  if voters >= 800000:
    signatures = ((voters - 800000) / 8) + 200000

  # 有権者数が40万人以上の場合
  elif voters >= 400000:
    signatures = ((voters - 400000) / 6) + (400000 / 3)

  # 有権者数が40万人未満の場合
  else:
    signatures = (voters / 3)

  # 小数点切り上げ
  signatures = math.ceil(signatures)

  return signatures


# 単体でも使えるようにする
if __name__ == "__main__":
  voters = int(input("有権者数を入力してください。"))
  signatures = calc_signatures(voters)
  print(f"必要な署名は{signatures:,}筆です。")