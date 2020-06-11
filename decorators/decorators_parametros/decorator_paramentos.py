from loguru import logger
from functools import wraps
import sys
import inspect

logger.remove()
logger.add(sys.stdout, level="DEBUG", colorize=True, format="<level>{time} | {level} | {message}</level>")

def log_debug(argumento='DEFAULT'):
    def real_debug(funcao):
        @wraps(funcao)
        def funcao_decorada(*args, **kwargs):
            instance = { chave: valor for chave, valor in inspect.getmembers(funcao) if chave == '__name__' }
            logger.debug(f'{argumento} | {instance["__name__"]} | {funcao.__name__} | inicio')
            funcao(*args, **kwargs)
            logger.debug(f'{argumento} | {instance["__name__"]}  | {funcao.__name__} | fim')
        return funcao_decorada
    return real_debug

class NovoObjeto():
    var = 'NovoObjeto'

    def __init__(self, variavel):
        self.variavel = variavel

    def __doc__(self):
        return self.variavel

    @log_debug(argumento='var')
    def teste(self, primeiro=var):
        print('executou')

class MaisUm(NovoObjeto):
    def __init__(self, variavel):
        super().__init__(variavel)

    def novo_metodo(self):
        return 'nada'    

if __name__ == '__main__':
    novo_objeto = NovoObjeto('Andri')
    novo_objeto.teste()

    mais_um = MaisUm
    mais_um.teste('1234')
    