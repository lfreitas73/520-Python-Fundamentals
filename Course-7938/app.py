import flask
app=flask.Flask(__name__)
@app.route("/")
def home():
    return "TESTE DE WEB SERVER !!!!"