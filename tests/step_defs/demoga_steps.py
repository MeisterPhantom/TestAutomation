from pytest_bdd import scenarios, given, when, then, parsers
from configurations.conftest import *
from src.pages.Login.login_demoga_page import LoginDemogaPage
from src.pages.home.home_demoga_page import HomeDemogaPage
from src.pages.modals.modals_demoga_page import ModalsDemogaPage
from src.pages.modules.modules_demoga_page import ModulesDemogaPage
from src.pages.textbox.textbox_demoga_page import TextBoxPage
from src.pages.updownload.updownload_demoga_page import UpDownLoadPage
from src.pages.windows.windows_demoga_page import WindowsDemogaPage

scenarios('../features/demoga.feature')


@given("the demoga page is displayed")
def home_demoga():
    HomeDemogaPage(browser)


@when(parsers.parse('I select the section "{section}"'))
def select_section(browser, section):
    HomeDemogaPage(browser).select_section_option(section)


@given('I select the option "<option>"')
def select_option(browser, option):
    ModulesDemogaPage(browser).select_list_option(option)


@then('I fill the form with "<full_name>", "<email>", "<current_address>" and "<permanent_address>"')
def fill_textbox_form(browser, full_name, email, current_address, permanent_address):
    TextBoxPage(browser).fill_form(full_name, email, current_address, permanent_address)


@given("send the information")
def send_textbox_form_information(browser):
    TextBoxPage(browser).send_information_form()


@then('I download the file')
def download_action(browser):
    UpDownLoadPage(browser).click_download()


@given('I select the option gender "<gender>"')
def step_impl():
    raise NotImplementedError(u'STEP: And I select the option gender "<gender>"')


@given('I select the option hobbies "<hobbies>"')
def step_impl():
    raise NotImplementedError(u'STEP: And I select the option hobbies "<hobbies>"')


@given('I select the state and city "<state>", "<city>"')
def step_impl():
    raise NotImplementedError(u'STEP: And I select the state and city "<state>", "<city>"')


@given("upload the photo")
def step_impl():
    raise NotImplementedError(u'STEP: And upload the photo')


@given("save the data")
def step_impl():
    raise NotImplementedError(u'STEP: And save the data')


@given("I create a new tab")
def new_tab_click(browser):
    WindowsDemogaPage(browser).select_new_tab()


@then(parsers.parse('The system show the new tab with the message "{message}"'))
def validate_new_tab(browser, message):
    WindowsDemogaPage(browser).new_tab_validation(message)


@then(parsers.parse('The system show the new dialog with the message "{message}"'))
def validate_small_modal(browser, message):
    ModalsDemogaPage(browser).show_small_modal_and_validate(message)


@given('I fill the form with "<username>" , "<password>"')
def login(browser, username, password):
    LoginDemogaPage(browser).send_login_information(username, password)


@then(parsers.parse('The system show a error message "{message}"'))
def validate_error_login(browser, message):
    LoginDemogaPage(browser).invalidate_login(message)
