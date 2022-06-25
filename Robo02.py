import os
import shutil
import tkinter
import zipfile
import rpa as r
import pyautogui as p
import pandas as pd
from tkinter import messagebox


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

# # Create a sample dataframe
# df = pd.read_csv('licitacao.csv')
#
# # Convert the date to datetime64
# df['DT_A'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
#
# # Filter data between two dates
# filtered_df = df.loc[(df['date'] >= '2020-09-01')
#                      & (df['date'] < '2020-09-15')]
# # Display
# filtered_df

tkinter.messagebox.showinfo(title='Bot do Pedrao', message='Processo Concluido')