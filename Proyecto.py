from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time

#Se crea la carpeta de capturas de pantalla (si no la hay)
if not os.path.exists("Screenshots"):
    os.makedirs("Screenshots")

#Se define la funcion para realizar las capturas de pantalla
def tomar_captura(driver, nombre_paso):
    ruta_captura = f"Screenshots/{nombre_paso}.png"
    driver.save_screenshot(ruta_captura)
    print(f"Captura Guardada en: {ruta_captura}")

#Punto 5 Utilizar Modo Headless
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
# Punto 1 Se ingresa al primer vinculo para llenar el formulario
    driver.get("https://demoqa.com/automation-practice-form")

    driver.find_element(By.ID, "firstName").send_keys("Steven Alejandro")
    driver.find_element(By.ID, "lastName").send_keys("Sandoval Cardozo")
    driver.find_element(By.ID, "userEmail").send_keys("steven.steal@example.com")
    driver.find_element(By.XPATH, "//input[@id='gender-radio-1']").send_keys(Keys.SPACE)
    driver.find_element(By.ID, "userNumber").send_keys("3015847110")
    campo_fecha = driver.find_element(By.ID, "dateOfBirthInput")
    campo_fecha.send_keys(Keys.CONTROL + "a")
    campo_fecha.send_keys("30 Jun 2002")
    campo_fecha.send_keys(Keys.ENTER)
    subject = driver.find_element(By.ID, "subjectsInput")
    subject.send_keys("Computer Science")
    subject.send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-3']").send_keys(Keys.SPACE)
    driver.find_element(By.ID, "uploadPicture").send_keys(os.path.abspath(r"C:\Users\steve\Pictures\Python.jpg"))
    driver.find_element(By.ID, "currentAddress").send_keys("Kr 01 # 02 - 03")
    estado = driver.find_element(By.ID, "react-select-3-input")
    estado.send_keys("Uttar Pradesh")
    estado.send_keys(Keys.ENTER)
    ciudad = driver.find_element(By.ID, "react-select-4-input")
    ciudad.send_keys("Lucknow")
    ciudad.send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").send_keys(Keys.ENTER)

    time.sleep(2)

    tomar_captura(driver, "Envio de formulario")

#Punto 2 Carga de Archivos
    driver.get("https://demoqa.com/upload-download")

    driver.find_element(By.ID, "uploadFile").send_keys(os.path.abspath(r"C:\Users\steve\Pictures\Python.jpg"))
    time.sleep(3)
    tomar_captura(driver, "Carga de Archivo")

#Punto 3 Descarga de Archivos
    driver.find_element(By.ID, "downloadButton").send_keys(Keys.ENTER)
    time.sleep(5)

    carpeta_usuario = os.path.expanduser("~")
    ruta_archivo = os.path.join(carpeta_usuario, "Downloads", "sampleFile.jpeg")
    #validar su existencia en una carpeta Downloads
    if os.path.exists(ruta_archivo):
        print("Archivo encontrado en la carpeta: ", ruta_archivo)
    else:
        print("Archivo no encontrado")
#Punto 4 Alertas
    driver.get("https://demoqa.com/alerts")

    driver.find_element(By.ID, "confirmButton").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Esperar a que la alerta esté presente
    alerta = driver.switch_to.alert
    alerta.accept()
    time.sleep(1)
    tomar_captura(driver, "Captura de confirmación")

    driver.find_element(By.ID, "promtButton").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Esperar a que la alerta esté presente
    alerta = driver.switch_to.alert
    alerta.send_keys("Hola Mundo")  # Enviar texto al prompt
    alerta.accept()

    tomar_captura(driver, "Capturar texto de alerta")

finally:
    input("Precione enter para salir")
    driver.quit()