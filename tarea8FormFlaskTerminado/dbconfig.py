from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

#configuracion
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'francisco'
app.config['MYSQL_DATABASE_DB'] = 'testing'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

#configuracion mysql, si funciona
#import mysql.connector

#database = mysql.connector.connect(
#            host = 'localhost',
#            user = 'root',
#            password = 'francisco',
#            database = 'testing'
#        )
