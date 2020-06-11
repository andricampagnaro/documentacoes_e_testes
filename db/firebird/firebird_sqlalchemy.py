import sqlalchemy

URL = "firebird://sysdba:masterkey@localhost:3050//var/lib/firebird/2.5/data/GIGAERP.FDB?charset=WIN1252"
engine = sqlalchemy.create_engine(URL)
conn = engine.connect()
resultado = conn.execute('select max(cod_cliente) from clientes;')

for row in resultado:
    print(row)