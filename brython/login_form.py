from browser import document
from browser.html import INPUT, LABEL, BR, FORM, H1

def login_form():
    form = FORM(id="meu-forme", action="#", method="GET", target="blank")

    form <= H1('Meu formulário em Brython')
    form <= LABEL('seu nome', For='nome')
    form <= INPUT(id='nome', name='nome')
    form <= BR()
    form <= LABEL('sua senha', For='senha')
    form <= INPUT(id='senha', type='password', name='senha')
    form <= BR()
    form <= INPUT(id='submit', type='submit')

    document <= form