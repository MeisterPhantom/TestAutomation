from selenium.webdriver.common.by import By


class ContactUsLocators:
    ATTACH_FILE_FIELD = (By.XPATH, '//*[@id="fileUpload"]')
    CONTACT_US_BTN = (By.XPATH, '//*[@id="contact-link"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="email"]')
    MESSAGE_FIELD = (By.XPATH, '//*[@id="message"]')
    ORDER_REFERENCE_FIELD = (By.XPATH, '//*[@id="id_order"]')
    SEND_BTN = (By.XPATH, '//*[@id="submitMessage"]')
    SUBJECT_FIELD = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/fieldset/div[1]/div[1]/div[1]/div/select/option[2]')
    SUBJECT_LIST = (By.XPATH, '//select/option')
    RESULT = (By.XPATH, '/html/body/div/div[2]/div/div[3]/div/p')
