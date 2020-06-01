from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='operacoes-aritmeticas',
    url='https://github.com/andricampagnaro/documentacao_python3',
    author='Andrieli Campagnaro',
    author_email='andricampagnaro@gmail.com',
    # Needed to actually package something
    packages=['operacoes_basicas', 'operacoes_intermediarias'],
    # Needed for dependencies
    # install_requires=['numpy'],
    # *strongly* suggested for sharing
    version=0.1,
    # The license can be anything you like
    license='MIT',
    description='Um pacote de teste com as operacoes matemáticas mais básicas: Adição e Substração.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)