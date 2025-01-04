from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout,
    QHBoxLayout, QPushButton
)

# Ініціалізація PyQt додатку
app = QApplication([])
menu_win = QWidget()
menu_win.setWindowTitle("Інтерфейс Запитань")

# Labels
lb_quest = QLabel("Введіть запитання:")
lb_right_ans = QLabel("Введіть вірну відповідь:")
lb_wrong_1 = QLabel("Введіть першу хибну відповідь:")
lb_wrong_2 = QLabel("Введіть другу хибну відповідь:")
lb_wrong_3 = QLabel("Введіть третю хибну відповідь:")

# LineEdits
le_quest = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_1 = QLineEdit()
le_wrong_2 = QLineEdit()
le_wrong_3 = QLineEdit()

# Buttons
bt_add = QPushButton("Додати запитання")
bt_clear = QPushButton("Очистити")
bt_back = QPushButton("Назад")
bt_back.setFixedSize(450, 40)

# Statistics Section
lb_header_stat = QLabel("Статистика")
lb_header_stat.setStyleSheet("font-size: 20px; font-weight: bold;")
lb_statistic = QLabel("Разів відповіли: 0\nВірних відповідей: 0\nУспішність: 0%")

# Layout for Labels and LineEdits
vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_1)
vl_labels.addWidget(lb_wrong_2)
vl_labels.addWidget(lb_wrong_3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_quest)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_1)
vl_lineEdits.addWidget(le_wrong_2)
vl_lineEdits.addWidget(le_wrong_3)

hl_input = QHBoxLayout()
hl_input.addLayout(vl_labels)
hl_input.addLayout(vl_lineEdits)

# Buttons Layout
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(bt_add)
hl_buttons.addWidget(bt_clear)

# Back Button Layout
hl_back = QHBoxLayout()
hl_back.addStretch()
hl_back.addWidget(bt_back, alignment=Qt.AlignCenter)
hl_back.addStretch()

# Statistics Layout
vl_stats = QVBoxLayout()
vl_stats.addWidget(lb_header_stat)
vl_stats.addWidget(lb_statistic)

# Main Layout
main_layout = QVBoxLayout()
main_layout.addLayout(hl_input)
main_layout.addLayout(hl_buttons)
main_layout.addLayout(vl_stats)
main_layout.addLayout(hl_back)

# Functions

def menu_generation(correct_answers, total_questions):
    """
    Функція підраховує статистику, ховає головний екран і показує меню.
    """
    if total_questions > 0:
        percent_correct = (correct_answers / total_questions) * 100
    else:
        percent_correct = 0

    wrong_answers = total_questions - correct_answers

    lb_statistic.setText(
        f"Разів відповіли: {total_questions}\n"
        f"Вірних відповідей: {correct_answers}\n"
        f"Успішність: {percent_correct:.2f}%"
    )

    print("Ховаємо головний екран...")
    print("Показуємо вікно меню...")

# Function to handle "Back to Menu"
def back_menu():
    """
    Функція обробляє натискання кнопки для повернення до головного екрану.
    """
    print("Ховаємо меню...")
    print("Показуємо головний екран...")

# Function to clear QLineEdit fields
def clear_lines(line_edits):
    """
    Функція очищає значення всіх QLineEdit.
    """
    for line_edit in line_edits:
        if isinstance(line_edit, QLineEdit):
            line_edit.clear()

# Connect "Очистити" button
bt_clear.clicked.connect(lambda: clear_lines([le_quest, le_right_ans, le_wrong_1, le_wrong_2, le_wrong_3]))

# Function to handle "Назад" button
def back_button_clicked():
    """
    Обробляє натискання кнопки "Назад".
    """
    print("Повернення до головного екрану...")
    menu_win.close()

bt_back.clicked.connect(back_button_clicked)

# Example: Connect "Додати запитання" button to update statistics
def update_statistics():
    """
    Функція-обробник для кнопки "Додати запитання".
    """
    correct_answers = 8
    total_questions = 10
    menu_generation(correct_answers, total_questions)

bt_add.clicked.connect(update_statistics)

menu_win.setLayout(main_layout)
menu_win.show()
app.exec_()
