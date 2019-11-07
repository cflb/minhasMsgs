from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'pagina inicia'

if __name__ == "__main__":
    app.run(debug=True)

