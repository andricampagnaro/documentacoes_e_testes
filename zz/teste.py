class Parametros:
    def __init__(self, primeiro='teste'):
        self.primeiro = primeiro

    def cria_segundo(self, segundo):
        self.segundo = segundo

parametros = Parametros()
print(parametros.primeiro)
parametros.cria_segundo('mais um teste')
print(parametros.segundo)

