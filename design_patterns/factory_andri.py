# import logging

# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too ã')

class ValidaSmart():
    def __init__(self):
        self._carrega_modulos_externos()

    def _carrega_modulos_externos(self):
        self.layout_pessoas = LayoutPessoas()
        self.layout_pessoas_enderecos = LayoutPessoasEnderecos()
        self.layout_produtos = LayoutProdutos()

    def executa(self):
        print('[ValidaSmart] Executando...')
        self.layout_pessoas.executa()
        self.layout_pessoas_enderecos.executa()
        self.layout_produtos.executa()
        print('[ValidaSmart] Executado!')


########################################################
class LayoutPessoas():
    def __init__(self):
        self._carrega_modulos_externos()

    def _carrega_modulos_externos(self):
        pass

    def executa(self):
        print('[LayoutPessoas] Executando...')
        print('[LayoutPessoas] Executado!')

class LayoutPessoasEnderecos():
    def __init__(self):
        self._carrega_modulos_externos()

    def _carrega_modulos_externos(self):
        pass

    def executa(self):
        print('[LayoutPessoasEnderecos] Executando...')
        print('[LayoutPessoasEnderecos] Executado!')

class LayoutProdutos():
    def __init__(self):
        self._carrega_modulos_externos()

    def _carrega_modulos_externos(self):
        self.campo_ncm = CampoNCM([1, 2, 3, 4, 5])

    def executa(self):
        print('[LayoutProdutos] Executando...')
        self.campo_ncm.confere_dados()
        print('[LayoutProdutos] Executado!')

########################################################
def busca_ncm(ncm):
    print(f'[Funcao Busca NCM] Buscando NCM {ncm}')
    if ncm == 1:
        print(f'[Funcao Busca NCM] NCM {ncm} é válido')
    else:
        print(f'[Funcao Busca NCM] NCM {ncm} é inválido')

########################################################
class CampoTipoString():
    def __init__(self, lista_registros):
        self.lista_registros = lista_registros
        self._quantidade_registros = len(self.lista_registros)
        self._nome_classe = self.__class__.__name__

    @property
    def tipo(self):
        return 'string'

    def confere_dados(self):
        print(f'[{self._nome_classe}] Iniciando a conferencia padrão...')
        self._verifica_tipo_campo()
        self._verifica_tamanho_campo()
        self._valida_registros_em_branco()
        print(f'[{self._nome_classe}] Conferência padrão concluída.')

    def _verifica_tipo_campo(self):
        print(f'[{self._nome_classe}] Verificando tipo do campo...')
        print(f'[{self._nome_classe}] Tipo do campo verificado.')
    
    def _verifica_tamanho_campo(self):
        print(f'[{self._nome_classe}] Verificando tamanho do campo...')
        print(f'[{self._nome_classe}] Tamanho do campo verificado.')

    def _valida_registros_em_branco(self):
        print(f'[{self._nome_classe}] Validando caracteres em branco...')
        print(f'[{self._nome_classe}] Validação de caracteres em branco concluída.')

########################################################
class CampoNCM(CampoTipoString):
    def confere_dados(self):
        super().confere_dados()
        print(f'[{self._nome_classe}] Iniciando a conferencias específicas do campo...')
        self._valida_caracteres_permitidos()
        print(f'[{self._nome_classe}] Conferencias específicas do campo concluídas...')

    def busca_ncms(self):
        print('[CampoNCM] Buscando NCMs...')
        for ncm in self.lista_registros:
            busca_ncm(ncm)
        print('[CampoNCM] Busca de NCMs concluída.')

    def _valida_caracteres_permitidos(self):
        print(f'[{self._nome_classe}] Validando caracteres...')
        print(f'[{self._nome_classe}] Caracteres validados.')


if __name__ == '__main__':
    valida_smart = ValidaSmart()
    valida_smart.executa()
    print(valida_smart.layout_produtos.campo_ncm.tipo)