from modules.pages.google_search import GoogleSearchPage
from tests.assertions import *
from configurations.conftest import *
import pytest


@pytest.mark.parametrize(
    "search",
    ["Simetrik"]
)
def test_google_search(browser, search):
    google = GoogleSearchPage(browser)
    google.send_search(search)
    assert_quantity_results(google.validate_result())
