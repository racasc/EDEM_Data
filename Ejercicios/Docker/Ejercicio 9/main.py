from flask import Flask,request,abort

app = Flask(__name__)

usuarios=[1,2,3,4,5]

@app.route('/')
def index():
    return 'Este es el ejercicio 3 y no te estas equivocando!'

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def getuser(user_id):
    if request.method == 'GET':
        return "Lo tienes"
    if request.method == 'POST':
        return "Lo enviaste"
    if request.method == 'DELETE':
        return "Lo eliminaste"
    else:
        abort(405,description="Method not allowed")

app.run(host='0.0.0.0', port=5000)
