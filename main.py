import sys
import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw
import re
from calc import calc_signatures


# 有権者数のバリエーション (検証)
def validate_voters_number(voters:str)->bool:
  pattern = r"^\d+$" # 正規表現パターン
  if re.match(pattern, voters):
    return True
  else:
    return False

class MainWindow(Qw.QMainWindow):
  
  def __init__(self):

    super().__init__() 
    self.setWindowTitle("リコールに必要な署名数の計算") 
    self.setGeometry(100, 50, 640, 130) 

    # 上の文(lb1)
    self.lb_1 = Qw.QLabel(self)
    self.lb_1.setGeometry(15,10,300,25)
    self.lb_1.setText("有権者数が")

    # 有権者数のテキストボックス
    self.tb_voters = Qw.QLineEdit(self)
    self.tb_voters.setGeometry(15,35,100,25)
    self.tb_voters.setPlaceholderText("有権者数(人)")
    self.tb_voters.setAlignment(Qc.Qt.AlignmentFlag.AlignCenter)
    self.tb_voters.textChanged.connect(self.voters_changed)

    # 有権者数の検証ラベル vm: Validation Message
    self.lb_voters_vm = Qw.QLabel(self)
    self.lb_voters_vm.setGeometry(125,35,200,25)
    self.lb_voters_vm.setText("自然数を入力してください。")
    self.lb_voters_vm.setStyleSheet("color: red;")
    self.lb_voters_vm.setVisible(True)

    # 人の場合(lb_nin)
    self.lb_nin = Qw.QLabel(self)
    self.lb_nin.setGeometry(125,35,100,25)
    self.lb_nin.setText("")
    self.lb_nin.setVisible(True)

    # 下の文(lb2)
    self.lb_2 = Qw.QLabel(self)
    self.lb_2.setGeometry(15,65,400,25)
    self.lb_2.setText("都道府県知事・市町村長の解職請求に必要な署名数は")

    #  署名の件数の表示(lb3)
    self.lb_3 = Qw.QLabel(self)
    self.lb_3.setGeometry(15,90,500,25)
    self.lb_3.setText("")

  # 有権者数のテキストボックスが変更
  def voters_changed(self):
    voters = self.tb_voters.text()
    if len(voters) == 0:
      self.lb_voters_vm.setText("有権者数を入力してください。")
      self.lb_nin.setText("")
      self.lb_3.setText("")
      
    else:
      if validate_voters_number(voters):
        self.lb_voters_vm.setText("")
        self.lb_nin.setText("人の場合")
        signatures = calc_signatures(int(voters))
        self.lb_3.setText(f"{signatures:,}筆です。")
      else:
        self.lb_voters_vm.setText("自然数を入力してください。")
        self.lb_nin.setText("")
        self.lb_3.setText("")


# 本体
if __name__ == "__main__":
  app = Qw.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())