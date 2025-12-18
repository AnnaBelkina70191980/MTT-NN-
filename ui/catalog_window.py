
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QListWidget,QLabel
import sqlite3
class CatalogWindow(QWidget):
    def __init__(self,user_id):
        super().__init__()
        self.setWindowTitle("Каталог")
        l=QVBoxLayout()
        self.list=QListWidget()
        c=sqlite3.connect("database/mettransterminal.db")
        for n,p in c.execute("SELECT name,price FROM products"):
            self.list.addItem(f"{n} — {p} руб.")
        c.close()
        l.addWidget(QLabel("Товары"))
        l.addWidget(self.list)
        self.setLayout(l)
