import datetime
import os
import shutil
import tkinter
import zipfile
import rpa as r
import pyautogui as p
from tkinter import messagebox
import Teste




def convertDate(date):
    return datetime.datetime.strptime(str(date), '%d/%m/%Y')  # .strftime('%Y-%m-%d')

if not os.path.exists('C:\RPA\ArquivosDescompactados'):
    os.makedirs('C:\RPA\ArquivosDescompactados')
r.init()
janela = p.getActiveWindow()
janela.maximize()
r.url('http://dados.tce.rs.gov.br/organization/tribunal-de-contas-do-estado-do-rio-grande-do-sul')
p.sleep(2)
r.type('//*[@id="field-giant-search"]', 'Licitações Consolidado 2022[enter]')
r.click('//*[@id="content"]/div[3]/div/article/div/ul/li[1]/div/h3/a')
r.wait(2.0)
r.click('//*[@id="dataset-resources"]/ul/li/div/button')
r.wait(2.0)
r.click('//*[@id="dataset-resources"]/ul/li/div/ul/li[2]/a')


while not os.path.isfile('2022.csv.zip'):
    p.sleep(1)
    if os.path.isfile('2022.csv.zip'):
        break
r.close()



with zipfile.ZipFile('2022.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('C:\RPA\ArquivosDescompactados')

source_folder = r"C:\RPA\ArquivosDescompactados\\"
destination_folder = r"C:\RPA\\"
files_to_move = ['licitacao.csv', 'item.csv']

# iterate files
for file in files_to_move:
    # construct full file path
    source = source_folder + file
    destination = destination_folder + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)


shutil.rmtree('C:\RPA\ArquivosDescompactados', ignore_errors=True)
os.remove('C:\RPA/2022.csv.zip')


primeiras_linhas = Teste.filtrar_linhas()
Teste.gera_pastas(primeiras_linhas)

tkinter.messagebox.showinfo(title='Bot do Pedrao', message='Processo Concluido')