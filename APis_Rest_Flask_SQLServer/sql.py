from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

nombre_usuario = 'sa'
contrasena = 'Colombia4$'
nombre_servidor ='localhost'
nombre_base_de_datos = 'Northwind'
driver_odbc = 'ODBC+Driver+17+for+SQL+Server'
cadena_conexion = f'mssql+pyodbc://{nombre_usuario}:{contrasena}@{nombre_servidor}/{nombre_base_de_datos}?driver={driver_odbc}'
app.config['SQLALCHEMY_DATABASE_URI'] = cadena_conexion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/consulta_sql_directa')
def consulta_sql_directa(): 
    sql_query = text('select  EmployeeID , LastName , Title ,FirstName, Title , Address   from Employees')
    
    resultados = db.session.execute(sql_query)
    
    usuarios_json = [dict(row._asdict()) for row in resultados]
    
    return jsonify({'usuarios': usuarios_json})

if __name__ == '__main__':
    #TODO: Configuracion para ejecutar la aplicacion en modo depuracion
    app.run(debug=True)
    
