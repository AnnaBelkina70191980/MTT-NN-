from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from ui.main_window import MainWindow

# Локальные пользователи (без базы данных). Лучше было бы использовать SQL файл, но  в учебной версии pycharm нет возможности это сделать
USERS = {
    "admin": {"password": "admin123", "role": "admin", "id": 1},
    "user1": {"password": "user123", "role": "user", "id": 2},
    "user2": {"password": "user123", "role": "user", "id": 3},
}


class LoginWindow(QWidget):
    #Класс окна авторизации пользователя

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Авторизация пользователя")
        self.setFixedSize(350, 220)

        self.init_ui()

    def init_ui(self):
        #Формирование окна авторизации
        layout = QVBoxLayout()

        title_label = QLabel("Вход в систему")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Логин пользователя")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.authenticate_user)

        layout.addWidget(title_label)
        layout.addWidget(QLabel("Логин:"))
        layout.addWidget(self.login_input)
        layout.addWidget(QLabel("Пароль:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def authenticate_user(self):
        #Проверка логина и пароля пользователя.

        username = self.login_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(
                self,
                "Ошибка авторизации",
                "Введите логин и пароль."
            )
            return

        user = USERS.get(username)
        if user and user["password"] == password:
            self.open_main_window(user["id"], user["role"])
        else:
            QMessageBox.warning(
                self,
                "Ошибка авторизации",
                "Неверный логин или пароль."
            )

    def open_main_window(self, user_id: int, role: str):
        #Открытие главного окна после успешной авторизациии
        self.main_window = MainWindow(user_id, role)
        self.main_window.show()
        self.close()
