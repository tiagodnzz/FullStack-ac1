import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  cpf = request.form['cpf']
  email = request.form['email']
  if nome and cpf and email:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nome, cpf, email))
    conn.commit()
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select user_name, user_username, user_password from tbl_user')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)