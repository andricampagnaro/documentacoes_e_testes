from loguru import logger
from functools import wraps, partial
import sys
import inspect

logger.remove()
logger.add(sys.stdout, level="DEBUG", colorize=True, format="<level>{time} | {level} | {message}</level>")
logger.add('Avisos.log', level="WARNING", format="{time} | {level} | {message}")
logger.add('Erros.log', level="ERROR", format="{time} | {level} | {message}")

class Log:
    def debug(self, mensagem):
        return logger.debug(f'{self.__class__.__name__} | {inspect.stack()[1][3]} | {mensagem}')

    def warning(self, mensagem):
        return logger.warning(f'{self.__class__.__name__} | {inspect.stack()[1][3]} | {mensagem}')

    def error(self, mensagem):
        return logger.error(f'{self.__class__.__name__} | {inspect.stack()[1][3]} | {mensagem}')


def real_warning(andrieli):
    def log_warning(funcao):
        @wraps(funcao)
        def funcao_decorada(*args, **kwargs):
            logger.warning(f'{andrieli} | {funcao.__qualname__.split(".")[0]} | {funcao.__name__} | inicio')
            funcao(*args, **kwargs)
            logger.warning(f'{andrieli} | {funcao.__qualname__.split(".")[0]} | {funcao.__name__} | fim')
        return funcao_decorada
    return log_warning
    
# real_warning = partial(log_warning, nome_objeto='Default')

def real_error(andrieli):
    def log_error(funcao):
        @wraps(funcao)
        def funcao_decorada(*args, **kwargs):
            logger.error(f'{andrieli} | {funcao.__qualname__.split(".")[0]} | {funcao.__name__} | inicio')
            funcao(*args, **kwargs)
            logger.error(f'{andrieli} | {funcao.__qualname__.split(".")[0]} | {funcao.__name__} | fim')
        return funcao_decorada
    return log_error

def real_debug(andrieli):
    def log_debug(funcao):
        @wraps(funcao)
        def funcao_decorada(*args, **kwargs):
            logger.debug(f'{andrieli} | {funcao.__qualname__.split(".")[0]} | {funcao.__name__} | inicio')
            funcao(*args, **kwargs)
            logger.debug(f'{andrieli} | {funcao.__qualname__.split(".")[0]} | {funcao.__name__} | fim')
        return funcao_decorada
    return log_debug

class ObjetoTeste(Log):
    def __init__(self):
        self.teste = 'essa é uma mensagem de teste'

    @real_debug('teste')
    def executa_validacoes(self):
        self._validacao1(10, 20)
        self._validacao2(30)
        self._nome()

    @real_debug('outro_nome')
    def _validacao1(self, arg1, arg2):
        print(f'{arg1} e {arg2}')

    @real_debug('mais um')
    def _validacao2(self, arg):
        super().warning('MAIUSCULAS MAIUSCULAS MAIUSCULAS MAIUSCULAS MAIUSCULAS MAIUSCULAS ')
        print(arg)

    @real_warning('ANDRIELI')
    def _nome(self):
        super().error('FADA FADA FADA FADA FADA FADA FADA FADA FADA FADA')
        print(self.__class__.__name__)


def printar():
    print('teste')

@real_error('teste')
def funcao_com_erro():
    print('erro')

@real_debug('esse tmb')
def funcao_com_argumentos(argumento1, argumento2):
    print(f'{argumento1} e {argumento2}')


if __name__ == '__main__':
    printar()
    funcao_com_erro()
    funcao_com_argumentos('teste', 1)

    meu_objeto = ObjetoTeste()
    meu_objeto.executa_validacoes()