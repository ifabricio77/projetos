from flask import Flask, jsonify, request
import json

servico = Flask(__name__)

IS_ALIVE = "Planning Ativo"

PLANNING = "/templates/planning.json"

@servico.route("/isalive/")
def is_alive():
    return IS_ALIVE


@servico.route("/planning/")
def get_planning():
    arquivo = open (PLANNING,"r")
    dados = json.load(arquivo)
    arquivo.close

    return dados

if __name__ == "__main__":
    servico.run(
        host = "0.0.0.0",
        debug=True
    )