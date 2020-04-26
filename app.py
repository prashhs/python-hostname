from flask import Flask , request , jsonify
import socket,sys

app = Flask(__name__)

@app.route("/")
def get_hostname():
    return jsonify ({ 'host' : socket.gethostname(),
    'version' : sys.version_info[0] })

# @app.route("/new")
# def helloNew():
#     name = request.args.get('name')
#     return "hello {}!".format(name)

if __name__ == "__main__":
    app.run(host="0.0.0.0")