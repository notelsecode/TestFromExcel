import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pandas as pd
from main_window_design import Ui_MainWindow

PREVIOUS = "previous"  # ключ предыдущего вопроса
NEXT = "next"  # ключ следующего вопроса


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.result = 0  # текущий результат
        self.count = 0  # текущее количество заданий, определяется после парсинга файла
        self.questions = list()
        self.current_question = 0
        self.answers = list()

        # соединение сигналов со слотами
        self.open_test_action.triggered.connect(self.open_file)
        self.statusbar.messageChanged.connect(lambda args: self.status_changed(args))
        self.finish_test_button.clicked.connect(self.finish_test)
        self.previous_question_button.clicked.connect(lambda: self.show_question(key=PREVIOUS))
        self.next_question_button.clicked.connect(lambda: self.show_question(key=NEXT))
        self.answer_line_edit.returnPressed.connect(self.check_answer)

    def check_answer(self):
        if self.answer_line_edit.text() == self.questions[self.current_question][1]:
            self.result += 1
            self.result = min(self.result, self.count)
        self.answers[self.current_question] = self.answer_line_edit.text()
        if self.current_question != self.count - 1:
            self.statusBar().showMessage("Ответ сохранён.", 5000)
        elif all(self.answers):
            self.statusBar().showMessage("Ответ сохранён. Вы ответили на все вопросы можете завершить тест.", 5000)
        else:
            self.statusBar().showMessage(
                "Ответ сохранён. Вы ответили на последний вопрос, но у вас остались вопросы без ответа.", 5000)
        self.statusBar().setStyleSheet("background-color: green")

    def show_question(self, key=None):
        if key == PREVIOUS and self.current_question != 0:
            self.current_question -= 1
        elif key == NEXT and self.current_question != self.count - 1:
            self.check_answer()
            self.current_question += 1
        if self.current_question == 0:
            self.previous_question_button.setEnabled(False)
        else:
            self.previous_question_button.setEnabled(True)
        if self.current_question == self.count - 1:
            self.next_question_button.setEnabled(False)
        else:
            self.next_question_button.setEnabled(True)
        self.question_label.setText(self.questions[self.current_question][0])
        self.answer_line_edit.setText(self.answers[self.current_question])
        self.statusBar().setStyleSheet("background-color: #EFEFEF")
        self.statusBar().showMessage("")

    def finish_test(self):
        self.check_answer()
        sep = '\n'
        no_answer = "Нет ответа"
        self.question_label.setText(
            f"Тест окончен, ваш результат: {self.result} из {self.count}\n"
            f"Ваши ответы - правильные ответы:\n"
            f"{sep.join(f'{self.answers[current] if self.answers[current] else no_answer} - {self.questions[current][1]}' for current in range(self.count))}")
        self.previous_question_button.setEnabled(False)
        self.next_question_button.setEnabled(False)
        self.finish_test_button.setEnabled(False)
        self.answer_line_edit.clear()
        self.answer_line_edit.setEnabled(False)

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
        self.result = 0
        self.count = 0
        self.questions = list()
        self.current_question = 0
        self.answers = list()
        self.question_label.setEnabled(True)
        self.previous_question_button.setEnabled(True)
        self.next_question_button.setEnabled(True)
        self.finish_test_button.setEnabled(True)
        self.answer_line_edit.setEnabled(True)

    def parse_file(self, path):
        xl = pd.ExcelFile(path)
        df1 = xl.parse(xl.sheet_names[0])
        self.questions = [list(row) for row in df1.values]
        self.count = len(self.questions)
        self.answers = ["" for _ in range(self.count)]
        self.show_question()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
