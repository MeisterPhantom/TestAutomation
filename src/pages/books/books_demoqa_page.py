from src.resources.books.books_demoqa_resources import *
from helper_methods.helpermethods import *
from selenium.common.exceptions import NoSuchElementException


class BooksDemoqaPage:

    def __init__(self, browser):
        self.browser = browser

    def add_book(self):
        HelperMethods(self.browser).get_element(BooksResources.ADD_BOOK_BTN, "Add To Your Collection")

    def information_book(self):
        try:
            self.browser.find_elemet(*BooksResources.TITLE_BOOK_LABEL).isDisplayed()
        except NoSuchElementException as e:
            # Capturar la excepción específica que se produce cuando no se encuentra el elemento
            print("Excepción capturada: Elemento no encontrado")
        finally:
            self.browser.quit()

    def select_book(self, name_book):
        HelperMethods(self.browser).get_element(BooksResources.BOOK_LIST, name_book)
