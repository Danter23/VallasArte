from flask import Flask, render_template, request, redirect, url_for, session
from database import init_db, db

app = Flask(__name__)
app.secret_key = 'vallasarte_secret_key_python'

init_db(app)

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Lógica de autenticación migrada de login.php
        session['user'] = username
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/facturas')
def facturas():
    return render_template('facturas.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/transporte')
def transporte():
    return render_template('transporte.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
