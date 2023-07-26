from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Am anfang noch selber in Mündlich rein gehen ansonsten geht es von selber solange es immer 100 Wörter sind die bei Mündlich sind 

def click_solution_and_correct_buttons(url):
    options = Options()
    options.add_argument("--user-data-dir=/path/to/profile")

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    while True:
        for i in range(100):
            loesung_button = WebDriverWait(driver, 90).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Lösung")]'))
            )

            

            loesung_button.click()

            richtig_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Richtig")]'))
            )

            richtig_button.click()

        speichern_button = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "speichern")]'))
        )

        speichern_button.click()

        time.sleep(1)

        Hauptmenue_button = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Hauptmenü")]'))
        )

        Hauptmenue_button.click()

        time.sleep(1)

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

url = ("https://www.navigium.de/login")

click_solution_and_correct_buttons(url)