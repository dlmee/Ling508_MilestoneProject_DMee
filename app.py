#Thanks to Dr. Berry for his example code in Sanskrit Repos
# https://github.com/jjberry-508/sanskrit-508/tree/week6

from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})


services = Services()


@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()

@app.route('/web')
def web() -> str:
    app.logger.info("web - Got request")
    with open("web/sense_finder.html", "r") as f:
        return f.read()

@app.route("/generatedb", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def generate_db():
    data = request.get_json()
    app.logger.info(f"/find_sense - Got request: {data}")
    results = services.instantiatedb(data.get('url'))
    app.logger.info(f"/generatedb - output: {results}")
    return jsonify(results)


@app.route("/find_sense", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def parse_word():
    data = request.get_json()
    app.logger.info(f"/find_sense - Got request: {data}")
    results = services.findsenses(data.get('word'))
    allforms = []
    for result in results.senses:
        forms = {}
        forms['surface'] = result.surface
        forms['sense'] = result.sense
        forms['vector'] = result.definition
        forms['examples'] = result.examples
        allforms.append(forms)
    app.logger.info(f"/find_sense - Output: {allforms}")
    return jsonify(allforms)



if __name__ == "__main__":
    app.run(host='0.0.0.0')