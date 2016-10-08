from bottle import route, run, template
import requests
import os
from subprocess import Popen

# startup react-markup-server
Popen('npm start >& react-markup-service.log', shell=True,
                                               stdin=None,
                                               stdout=None,
                                               stderr=None,
                                               close_fds=True)

markup_api_url = 'http://localhost:8181/render'
port = os.getenv('PORT', 8080)

def get_markup(component = '', payload = {}):
    post_data = payload.copy()
    post_data.update({ 'component': component })
    resp = requests.post(markup_api_url, json=post_data)
    print "%s response from react-markup-service: %s" % (resp.status_code, resp.text)
    if resp.status_code == 200:
        return resp.content
    return ''


@route('/')
def index():
    markup = get_markup('./Greeting', { 'name':'world' })
    return markup

@route('/<name>')
def index(name):
    markup = get_markup('./Greeting', {'name': name})
    return markup

run(host='localhost', port=8080)
