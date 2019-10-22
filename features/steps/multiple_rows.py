from behave import *

from pages.rows_page import RowsPage


@when("I add users for the table")
def i_add_users_for_the_table(context):
    rows_page = RowsPage(context.behave_driver)
    rows_page.switch_to_iframe()

    for row in context.table:
        rows_page.enter_user(row['name'], row['mail'], row['phone'])
        rows_page.add_row()

    print ('add breakpoint here')


@when('I add user with name "{name}", surname "{surname}" and phone "{phone}"')
def step_impl(context, name, surname, phone):
    pass
