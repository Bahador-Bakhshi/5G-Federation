#!/usr/bin/env python3

import connexion
import pathlib
import logging

from flask.logging import default_handler

from swagger_server import encoder
import swagger_server.core.init_ac as init_ac
import swagger_server.core.learned_policy as policy


def main():
    
    init_ac.init()
    policy.load_policy()
    
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.logger.setLevel(logging.WARNING)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Admission Controller API'}, pythonic_params=True)

    
    app.run(port=8080)


if __name__ == '__main__':
    main()
    
    

