from pytest_bdd import scenarios, given, when, then, parsers
from configurations.conftest import *
from src.pages.Login.login_demoqa_page import LoginDemoqaPage
from src.pages.home.home_demoqa_page import HomeDemoqaPage
from src.pages.modals.modals_demoqa_page import ModalsDemoqaPage
from src.pages.modules.modules_demoqa_page import ModulesDemoqaPage
from src.pages.textbox.textbox_demoqa_page import TextBoxPage
from src.pages.updownload.updownload_demoqa_page import UpDownLoadPage
from src.pages.windows.windows_demoqa_page import WindowsDemoqaPage
from src.pages.form.form_demoqa_page import FormDemoqaPage
from src.pages.profile.profile_demoqa_page import ProfileDemoqaPage
from src.pages.books.books_demoqa_page import BooksDemoqaPage

scenarios('../features/test_demoqa.feature')


@given("the demoqa page is displayed")
def home_demoqa():
    HomeDemoqaPage(browser)


@when(parsers.parse('I select the section "{section}"'))
def select_section(browser, section):
    browser.implicitly_wait(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    HomeDemoqaPage(browser).select_section_option(section)


@when(parsers.parse('I select the option "{option}"'))
@when('I select the option "<option>"')
def select_option(browser, option):
    browser.implicitly_wait(5)
    ModulesDemoqaPage(browser).select_list_option(option)


@then(parsers.parse('I fill the form with "{full_name}", "{email}", "{current_address}", and "{permanent_address}"'))
def fill_textbox_form(browser, full_name, email, current_address, permanent_address):
    browser.implicitly_wait(10)
    TextBoxPage(browser).fill_form(full_name, email, current_address, permanent_address)


@then("send the information")
def send_textbox_form_information(browser):
    TextBoxPage(browser).send_information_form()


@then('I download the file')
def download_action(browser):
    UpDownLoadPage(browser).click_download()


@then(parsers.parse('I fill the form with "{first_name}", "{last_name}", "{email}", '
                    '"{mobile}", "{date_of_birth}", "{subjects}", and "{current_address}"'))
def fill_form(browser, first_name, last_name, email, mobile, date_of_birth, subjects, current_address):
    FormDemoqaPage(browser).send_field_information(first_name, last_name, mobile, date_of_birth, subjects,
                                                   current_address)


@then(parsers.parse('I select the option gender "{gender}"'))
def select_gender(browser, gender):
    FormDemoqaPage(browser).select_gender(gender)


@then(parsers.parse('I select the option hobbies "{hobbies}"'))
def select_hobbies(browser, hobbies):
    FormDemoqaPage(browser).select_hobbie(hobbies)


@then("save the data")
def send_data(browser):
    FormDemoqaPage(browser).send_data_form()


@when("I create a new tab")
def new_tab_click(browser):
    WindowsDemoqaPage(browser).select_new_tab()


@then(parsers.parse('the system shows the new tab with the message "{message}"'))
def validate_new_tab(browser, message):
    browser.implicitly_wait(10)
    WindowsDemoqaPage(browser).new_tab_validation(message)


@then(parsers.parse('The system shows the new dialog with the message "{message}"'))
def validate_small_modal(browser, message):
    ModalsDemoqaPage(browser).show_small_modal_and_validate(message)


@when(parsers.parse('I fill the form with "{username}", "{password}"'))
def login(browser, username, password):
    LoginDemoqaPage(browser).send_login_information(username, password)


@then(parsers.parse('The system shows an error message "{message}"'))
def validate_error_login(browser, message):
    LoginDemoqaPage(browser).invalidate_login(message)


@then(parsers.parse('I show the profile of user, with the "{username}"'))
def validate_username_profile(browser, username):
    ProfileDemoqaPage(browser).validate_username_field(username)


@then("logout account")
def logout_account(browser):
    ProfileDemoqaPage(browser).logout_user()


@then(parsers.parse('I select the book "{name_book}"'))
@then('I select the book <name_book>')
def select_book(browser, name_book):
    BooksDemoqaPage(browser).select_book(name_book)


@then("I show the information of the book")
def show_book_information(browser):
    BooksDemoqaPage(browser).information_book()


@then("Add to the collection")
def add_book(browser):
    BooksDemoqaPage(browser).add_book()


@then("I show the list of the books associated to the account")
def validate_list_book_of_user(browser):
    ProfileDemoqaPage(browser).validate_list_books()


@then("I delete the book")
def delete_browser():
    ProfileDemoqaPage(browser).delete_book()


@given('I search ".."')
def step_impl():
    raise NotImplementedError(u'STEP: And I search ".."')


@then("I show the list of the books that concord with the search")
def step_impl():
    raise NotImplementedError(u'STEP: Then I show the list of the books that concord with the search')

