from pytest_bdd import scenario, given, when, then


@scenario('..//features/google.feature')
@given('the browser has in "google.com"')
def step_impl():
    raise NotImplementedError(u'STEP: Given the browser has in "google.com"')


@when('search "Any word"')
def step_impl():
    raise NotImplementedError(u'STEP: When search "Any word"')


@then("the browser show all results")
def step_impl():
    raise NotImplementedError(u'STEP: Then the browser show all results')


@given("validate the results be maior than zero")
def step_impl():
    raise NotImplementedError(u'STEP: And validate the results be maior than zero')
