import dataset

def soma(a, b):
    return a + b

class BancoDados:
    def __init__(self):
        self.db = dataset.connect('postgresql://postgres:postgres@172.18.0.3:5432/postgres')
        self.tabela = self.db['tabela_teste1']

    def insere_nome(self, informacao):
        self.tabela.insert(dict(nome=informacao, idade=0))

if __name__ == "__main__":
    banco = BancoDados()
    print(banco.db.tables)
    print(banco.db['tabela_teste1'].columns)
    banco.insere_nome('nome1')
    print(list(banco.db['tabela_teste1'].all()))