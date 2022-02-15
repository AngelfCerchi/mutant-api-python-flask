from utils.db import db

class Xmen(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    dna = db.Column(db.String(100), unique=True )
    isMutant = db.Column(db.Boolean)

    def __init__(self, dna,isMutant):
        self.dna = dna
        self.isMutant = isMutant