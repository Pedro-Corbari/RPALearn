import datetime
import os
import shutil

import pandas as pd

date_key = 'DT_ABERTURA'
parent_dir = r"C:\RPA\\"
name_dir = 'arquivos_gerados\\'

arquivosGerados = f'{parent_dir}{name_dir}'

def convert_date(date):
    return datetime.datetime.strptime(str(date), '%d/%m/%Y')  # .strftime('%Y-%m-%d')

def filtrar_linhas():
    df = pd.read_csv('licitacao.csv', date_parser=convert_date)
    filtered_df = df.loc[(df[date_key] >= '2022-05-01')].sort_values(date_key)
    firstRows = filtered_df.head(30)  # [:30]
    return firstRows


def apaga_arquivos_temp():
    shutil.rmtree(f'{parent_dir}{name_dir}')


def gera_pastas(firstRows):
    for index, row in firstRows.iterrows():
        cdOrgao = row['CD_ORGAO']
        cdTipoModalidade = row['CD_TIPO_MODALIDADE']
        nrLicitacao = int(row['NR_LICITACAO'])
        anoLicitacao = row['ANO_LICITACAO']

        os.makedirs(f'{arquivosGerados}{cdOrgao} - {cdTipoModalidade} - {nrLicitacao} - {anoLicitacao}')
        #print(f'{arquivosGerados}{cdOrgao} - {cdTipoModalidade} - {nrLicitacao} - {anoLicitacao}')


#primeirasLinhas = Teste.filtrar_linhas()
#apaga_arquivos_temp()

