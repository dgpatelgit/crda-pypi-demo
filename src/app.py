#!/usr/bin/env python
import os
import logging

import daiquiri
import flask
from flask import Flask, request

app = Flask(__name__)

app.logger.info('App initialized, ready to rock and roll...')

daiquiri.setup(level=os.environ.get('FLASK_LOGGING_LEVEL', logging.INFO))
_logger = daiquiri.getLogger(__name__)

app.logger.info('Logger setup done.')


@app.route('/', methods=['GET', 'POST'])
def rootRoute():
    return flask.jsonify({
        'data': 'Home route called'
    }), 200


@app.route('/liveness', methods=['GET'])
def liveness():
    """Define the liveness probe."""
    return flask.jsonify({
        'status': 'alive', 
        'data': 'I am a live'
    }), 200


@app.route('/readiness', methods=['GET'])
def readiness():
    """Define the readiness probe."""
    return flask.jsonify({
        'status': 'ready', 
        'data': 'I am always ready.'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=6565)
