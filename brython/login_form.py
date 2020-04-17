from browser import document
from browser.html import INPUT, LABEL, BR, FORM, H1, H2

def cabecalho():
    document <= H1('Página escrita em Brython')

def login_form():
    form = FORM(Class='form login-form', id="meu-forme", action="#", method="GET", target="blank")

    form <= H2('Meu formulário')
    form <= LABEL('seu nome', For='nome')
    form <= INPUT(id='nome', name='nome', required=True)
    form <= BR()
    form <= LABEL('sua senha', For='senha')
    form <= INPUT(id='senha', type='password', name='senha', required=True)
    form <= BR()
    form <= INPUT(id='submit', type='submit')

    document <= form