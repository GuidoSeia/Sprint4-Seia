from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_eliminarProductoCarrito:
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
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="PredictiveResults"]/div/div/div/div/a').click()
            time.sleep(1)
    
    def aumentarCantidad(self):
          cantidad = 2
          for i in range(cantidad):
            self.driver.find_element(By.XPATH,'//*[@id="ProductSection-template--16134502580456__main-8124947464424"]/div/div/div[2]/div[2]/div/div[2]/div[9]/div/div/button[2]').click()
            time.sleep(1)
          

    def agregarAlCarrito(self):
            self.driver.find_element(By.XPATH, '//*[@id="AddToCartForm-template--16134502580456__main-8124947464424"]/div[3]/button').click()
            time.sleep(1)

    
    def disminuirCantidad(self):
            cantidad = 3
            for i in range(cantidad):
                self.driver.find_element(By.XPATH,'//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[1]').click()
                time.sleep(1) 


    def validarCarritoVacio(self):
            mensaje_carrito_vacio = self.driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/div')  
            if mensaje_carrito_vacio.is_displayed() and mensaje_carrito_vacio.text == "Su carrito actualmente está vacío":
                    print("El carrito está vacío.")
            else:
                    print("El carrito no está vacío o el mensaje no se encontró.")
  

    def eliminar(self):
            self.abrir_pagina()
            self.busqueda()
            self.aumentarCantidad()
            self.agregarAlCarrito()
            self.disminuirCantidad()
            self.validarCarritoVacio()
            time.sleep(5)
        
          


if __name__ == "__main__":
    automation = test_eliminarProductoCarrito()
    automation.eliminar()