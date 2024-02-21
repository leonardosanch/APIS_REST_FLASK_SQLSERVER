from flask import Flask, jsonify, request
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

@app.route('/api/usuarios', methods=['GET', 'POST'])
def usuarios(): 
    try:
        nombre_store_procedure = 'SP_L_USUARIO_01'
        sql_query = text(f'EXEC {nombre_store_procedure}')
        resultados=db.session.execute(sql_query)
        usuarios_json = [dict(row._asdict()) for row in resultados]
        return jsonify({'usuarios': usuarios_json})
    except Exception as e:
        return jsonify({'error':str(e)})
    
    

@app.route('/api/usuario/<int:id>', methods=['GET', 'POST'])
def usuario(id): 
    try:
        nombre_store_procedure = 'SP_L_USUARIO_02'
        sql_query = text(f'EXEC {nombre_store_procedure} @usu_id=:id')
        resultados=db.session.execute(sql_query,{'id':id})
        usuarios_json = [dict(row._asdict()) for row in resultados]
        return jsonify({'usuarios': usuarios_json})
    except Exception as e:
        return jsonify({'error':str(e)})
    

@app.route('/api/insertar', methods=['POST'])
def insertar():
    try:
        datos_json = request.get_json()
        usu_nom = datos_json['usu_nom']
        usu_correo = datos_json['usu_correo']
        
        nombre_store_procedure = 'SP_I_USUARIO_01'
        sql_query = text(f'EXEC {nombre_store_procedure} @usu_nom=:usu_nom, @usu_correo=:usu_correo')
        db.session.execute(sql_query, {'usu_nom': usu_nom, 'usu_correo': usu_correo})
        db.session.commit()
        
        return jsonify({'Mensaje': 'Usuario se ha registrado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
    
@app.route('/api/update', methods=['PUT'])
def update():
    try:
        datos_json = request.get_json()
        usu_id = datos_json['usu_id']
        usu_nom = datos_json['usu_nom']
        usu_correo = datos_json['usu_correo']
        
        nombre_store_procedure = 'SP_U_USUARIO_01'
        sql_query = text(f'EXEC {nombre_store_procedure} @usu_id=:usu_id, @usu_nom=:usu_nom, @usu_correo=:usu_correo')
        db.session.execute(sql_query, {'usu_id': usu_id,'usu_nom': usu_nom, 'usu_correo': usu_correo})
        db.session.commit()
        
        return jsonify({'Mensaje': 'Usuario se ha actualizado Correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
    
@app.route('/api/delete', methods=['DELETE'])
def delete():
    try:
        datos_json = request.get_json()
        usu_id = datos_json['usu_id']
        
        nombre_store_procedure = 'SP_D_USUARIO_01'
        sql_query = text(f'EXEC {nombre_store_procedure} @usu_id=:usu_id')
        db.session.execute(sql_query, {'usu_id': usu_id})
        db.session.commit()
        
        return jsonify({'Mensaje': 'Usuario se ha eliminado Correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})
        
        
        
    


if __name__ == '__main__':
    #TODO: Configuracion para ejecutar la aplicacion en modo depuracion
    app.run(debug=True)
    
    

    
    

