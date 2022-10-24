from assertpy import assert_that


def assert_form_contact_us(message):
    assert_that(message).is_equal_to("Your message has been successfully sent to our team.")
