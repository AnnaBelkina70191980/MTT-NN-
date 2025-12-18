
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QListWidget,QLabel
from recommender.hybrid_recommender import HybridRecommender
class RecommendationsWindow(QWidget):
    def __init__(self,user_id):
        super().__init__()
        self.setWindowTitle("Рекомендации")
        l=QVBoxLayout()
        self.list=QListWidget()
        rec=HybridRecommender("database/mettransterminal.db")
        for r in rec.get_recommendations(user_id):
            self.list.addItem(r)
        l.addWidget(QLabel("Рекомендуемые товары"))
        l.addWidget(self.list)
        self.setLayout(l)
