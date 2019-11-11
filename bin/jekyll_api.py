#!/usr/bin/python3
"""This api module allows you to publish new posts via curl"""

# Imports
import os # File location stuff
import magic # Testing uploaded file type (WIP)
import flask # API Framework
from flask import request, Response # API framework
from werkzeug.utils import secure_filename # Secure filenames helper

# Initialize and configure flask
japi = flask.Flask(__name__)
japi.config['DEBUG'] = True
japi.config['POSTDIR'] = '/var/www/default/_posts'
japi.config['SAFEEXT'] = {'md', 'markdown'}
japi.config['SECUREID'] = 'asdf12345'
japi.config['HOSTIP'] = '127.0.0.1'
japi.config['PORT'] = '10000'

# def transformFileName(filename):
# TODO: automatically transform filenames into Y-M-D-NAME format

# Base api route, won't really return much
@japi.route('/api', methods=['GET'])
def api_base():
    """Literally a debug function to make sure the api is running"""
    return 'api touched'

# Providing probe definitions to a host
@japi.route('/api/v1/newpost', methods=['POST'])
def make_new_post():
    """Ingest new markdown file to publish to jekyll"""
    if 'file' not in request.files:
        return Response("{'Error':'No file'}\n", status=417, mimetype='application/json')
    if request.headers['id'] != japi.config['SECUREID']:
        return Response("{'Error':'Invalid token'}\n", status=401, mimetype='application/json')
    new_post_file = request.files['file']
    #tf_file_name = transformFileName(new_post_file.filename)
    # Read the file and verify it's not malicious (WIP)
    file_content = new_post_file.read()
    file_type = magic.from_buffer(file_content)
    if file_type == 'ASCII text':
        secure_file_name = secure_filename(new_post_file.filename)
        with open(os.path.join(japi.config['POSTDIR'], secure_file_name), 'wb') as post:
            post.write(request.files['file'].read())
        return Response("{'Success':'Post published}\n", status=200, mimetype='application/json')
    else:
        return Response("{'Error':'Invalid file type'}\n", status=415, mimetype='application/json')
japi.run(host=japi.config['HOSTIP'], port=japi.config['PORT'])
