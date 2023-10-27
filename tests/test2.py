from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_seleccion:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://bertoldi.com.ar/"


    def abrir_pagina(self):
            # Abrir la página de Bertoldi
            self.driver.get(self.url)
        

    def inicio_sesion(self):
            self.driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]').click()
            time.sleep(2)
            self.driver.find_element(By.ID,'CustomerEmail').send_keys("guido123@hotmail.com")
            self.driver.find_element(By.ID,'CustomerPassword').send_keys("guidoseia")
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="customer_login"]/p[1]/button').click()
            time.sleep(3)


    def busqueda(self):
            self.driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[3]/form/input[3]').send_keys('Delineador De Ojos Star Line Rosa Idi HD')
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="PredictiveResults"]/div/div/div/div/a').click()
            time.sleep(1)


    def seleccionar(self):
        self.abrir_pagina()
        time.sleep(3)
        self.inicio_sesion()
        self.busqueda()
        time.sleep(1)
        

if __name__ == "__main__":
    automation = test_seleccion()   
    automation.seleccionar()