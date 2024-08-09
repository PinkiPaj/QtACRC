import sys
from PyQt6.QtWidgets import *
from win import secondWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.win_sec_exel_clicked = secondWindow.SecondWindowExel()
        self.win_sec_img_file_clicked = secondWindow.SecondWindowImg()

        self.btn = QPushButton('OPAL exel',self)
        self.btn.clicked.connect(self.evt_opal_exel_clicked)


        self.btn2 = QPushButton('Convert img file', self)
        self.btn2.move(0, 50)
        self.btn2.clicked.connect(self.evt_convert_img_file_clicked)

    def evt_opal_exel_clicked(self):
        self.win_sec_exel_clicked.show()

    def evt_convert_img_file_clicked(self):
        self.win_sec_img_file_clicked.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = MainWindow()#create main GUI window
    dlgMain.show()#show GUI
    sys.exit(app.exec())