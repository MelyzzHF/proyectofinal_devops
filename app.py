from flask import Flask
import boto3

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hola Mundo Avance Proyecto Final --  App en Docker</h1><p>Servidor corriendo exitosamente con Flask y Nginx.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
