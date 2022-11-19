from modules.pages.contact_us import ContactUsPage
from tests.assertions import *
from configurations.conftest import *
import pytest


@pytest.mark.parametrize(
    "search, assertion",
    [("Outsource", "What not to do when working with an outsourced software team")]
)
def test_form_contact_us(browser, search, assertion):
    contact = ContactUsPage(browser)
    contact.send_search_and_validate(search)
    print(contact.validate_result())
    assert_list_result(contact.validate_result(), assertion)
