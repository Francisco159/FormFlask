from app import app
from flask import flash, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from dbconfig import mysql
import pymysql

@app.route('/')
def helloworld():
    return render_template('form.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    conn = None
    cursor = None
    try:
        if request.method == 'POST':
            name = request.form['name']
            appa = request.form['appa']
            apma = request.form['apma']
            phone = request.form['phone']
            sex = request.form['sex']
            address = request.form['address']
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql = "insert into empleado (nombre,ape_pat,ape_mat,telefono,sexo,direccion) values (%s,%s,%s,%s,%s,%s)"
            values = (name, appa, apma, phone, sex, address)
            cursor.execute(sql, values)
            conn.commit()
            return render_template('form.html')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/mostrar')
def mostrar():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'select * from empleado;'
        cursor.execute(sql)
        datos = cursor.fetchall()
        conn.commit()
        return render_template('mostrar.html', datos=datos)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/formDelete')
def formDelete():
    return render_template('delete.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    conn = None
    cursor = None
    try:
        if request.method == 'POST':
            name = request.form['name']
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sql = 'delete from empleado where nombre = %s;'
            value = (name)
            cursor.execute(sql, value)
            sql2 = 'alter table empleado AUTO_INCREMENT=1;'
            cursor.execute(sql2)
            conn.commit()
            return render_template('delete.html')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def not_found():
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.run()
