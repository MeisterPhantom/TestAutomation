from selenium.common.exceptions import NoSuchElementException
from src.resources.profile.profile_demoqa_resources import *


class ProfileDemoqaPage:

    def __init__(self, browser):
        self.browser = browser

    def delete_book(self):
        self.browser.find_element(*ProfileLocators.DELETE_BOOK_BTN).click()

    def logout_user(self):
        self.browser.find_element(*ProfileLocators.LOGOUT_BTN).click()

    def validate_list_books(self):
        try:
            self.browser.find_elemet(*ProfileLocators.BOOK_LIST).isDisplayed()
        except NoSuchElementException as e:
            # Capturar la excepción específica que se produce cuando no se encuentra el elemento
            print("Excepción capturada: Elemento no encontrado")
        finally:
            self.browser.quit()

    def validate_username_field(self, username):
        text = self.browser.find_element(*ProfileLocators.USERNAME_LABEL).text
        assert text == username
