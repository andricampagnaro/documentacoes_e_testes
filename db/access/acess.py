import subprocess

arquivo = 'database_access.mdb'

print('start')
subprocess.call(f'./access_to_csv.sh {arquivo}', shell=True)
print('end')