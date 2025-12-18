
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QListWidget,QLabel
import sqlite3
class AnalyticsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Аналитика")
        l=QVBoxLayout()
        self.list=QListWidget()
        c=sqlite3.connect("database/mettransterminal.db")
        for n,a in c.execute("SELECT p.name, AVG(r.rating) FROM ratings r JOIN products p ON p.id=r.product_id GROUP BY p.id"):
            self.list.addItem(f"{n}: {round(a,2)}")
        c.close()
        l.addWidget(QLabel("Средние оценки"))
        l.addWidget(self.list)
        self.setLayout(l)
