from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QPushButton, QApplication, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('В каком году родился?', '2007', '2001', '2003', '1993'))
question_list.append(Question('Какого цвета нет на флаге России?', 'желтый', 'белый', 'красный', 'синий'))
question_list.append(Question('ДА?', '...', '...', '...', '...'))
question_list.append(Question('НЕТ?', '***', '***', '***', '***'))
question_list.append(Question('Зимой и летом одним цветом?', 'мышь', 'дверь', 'ёлка', 'зима'))
question_list.append(Question('Какой национальности не существует?', 'чулымцы', 'энцы', 'аулеты', 'смурфы'))


#создание приложения и главного окна
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Memory Card')
my_win.resize(400, 200)

#создание виджетов главного окна
v_line = QVBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

quest = QLabel('Какой национальности не существует?')
h_line = QHBoxLayout()
h_line.addWidget(quest, alignment = Qt.AlignCenter)
v_line.addLayout(h_line)

group = QGroupBox('Варианты ответов')
h_line2 = QHBoxLayout()
h_line2.addWidget(group, alignment = Qt.AlignCenter)
v_line.addLayout(h_line2)

otvet = QPushButton('Ответить')
h_line1 = QHBoxLayout()
h_line1.addWidget(otvet, alignment = Qt.AlignCenter)
v_line.addLayout(h_line1)

#---------------------------------
an1 = QRadioButton("Энцы")
an2 = QRadioButton('Чулымцы')
an3 = QRadioButton('Смурфы')
an4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(an1)
RadioGroup.addButton(an2)
RadioGroup.addButton(an3)
RadioGroup.addButton(an4)

h_line3 = QHBoxLayout()
v_line4 = QVBoxLayout()
v_line5 = QVBoxLayout()

v_line4.addWidget(an2, alignment = Qt.AlignCenter)
v_line4.addWidget(an1, alignment = Qt.AlignCenter)
v_line5.addWidget(an3, alignment = Qt.AlignCenter)
v_line5.addWidget(an4, alignment = Qt.AlignCenter)
#---------------------------------

h_line3.addLayout(v_line4)
h_line3.addLayout(v_line5)

group.setLayout(h_line3)
# 2 часть - форма ответа
answer_vertical_line = QVBoxLayout()
answer_horizontal_line = QHBoxLayout()

answer_group = QGroupBox('Результат теста')
answer2 = QLabel('Правильно/Неправильно')
answer1 = QLabel('Правильный ответ')

answer_vertical_line.addWidget(answer2)
answer_vertical_line.addWidget(answer1, alignment = Qt.AlignCenter)
answer_group.setLayout(answer_vertical_line)
h_line2.addWidget(answer_group, alignment = Qt.AlignCenter)
answer_group.hide()
# 2 часть - конец

#---------------------------------
def show_result(): 
    group.hide()
    answer_group.show()
    otvet.setText("Следующий вопрос")

def show_question():
    answer_group.hide()
    group.show()
    otvet.setText("Ответить")
    RadioGroup.setExclusive(False)
    an1.setChecked(False)
    an2.setChecked(False)
    an3.setChecked(False)
    an4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [an1, an2, an3, an4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    quest.setText(q.question)
    answer1.setText(q.right_answer)
    show_question()

def check_answer():
    if answer[0].isChecked():
        answer2.setText("Правильно!")
        show_result()
        my_win.score += 1
        print("\nСтатистика", "\n--Всего вопросов:", my_win.total, '\n--Правильных ответов:', my_win.score, "\nРейтинг:", my_win.score / my_win.total * 100, '%')
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        answer2.setText("Неправильно!")
        show_result()
        print("\nСтатистика", "\n--Всего вопросов:", my_win.total, '\n--Правильных ответов:', my_win.score, "\nРейтинг:", my_win.score / my_win.total * 100, '%')

def next_question():
    my_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def Click_OK():
    if otvet.text() == 'Ответить':
        check_answer()
    else:
        next_question()
#---------------------------------

my_win.setLayout(v_line)

q = Question('Государственный язык Бразилии', '.', '.', '.', '.')
ask(q)
my_win.score = 0
my_win.total = 0
otvet.clicked.connect(Click_OK)
next_question()

#отображение окна приложения 
my_win.show()
app.exec_()