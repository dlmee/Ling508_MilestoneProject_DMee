#Thanks to Dr. Berry for his example code in Sanskrit Repos
# https://github.com/jjberry-508/sanskrit-508/tree/week6

from flask import Flask, request, jsonify
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

services.instantiatedb()


@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()

'''
@app.route("/generate", methods=["GET"])
def generate_words():
    services.generate_words()
    app.logger.info("/generate - Generated words.")
    return jsonify({"msg": "success"})
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0')