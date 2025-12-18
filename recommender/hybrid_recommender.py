
import sqlite3, math
from collections import defaultdict
class HybridRecommender:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
    def cosine(self,a,b):
        d=sum(x*y for x,y in zip(a,b))
        na=math.sqrt(sum(x*x for x in a))
        nb=math.sqrt(sum(y*y for y in b))
        return d/(na*nb) if na and nb else 0
    def get_recommendations(self,user_id):
        cur=self.conn.cursor()
        users=[u[0] for u in cur.execute("SELECT DISTINCT user_id FROM ratings")]
        products=[p[0] for p in cur.execute("SELECT id FROM products")]
        ratings=defaultdict(lambda:{p:0 for p in products})
        for u,p,r in cur.execute("SELECT user_id,product_id,rating FROM ratings"):
            ratings[u][p]=r
        target=list(ratings[user_id].values())
        scores=defaultdict(float)
        for u in users:
            if u==user_id: continue
            sim=self.cosine(target,list(ratings[u].values()))
            for p,r in ratings[u].items():
                scores[p]+=sim*r
        return [cur.execute("SELECT name FROM products WHERE id=?",(p,)).fetchone()[0]
                for p,_ in sorted(scores.items(),key=lambda x:x[1],reverse=True)]
