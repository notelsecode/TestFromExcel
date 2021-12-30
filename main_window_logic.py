import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from main_window_design import Ui_MainWindow

PREVIOUS = "previous"  # ключ предыдущего вопроса
NEXT = "next"  # ключ следующего вопроса


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.result = 0  # текущий результат
        self.count = 0  # текущее количество заданий, определяется после парсинга файла

        # соединение сигналов со слотами
        self.open_test_action.triggered.connect(self.open_file)
        self.statusbar.messageChanged.connect(lambda args: self.status_changed(args))
        self.finish_test_button.clicked.connect(self.finish_test)
        self.previous_question_button.clicked.connect(lambda: self.show_question(key=PREVIOUS))
        self.next_question_button.clicked.connect(lambda: self.show_question(key=NEXT))

    def show_question(self, key):
        # логгирование
        print("clicked", self.sender().text(), f"with key {key}")

    def finish_test(self):
        self.question_label.setText(f"Тест окончен, ваш результат: {self.result} из {self.count}")

    def status_changed(self, args):
        if not args:
            self.statusBar().setStyleSheet("background-color: #EFEFEF")

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "выбрать тест",
            "",
            "Excel файл (*.xlsx *.xls)",
        )[0]
        if file_name:
            self.enable()
            self.parse_file(file_name)
            self.statusBar().showMessage("Файл выбран.", 5000)
            self.statusBar().setStyleSheet("background-color: green")
        else:
            self.statusBar().showMessage("Не выбран файл.", 5000)
            self.statusBar().setStyleSheet("background-color: red")

    def enable(self):
        self.question_label.setEnabled(True)
        self.previous_question_button.setEnabled(True)
        self.next_question_button.setEnabled(True)
        self.finish_test_button.setEnabled(True)
        self.answer_line_edit.setEnabled(True)

    def parse_file(self, path):
        # TODO: добавить парсинг Excel файла
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
