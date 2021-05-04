from flask import Flask, jsonify, request
import json

servico = Flask(__name__)

IS_ALIVE = "Lean Ativo"

LEAN = "/templates/lean_inception.json"

@servico.route("/isalive/")
def is_alive():
    return IS_ALIVE


# rota que retorna o template Lean Inception
@servico.route("/lean/")
def get_lean_inception():
    arquivo = open (LEAN,"r")
    dados = json.load(arquivo)
    arquivo.close

    return dados

if __name__ == "__main__":
    servico.run(
        host = "0.0.0.0",
        debug=True
    )