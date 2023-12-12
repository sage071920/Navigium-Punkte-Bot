from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
from discord_webhook import DiscordWebhook

def click_solution_and_correct_buttons(url1):


    driver.get(url1)
    username_field = driver.find_element(By.NAME, "name")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("USERNAME")
    password_field.send_keys("PASSWORD")

    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()
    
    desired_text = "Vokabeltrainer n. Karteikasten"
        
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[text()='{desired_text}']"))
        )

    div_element.click()

    time.sleep(1)

    Muendlich_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Mündlich")]'))
        )

    Muendlich_button.click()

    time.sleep(1)

    Starten_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Starten")]'))
        )

    Starten_button.click()

    while True:

        time.sleep(1.5)
        xpathdiv = '//div[@class="col-md-5"]'
        div_textzahl = driver.find_element(By.XPATH, xpathdiv)
        text = div_textzahl.text
        zahl = re.search(r'\d+', text)

        if zahl:
            extracted_number = int(zahl.group())  
            print(extracted_number) 
 
        else:
         print("Keine Zahl gefunden")


        for i in range(extracted_number):
            loesung_button = WebDriverWait(driver, 90).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Lösung")]'))
            )

            

            loesung_button.click()

            richtig_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Richtig")]'))
            )

            richtig_button.click()

        time.sleep(1)

        if extracted_number < 100:
            ending()
        else:
            stillgoing()

def stillgoing():
    speichern_button2 = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Ergebnisse speichern")]'))
    )

    speichern_button2.click()
    time.sleep(1)
    Hauptmenue_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Hauptmenü")]'))
    )
    Hauptmenue_button.click()
    time.sleep(1)
    desired_text = "Vokabeltrainer n. Karteikasten"
    div_element=WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, f"//div[text()='{desired_text}']"))
    )

    div_element.click()
    time.sleep(1)
    Muendlich_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Mündlich")]'))
    )
    Muendlich_button.click()
    time.sleep(1)
    Starten_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Starten")]'))
    )
    Starten_button.click()



def ending():
    speichern_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "speichern")]'))
    )
    speichern_button.click()
    time.sleep(1)
    webhook = DiscordWebhook(url="YOUR_DISCORD_WEBHOOK", content="Navigium Fertig!!")
    response = webhook.execute()
    time.sleep(1)
    exit()


options = Options()
options.add_argument("--user-data-dir=/path/to/profile")

driver = webdriver.Chrome(options=options)

url1 = ("https://www.navigium.de/login/schule/RBG_LANGENAU")
click_solution_and_correct_buttons(url1)
