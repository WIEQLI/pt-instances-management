"""
Created on 13/07/2015

@author: Aitor Gomez Goiri <aitor.gomez-goiri@open.ac.uk>
"""

import urllib2
from os import environ as env
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flasgger import Swagger
from ptinstancemanager.config import configuration


# Install proxy in urllib2 (if it is set)
def get_proxy_config():
    el = {}
    if 'http_proxy' in env:
        el['http'] = env['http_proxy']
    elif 'HTTP_PROXY' in env:
        el['http'] = env['HTTP_PROXY']
    if 'https_proxy' in env:
        el['HTTPS_PROXY'] = env['https_proxy']
    elif 'HTTPS_PROXY' in env:
        el['https'] = env['HTTPS_PROXY']
    return el

conf = get_proxy_config()
if conf:
    proxy = urllib2.ProxyHandler(conf)
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)


# Create web application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = configuration.get_database_uri()
app.config['LOWEST_PORT'] = configuration.get_lowest_port()
app.config['HIGHEST_PORT'] = configuration.get_highest_port()
app.config['DOCKER_URL'] =  configuration.get_docker_url()
app.config['DOCKER_IMAGE'] = configuration.get_docker_image_name()
app.config['DOCKER_DATA_ONLY'] = configuration.get_docker_data_container()
app.config['DOCKER_VNC_PORT'] =  configuration.get_docker_vnc_port()
app.config['DOCKER_PT_PORT'] =  configuration.get_docker_pt_port()
app.config['CACHE_DIR'] =  configuration.get_cache_directory()
app.config['CACHE_CONTAINER_DIR'] =  configuration.get_container_directory()
app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "pt-instances-management",
    "specs": [{
            "version": "0.0.1",
            "title": "API v1",
            "endpoint": 'v1_spec',
            "route": '/spec',
            "rule_filter": lambda rule: rule.endpoint.startswith('v1'),
    }],
}
swagger = Swagger(app)

# Configure DB
db = SQLAlchemy(app)
