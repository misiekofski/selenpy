from behave import *

@when("I add users for the table")
def i_add_users_for_the_table(context):
    pass


@when('I add user with name "{name}", surname "{surname}" and phone "{phone}"')
def step_impl(context, name, surname, phone):
    pass
