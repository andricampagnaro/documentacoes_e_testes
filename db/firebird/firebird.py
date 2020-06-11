import fdb

con = fdb.connect(database='/var/lib/firebird/2.5/data/GIGAERP.FDB', 
                  user='sysdba', 
                  password='masterkey',
                  host='localhost',
                  port=3050,
                  charset='WIN1252')

cur = con.cursor()
cur.execute('select max(cod_cliente) from clientes;')
for row in cur:
    print(row)