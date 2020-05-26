from loguru import logger
import sys

logger.add(sys.stderr, format="{time} | {level} | {message}", level="INFO")
logger.add('debug.log', format="{time} | {level} | {module} | {line} | {function} | {message} ", level="INFO")
logger.add('info.log', level="INFO")

class OutraFuncao:
    def executa(self):
        logger.debug('Texto debug')
        logger.info('Texto info')
        logger.warning('Texto warning')
        logger.error('Texto error')
        logger.critical('Texto critical')