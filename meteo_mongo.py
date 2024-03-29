from datetime import datetime,timedelta
from pymongo import MongoClient
import psycopg2
import random



# Conectamos a mongo
client = MongoClient()
mongo = client.eolica


# Conectamos a pg

pg_conn = psycopg2.connect("dbname='eolica' user='eolica' host='db.gregal' password='eolica'")
cur = pg_conn.cursor()
cur.execute("""SELECT * from observaciones_eolica where nombre_cliente = 'EVERPOWER'""")


def llena_observaciones_de_gregal():
    mongo.observaciones.drop()
    for row in cur.fetchall():
        observacion = {}
        observacion['nombre_cliente'] = row[0]
        observacion['codigo_unidad'] = row[1]
        observacion['fecha_obs'] = row[2]
        observacion['valor'] = row[3]
        observacion['periodo_acu'] = row[4]
        observacion['valid'] = row[5]
        observacion['tipo_observable'] = row[6]
        print "Metiendo %s" % observacion
        mongo.observaciones.insert(observacion)
        
def inserta_observaciones():
    cluster = MongoClient('mongodb://admin:123456@localhost:8881/')
    db_cluster = cluster.eolica
    origen = mongo.observaciones.find()
    db_cluster.observaciones.remove()
    return db_cluster.observaciones.insert(list(origen))



if __name__ == "__main__":
    llena_observaciones_de_gregal()
