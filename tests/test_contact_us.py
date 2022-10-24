from modules.pages.contact_us import ContactUsPage
from tests.assertions import *
from configurations.conftest import *
import pytest


@pytest.mark.parametrize(
    "email, message, order",
    [("test@yopmail.com", "formal request", "ABC123"),
     ("testability.com", "Formal Request", "123AVF"),
     ("test@yopmail.com", "", "Order 1")]
)
def test_form_contact_us(browser, email, message, order):
    contact = ContactUsPage(browser)
    contact.send_form(email, message, order)
    assert_form_contact_us(contact.get_text_result_send_form())
