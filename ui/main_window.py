
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton
from ui.catalog_window import CatalogWindow
from ui.recommendations_window import RecommendationsWindow
from ui.admin_window import AdminWindow
from ui.analytics_window import AnalyticsWindow
class MainWindow(QWidget):
    def __init__(self,user_id,username):
        super().__init__()
        self.setWindowTitle("Главное меню")
        l=QVBoxLayout()
        l.addWidget(QLabel(f"Добро пожаловать, {username}"))
        b1=QPushButton("Каталог")
        b2=QPushButton("Рекомендации")
        b3=QPushButton("Администрирование")
        b4=QPushButton("Аналитика")
        b1.clicked.connect(lambda: CatalogWindow(user_id).show())
        b2.clicked.connect(lambda: RecommendationsWindow(user_id).show())
        b3.clicked.connect(lambda: AdminWindow().show())
        b4.clicked.connect(lambda: AnalyticsWindow().show())
        for b in (b1,b2,b3,b4): l.addWidget(b)
        self.setLayout(l)
