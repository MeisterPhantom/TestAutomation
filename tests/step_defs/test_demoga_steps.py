from pytest_bdd import scenarios, given, when, then, parsers
from configurations.conftest import *
# from tests.step_defs.conftest import *
from src.pages.Login.login_demoga_page import LoginDemogaPage
from src.pages.home.home_demoga_page import HomeDemogaPage
from src.pages.modals.modals_demoga_page import ModalsDemogaPage
from src.pages.modules.modules_demoga_page import ModulesDemogaPage
from src.pages.textbox.textbox_demoga_page import TextBoxPage
from src.pages.updownload.updownload_demoga_page import UpDownLoadPage
from src.pages.windows.windows_demoga_page import WindowsDemogaPage
from src.pages.form.form_demoqa_page import FormDemogaPage

scenarios('../features/test_demoga.feature')


@given("the demoga page is displayed")
def home_demoga():
    HomeDemogaPage(browser)


@when(parsers.parse('I select the section "{section}"'))
def select_section(browser, section):
    browser.implicitly_wait(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    HomeDemogaPage(browser).select_section_option(section)


@when(parsers.parse('I select the option "{option}"'))
@when('I select the option "<option>"')
def select_option(browser, option):
    browser.implicitly_wait(5)
    ModulesDemogaPage(browser).select_list_option(option)


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


@then(parsers.parse('I fill the form with "{first_name}", "{last_name}", "{email}", "{mobile}", "{date_of_birth}", "{subjects}", and "{current_address}"'))
def fill_form(browser, first_name, last_name, email, mobile, date_of_birth, subjects, current_address):
    FormDemogaPage(browser).send_field_information(first_name, last_name, mobile, date_of_birth, subjects,
                                                   current_address)


@then(parsers.parse('I select the option gender "{gender}"'))
def select_gender(browser, gender):
    FormDemogaPage(browser).select_gender(gender)


@then(parsers.parse('I select the option hobbies "{hobbies}"'))
def select_hobbies(browser, hobbies):
    FormDemogaPage(browser).select_hobbie(hobbies)


@then("save the data")
def send_data(browser):
    FormDemogaPage(browser).send_data_form()


@when("I create a new tab")
def new_tab_click(browser):
    WindowsDemogaPage(browser).select_new_tab()


@then(parsers.parse('the system shows the new tab with the message "{message}"'))
def validate_new_tab(browser, message):
    browser.implicitly_wait(10)
    WindowsDemogaPage(browser).new_tab_validation(message)


@then(parsers.parse('The system shows the new dialog with the message "{message}"'))
def validate_small_modal(browser, message):
    ModalsDemogaPage(browser).show_small_modal_and_validate(message)


@when(parsers.parse('I fill the form with "{username}", "{password}"'))
def login(browser, username, password):
    LoginDemogaPage(browser).send_login_information(username, password)


@then(parsers.parse('The system shows an error message "{message}"'))
def validate_error_login(browser, message):
    LoginDemogaPage(browser).invalidate_login(message)
