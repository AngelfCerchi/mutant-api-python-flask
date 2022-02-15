from models.xmen import Xmen
from utils.db import db

class MagnetoRepository:
    def __init__(self):
        pass

    def guardarDnaDb(self,dna,mutante):
        
        try:
            if mutante:
                xm = Xmen(dna,mutante)
                db.session.add(xm)
                db.session.commit()
                # print('Mutante Guardado')
                return dna , mutante , None
            else:
                xm = Xmen(dna,mutante)
                db.session.add(xm)
                db.session.commit()
                # print('Humano guardado')
                return dna,mutante , None
        except Exception as e:
            return None,None, e

    def stats(self):
        try:
            mutant = Xmen.query.filter_by(isMutant=1).all()
            human = Xmen.query.filter_by(isMutant=0).all()
            return mutant , human , None
        except Exception as e:
            return None, None ,e