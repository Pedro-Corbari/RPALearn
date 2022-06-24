import rpa as r
import pyautogui as p

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