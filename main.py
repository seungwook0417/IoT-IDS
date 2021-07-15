from flask import Flask, render_template, g
from db import *

# Definicoes do flask
app = Flask(__name__, static_url_path='', static_folder='templates')
DATABASE = "./database.db"

# ---------------------------------------------------------------------------------------
@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

# pagina principal do dashboard
@app.route("/")
def dashboard():
    cur = g.db
    devies = cur.execute("SELECT devies FROM attack where id = 1").fetchone()[0]
    attacks = cur.execute("SELECT attacks FROM attack where id = 1").fetchone()[0]
    data = cur.execute("SELECT IP, MAC, Device, Status, currenttime FROM device order by id desc").fetchall()
    return render_template('/index.html', data=data, connected_devices=devies, attacks=attacks)

if __name__ == "__main__":
    initDB(DATABASE)
    app.run(host="0.0.0.0", port=5000)
