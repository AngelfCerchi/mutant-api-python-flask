from flask import Blueprint, request , Response
from src.services.magneto_service import MagnetoService

magnetoservice = Blueprint('magnetoservice', __name__)

@magnetoservice.route('/mutant/', methods=['POST'])
def verificar_mutante():
    dna = request.json.get('dna')
    magneto_service = MagnetoService()
    mutante = magneto_service.isMutant(dna)
    try:
        if mutante:
            return Response(status=200)
        return Response(status=403)
    except Exception as e:
        return print(str(e))

@magnetoservice.route('/save', methods=['POST'])
def guardarDna():
    dna = request.json.get('dna')
    ms = MagnetoService()
    dnaj, mutante, error = ms.guardarDna(dna)
    if error != None:
        return Response(str(error), status=401)
    return Response(status=201)

@magnetoservice.route('/stats', methods=['GET'])
def stats():
    ms = MagnetoService()
    cant_mutant, cant_human, ratio , error = ms.stats()
    if error != None:
        return Response(str(error)) 
    res = {
        "count_mutant_dna": cant_mutant,
        "count_human_dna": cant_human,
        "ratio": ratio
        }
    return res


