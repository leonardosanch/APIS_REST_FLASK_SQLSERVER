import pyodbc
#TODO: configuracion de la conexion a SQL SERVER
server = 'localhost'
database = 'Northwind'
username = 'sa'
password = ''

#TODO: Crear la cadena de conexion 
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

#TODO: Establecer la conexion
conn = pyodbc.connect(conn_str)

#TODO: Crear Cursor
cursor = conn.cursor()

try: 
    #TODO: LLamar al query
    cursor.execute(" select  EmployeeID , LastName , Title ,FirstName, Title , Address   from Employees")
    
    
    #TODO Obtener Resultados   
    rows = cursor.fetchall()
    
    #TODO: Mostrar los resultados en consola 
    for row in rows:
        print(row)
        
    
except Exception as e:
    print(f"Error:{str(e)}")
    
finally:
    cursor.close
    conn.close
    
    
