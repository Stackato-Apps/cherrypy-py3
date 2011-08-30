import os
import sys
import cherrypy

class HelloWorld:
    def index(self):
        pyver = '.'.join(map(str, tuple(sys.version_info)[:3]))
        return "Hello world! (from Python %s)" % pyver
    index.exposed = True


if __name__ == '__main__':
    port = int(os.getenv('VCAP_APP_PORT', '8000'))
    host = os.getenv('VCAP_APP_HOST', '0.0.0.0')
    cherrypy.quickstart(
        HelloWorld(),
        config={
            'global': {
                'server.socket_port': port,
                'server.socket_host': host}})
