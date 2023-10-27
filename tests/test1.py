from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_navegacion:
    def __init__(self):
        # Inicializar el navegador web (en este caso, Chrome)
        self.driver = webdriver.Chrome()
        self.url = "https://bertoldi.com.ar/"
        self.menu_items = [
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[1]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[2]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[3]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[4]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[5]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[6]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[7]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[8]/a',
            '//*[@id="SiteHeader"]/div[2]/div/ul/li[9]/a',
        ]
    
    def abrir_pagina(self):
        # Abrir la página de Bertoldi
        self.driver.get(self.url)
    
    def navegar_a_home(self):
        elemento_enlace = self.driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[2]/div/a')
        elemento_enlace.click()
        time.sleep(5)  


    def navegar(self):
        self.abrir_pagina()
        for item_xpath in self.menu_items:
            self.driver.find_element(By.XPATH, item_xpath).click()
            time.sleep(3)
            self.navegar_a_home()
        
    def close_browser(self):
        # Cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    automation = test_navegacion()
    automation.navegar()
    automation.close_browser()
