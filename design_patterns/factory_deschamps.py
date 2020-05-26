class Triangulo():
    # def __init__(self):
    #     self.start()
    #     self.stop()

    def start(self):
        print('[Triangulo] Iniciado')

    def stop(self):
        print('[Triangulo] Parado')

class Quadrado():
    # def __init__(self):
    #     self.start()
    #     self.stop()

    def start(self):
        print('[Quadrado] Iniciado')
    
    def stop(self):
        print('[Quadrado] Parado')

class FrenteCasa():
    def __init__(self):
        self.triangulo = Triangulo()
        self.quadrado = Quadrado()
        self.start()
        self.stop()

    def start(self):
        print('[FrenteCasa] Iniciando...')
        self.triangulo.start()
        self.quadrado.start()
        print('[FrenteCasa] Iniciado!')

    def stop(self):
        print('[FrenteCasa] Parando...')
        self.quadrado.stop()
        self.triangulo.stop()
        print('[FrenteCasa] Parado!')

if __name__ == '__main__':
    minha_casa = FrenteCasa()