from PyQt5.QtWidgets import ( QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox)
from PyQt5.QtCore import Qt
from ui.catalog_window import CatalogWindow
from ui.recommendations_window import RecommendationsWindow
from ui.admin_window import AdminWindow
from ui.analytics_window import AnalyticsWindow

class MainWindow(QWidget):

    def __init__(self, user_id: int, role: str):
        super().__init__()

        self.user_id = user_id
        self.role = role

        self.catalog_window = None
        self.recommendations_window = None
        self.admin_window = None
        self.analytics_window = None

        self.setWindowTitle("Рекомендательная система металлопроката")
        self.setFixedSize(400, 300)

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()

        title_label = QLabel("Главное меню")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        layout.addWidget(title_label)

        # Кнопка каталога
        self.catalog_button = QPushButton("Каталог металлопроката")
        self.catalog_button.clicked.connect(self.open_catalog)
        layout.addWidget(self.catalog_button)

        # Кнопка рекомендаций
        self.recommendations_button = QPushButton("Рекомендации")
        self.recommendations_button.clicked.connect(self.open_recommendations)
        layout.addWidget(self.recommendations_button)

        # Кнопка аналитики
        self.analytics_button = QPushButton("Аналитика")
        self.analytics_button.clicked.connect(self.open_analytics)
        layout.addWidget(self.analytics_button)

        # Кнопка администрирования (только для admin)
        if self.role == "admin":
            self.admin_button = QPushButton("Администрирование")
            self.admin_button.clicked.connect(self.open_admin)
            layout.addWidget(self.admin_button)

        self.setLayout(layout)


    def open_catalog(self):

        # Открытие окна каталога металлопроката.

        if self.catalog_window is None:
            self.catalog_window = CatalogWindow(self.user_id)
        self.catalog_window.show()
        self.catalog_window.raise_()
        self.catalog_window.activateWindow()

    def open_recommendations(self):

       # Открытие окна рекомендаций.

        if self.recommendations_window is None:
            self.recommendations_window = RecommendationsWindow(self.user_id)
        self.recommendations_window.show()
        self.recommendations_window.raise_()
        self.recommendations_window.activateWindow()

    def open_admin(self):

        # Открытие административного окна.
        # Доступно только пользователю с ролью 'admin'.

        if self.role != "admin":
            QMessageBox.warning(
                self,
                "Доступ запрещён",
                "У вас нет прав для доступа к административному разделу."
            )
            return

        if self.admin_window is None:
            self.admin_window = AdminWindow()
        self.admin_window.show()
        self.admin_window.raise_()
        self.admin_window.activateWindow()

    def open_analytics(self):

       # Открытие аналитического окна.

        if self.analytics_window is None:
            self.analytics_window = AnalyticsWindow()
        self.analytics_window.show()
        self.analytics_window.raise_()
        self.analytics_window.activateWindow()
