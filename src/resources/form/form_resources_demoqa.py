from selenium.webdriver.common.by import *


class FormResources:
    FIRSTNAME_FIELD = (By.XPATH, '//*[@id="firstName"]')
    LASTNAME_FIELD = (By.XPATH, '//*[@id="lastName"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="userEmail"]')
    MOVIL_NUMBER_FIELD = (By.XPATH, '//*[@id="userNumber"]')
    SUBJECTS_FIELD = (By.XPATH, '//*[@id="subjectsInput"]')
    CURRENT_ADDRESS_FIELD = (By.XPATH, '//*[@id="currentAddress"]')
    DATE_OF_BIRTH_FIELD = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    GENDER_RADIO_BTN = '//*[@name="gender"]'
    HOBBIE_RADIO_BTN = '//*[@id="hobbiesWrapper"]/div[2]/div/label'
    SUBMIT_BTN = '//*[@id="submit"]'
