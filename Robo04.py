import rpa as r
import pyautogui as p

r.init()
r.url('https://www.udemy.com')
p.sleep(5)
localPesq = p.locateOnScreen('Capturar.PNG', confidence=0.6)
print(localPesq)