import pytest
from PageModules.Pages.contact_us import ContactUsPage


@pytest.mark.parametrize(
    "email, message, order, subject_type",
    [("test@yopmail.com", "formal request", "ABC123", "Customer service"),
     ("testability.com", "Formal Request", "123AVF", "Customer service"),
     ("test@yopmail.com", "", "Order 1", "Customer service")]
)
def test_form_contact_us(browser, email, message, order, subject_type):
    contact = ContactUsPage(browser)
    contact.send_form(email, message, order, subject_type)
