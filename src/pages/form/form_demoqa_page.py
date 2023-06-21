from src.resources.form.form_resources_demoqa import *
from helper_methods.helpermethods import *


class FormDemogaPage:

    def __init__(self, browser):
        self.browser = browser

    def send_field_information(self, first_name, last_name, email, movil_number, date_of_birth, subjects, current_address):
        self.browser.find_element(*FormResources.FIRSTNAME_FIELD).send_keys(first_name)
        self.browser.find_element(*FormResources.LASTNAME_FIELD).send_keys(last_name)
        self.browser.find_element(*FormResources.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*FormResources.MOVIL_NUMBER_FIELD).send_keys(movil_number)
        self.browser.find_element(*FormResources.SUBJECTS_FIELD).send_keys(subjects)
        self.browser.find_element(*FormResources.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        self.browser.find_element(*FormResources.DATE_OF_BIRTH_FIELD).send_keys(date_of_birth)

    def select_gender(self, option):
        HelperMethods(self.browser).get_element(FormResources.GENDER_RADIO_BTN, option)

    def select_hobbie(self, option):
        HelperMethods(self.browser).get_element(FormResources.HOBBIE_RADIO_BTN, option)

    def send_data_form(self):
        self.browser.find_element(*FormResources.SUBMIT_BTN).click()
