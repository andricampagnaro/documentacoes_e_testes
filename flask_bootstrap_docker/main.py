from flask import Flask, request
from flask import render_template
import funcoes

app = Flask(__name__)

@app.route('/')
def main():
    return 'hello world'

@app.route('/chama_funcao')
def chama_funcao():
    resultado = funcoes.soma(2, 3)
    print(f'Olha só o resultado: {resultado}')
    return 'somou'

@app.route('/formulario')
def formulario():
    return render_template('form-basic.html')

@app.route('/my_form', methods=['POST'])
def my_form():
    form_input = request.form['unico_campo']
    print(form_input)
    return "done"