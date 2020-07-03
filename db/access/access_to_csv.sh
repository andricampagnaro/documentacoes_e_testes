#!/bin/bash

DIRETORIO_ATUAL=$(pwd)
DATABASE=''
DIRETORIO_ARQUIVOS_CSV=''
TABELAS=''

verifica_e_instala_pacotes() {
    echo "Verificando dependencias..."
    pacote=$1
    status=$(dpkg-query -W --showformat='${Status}\n' ${pacote}|grep "install ok installed")
    if [ "${status}" = "" ]; then
        echo "Pacote ${pacote} não existe. Instalando..."
        sudo apt install -y $pacote
    fi
}

grava_variavel_database() {
    DATABASE=$1
}

grava_variavel_diretorio_arquivos_csv() {
    DIRETORIO_ARQUIVOS_CSV=$(echo ${DIRETORIO_ATUAL}/${DATABASE} | awk -F "." '{print $1}')
}

cria_diretorio_arquivos_csv() {
    if [ ! -d ${DIRETORIO_ARQUIVOS_CSV} ]
    then
        echo "Criando diretório para salvar arquivos CSV..."
        mkdir ${DIRETORIO_ARQUIVOS_CSV}
    fi
}

lista_tabelas() {
    echo "Listando tabelas da database..."
    TABELAS=$(mdb-tables ${DATABASE})
}

cria_csv() {
    echo "Iniciando criação dos arquivos CSV:"
    for tabela in ${TABELAS}
    do
        echo "- Criando arquivo ${tabela}"
        mdb-export ${DATABASE} ${tabela} > ${DIRETORIO_ARQUIVOS_CSV}/${tabela}.csv
    done
}

importa_tabelas() {
    verifica_e_instala_pacotes "mdbtools"
    grava_variavel_database $1
    grava_variavel_diretorio_arquivos_csv
    cria_diretorio_arquivos_csv
    lista_tabelas
    cria_csv
}

importa_tabelas $1