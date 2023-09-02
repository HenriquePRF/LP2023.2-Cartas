from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def cartas():
    return render_template("login.html")

username = 'nome'
password = 'senha'

@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        if nome == username and senha == password:
            return render_template("cartas.html")
        else:
            return "<h1>Senha ou Usuario incorreto</h1>"
    
"""
with open('login.txt', 'r') as login_file:
    for line in login_file:
        if "Username:" in line:
            username = line.split(":")[1].strip()
        elif "Password:" in line:
            password = line.split(":")[1].strip()
    login_file.close()
"""




app.run()