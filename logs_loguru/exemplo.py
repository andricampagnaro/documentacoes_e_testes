from loguru import logger
from arquivo_externo import OutraFuncao
import sys

logger.add(sys.stderr, format="{time} | {level} | {message}", level="INFO")
logger.add('log_info.log', level="INFO")

class Teste:
    def __init__(self):
        self.outra_funcao = OutraFuncao()

    def executa(self):
        logger.debug('Inicio Execução')
        self.outra_funcao.executa()
        logger.info('Fim Execução')



if __name__ == '__main__':
    teste = Teste()
    teste.executa()