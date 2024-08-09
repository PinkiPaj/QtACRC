from PyQt6.QtWidgets import *
from scripts import correct_image_file


class SecondWindowImg(QWidget):
    res_operation = False

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.x = QLineEdit()
        self.x.setText("Width")
        self.x.move(0, 510)
        layout.addWidget(self.x)

        self.y = QLineEdit()
        self.x.move(0, 50)
        self.y.setText("Height")
        layout.addWidget(self.y)

        self.btn3 = QPushButton('Selekt folder', self)
        self.btn3.clicked.connect(self.evt_convert_clicked)
        layout.addWidget(self.btn3)

        self.setLayout(layout)

    def evt_convert_clicked(self):
        try:
            int(self.y.text()) / 1
            int(self.x.text()) / 1
            res = QFileDialog.getExistingDirectory(self, 'Open File', 'C:/')
            res_operation = correct_image_file.main(int(self.x.text()), int(self.y.text()), res)
            if res_operation == True:
                self.destroy()
        except Exception as err:
            print(err)


from PyQt6.QtWidgets import *
from scripts import text_to_exel


class SecondWindowExel(QWidget):
    res_operation = False

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLineEdit()
        self.label.setText("Text")
        layout.addWidget(self.label)

        self.btn3 = QPushButton('Convert', self)
        self.btn3.clicked.connect(self.evt_convert_clicked)
        layout.addWidget(self.btn3)

        self.setLayout(layout)

    def evt_convert_clicked(self):
        res_operation = text_to_exel.main(self.label.text())
        if res_operation == True:
            self.destroy()
