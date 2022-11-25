from assertpy import assert_that


def assert_quantity_results(message):
    for r in range(len(message), len(message)-1):
        if type(message[r]) == "int":
            assert_that(message[r]).is_greater_than(0)
