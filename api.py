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
  endereco = request.form['endereco']
  if nome and cpf and endereco:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_user (user_nome, user_cpf, user_endereco) VALUES (%s, %s, %s)', (nome, cpf, endereco))
    conn.commit()
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select user_nome, user_cpf, user_endereco from tbl_user')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)


    # SQL

    # create schema teste;

    # use teste;

    # CREATE TABLE tbl_user ( user_id BIGINT NOT NULL AUTO_INCREMENT, user_nome VARCHAR(45) NULL, user_cpf VARCHAR(45) NULL, user_endereco VARCHAR(45) NULL, PRIMARY KEY (user_id));