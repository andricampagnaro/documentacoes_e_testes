from grava_logs import *

class MeuNovoObjeto(Log):
    def __init__(self, teste):
        self._teste = teste

    @log_debug
    def executa_validacoes(self):
        self._validacao1()
        self._validacao2(2, 3)

    @log_debug
    def _validacao1(self):
        super().warning(self._teste == 'valor')
        # logger.warning(self._teste == 'valor')

    @log_debug
    def _validacao2(self, arg1, arg2):
        super().error(f'{arg1} e {arg2}')
        # logger.error(f'{arg1} e {arg2}')

if __name__ == '__main__':
    objeto_valor = MeuNovoObjeto('valor')
    objeto_valor.executa_validacoes()
