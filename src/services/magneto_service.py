from src.repository.magneto_repository import MagnetoRepository

class MagnetoService:
    def __init__(self):
        pass

    def esLetraDeBaseNitrogenada(self,letra):
        if not letra in ['A','T','C','G']:
            raise Exception("No es base Nitrogenada")

    def secuenciasEnFila(self,dna):
        contadorSecuencias = 0
        for posF in range(len(dna)):
            anterior = ''
            contadorLetras = 0
            for posC in range(len(dna[0])):
                self.esLetraDeBaseNitrogenada(dna[posF][posC])
                if dna[posF][posC] == anterior:
                    contadorLetras+= 1
                elif contadorLetras >= 3:
                    contadorSecuencias+= 1
                    contadorLetras = 0
                    anterior = dna[posF][posC]
                else:
                    contadorLetras = 0
                    anterior = dna[posF][posC]
            if contadorLetras >= 3:
                contadorSecuencias+= 1
        return contadorSecuencias

    def sencuenciasEnColumna(self,dna):
        contadorSecuencias = 0
        for posC in range(len(dna[0])):
            anterior = ''
            contadorLetras = 0
            for posF in range(len(dna)):
                self.esLetraDeBaseNitrogenada(dna[posF][posC])
                if dna[posF][posC] == anterior:
                    contadorLetras+= 1
                elif contadorLetras >= 3:
                    contadorSecuencias+= 1
                    contadorLetras = 0
                    anterior = dna[posF][posC]
                else:
                    contadorLetras = 0
                    anterior = dna[posF][posC]
            if contadorLetras >= 3:
                contadorSecuencias+= 1
        return contadorSecuencias       

    def secuenciasEnOblicuo(self,dna):
        contadorSecuencias = 0
        contadorLetras = 0
        anterior = ''
        for posF in range(len(dna)):
            self.esLetraDeBaseNitrogenada(dna[posF][posF])
            if dna[posF][posF] == anterior:
                contadorLetras+= 1
            elif contadorLetras  >= 3:
                contadorSecuencias+= 1
                contadorLetras = 0
                anterior = dna[posF][posF]
            else:
                contadorLetras = 0
                anterior = dna[posF][posF]
        if contadorLetras >= 3:
            contadorSecuencias+= 1
        return contadorSecuencias       
    
    def secuenciasEnOblicuoInverso(self,dna):
        contadorSecuencias = 0
        contadorLetras = 0
        anterior = ''
        posC = len(dna)-1
        for posF in range(len(dna)):
            self.esLetraDeBaseNitrogenada(dna[posF][posC])
            if dna[posF][posC] == anterior:
                contadorLetras+= 1
            elif contadorLetras >= 3:
                contadorSecuencias+= 1
                contadorLetras = 0
                anterior = dna[posF][posC]
            else:
                contadorLetras = 0
                anterior = dna[posF][posC]
            posC-=1
        if contadorLetras >= 3:
            contadorSecuencias+= 1      
        return contadorSecuencias          

    def isMutant(self,dna):
        return self.secuenciasEnFila(dna) + self.sencuenciasEnColumna(dna) + self.secuenciasEnOblicuo(dna)+self.secuenciasEnOblicuoInverso(dna) > 1

    def guardarDna(self,dna):
        mutante = self.isMutant(dna)
        mr = MagnetoRepository()
        dnaj , mutante, e = mr.guardarDnaDb(str(dna),mutante)
        return dnaj,mutante, e

    def stats(self):
        mr = MagnetoRepository()
        cant_mutant , cant_human , error = mr.stats()
        try:
            if len(cant_human) == 0:
                ratio = len(cant_mutant)/1
                return len(cant_mutant), len(cant_human), ratio,error
            else:
                ratio = len(cant_mutant) / len(cant_human)
                return len(cant_mutant), len(cant_human), ratio, error
        except Exception as e:
            return None, None, None ,e


            



