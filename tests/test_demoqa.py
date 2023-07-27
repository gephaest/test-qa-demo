import datetime

from allure_commons.types import Severity

from demoqa.data.users import User
from demoqa.pages.registration_page import RegistrationPage
import allure


@allure.title('Successful fill registration form')
@allure.tag("WEB")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Anna Malinovskaia")
@allure.feature("Регистрационная форма студента")
@allure.story("Пользователь может зарегестрироваться")
def test_registration_user(setup_browser):
    registration_page = RegistrationPage(browser=setup_browser)

    anna = User(
        first_name='Anna',
        last_name='Malinovskaia',
        email='tests@demoqa.com',
        gender='Other',
        mobile='9115678907',
        date_of_birth=datetime.date(1989, 1, 11),
        hobbies='Reading',
        subjects='Maths',
        picture='kotik.jpeg',
        address='Russia, Moscow, str.Testers',
        state='NCR',
        city='Delhi'
    )

    with allure.step('Open registration form'):
        registration_page.open()

    with allure.step('Fill registration form'):
        registration_page.register(anna)

    with allure.step('Check results'):
        registration_page.should_have_registred(anna)
