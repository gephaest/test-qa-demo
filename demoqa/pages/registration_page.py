from selene import have, be
from demoqa.data.users import User
from demoqa.pages import resources


class RegistrationPage:

    def __init__(self, browser):
        self.b = browser

        self.registered_user_data = self.b.element('.table').all('td')
        self.first_name = self.b.element('#firstName')
        self.last_name = self.b.element('#lastName')
        self.email = self.b.element('#userEmail')
        self.gender = self.b.all('#genterWrapper label')
        self.mobile = self.b.element('#userNumber')
        self.subjects = self.b.element('#subjectsInput')
        self.hobbies = self.b.all('#hobbiesWrapper label')
        self.picture = self.b.element('#uploadPicture')
        self.address = self.b.element('#currentAddress')
        self.submit = self.b.element('#submit')

    def open(self):
        self.b
        self.b.open('https://demoqa.com/automation-practice-form/')
        self.b.driver.execute_script("$('footer').remove()")
        self.b.driver.execute_script("$('#fixedban').remove()")

    def register(self, anna: User):
        self.first_name.type(anna.first_name)
        self.last_name.type(anna.last_name)
        self.email.type(anna.email)
        self.gender.element_by(have.exact_text(anna.gender)).click()
        self.mobile.type(anna.mobile)
        self.fill_date_of_birth(anna.date_of_birth)
        self.subjects.type(anna.subjects).press_enter()
        self.hobbies.element_by(have.text(anna.hobbies)).click()
        self.picture.set_value(resources.path(anna.picture))
        self.address.type(anna.address)
        self.fill_state(anna.state)
        self.fill_city(anna.city)
        self.submit.click()
        return self

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        self.b.element('#dateOfBirthInput').click()
        self.b.element('.react-datepicker__year-select').click()
        self.b.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        self.b.element('.react-datepicker__month-select').click()
        self.b.element(f'.react-datepicker__month-select option[value="{month}"]').click()
        self.b.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_state(self, value):
        self.b.element('#state').click()
        self.b.all("#state div").element_by(have.exact_text(value)).click()
        return self

    def fill_city(self, value):
        self.b.element('#city').click()
        self.b.all("#city div").element_by(have.exact_text(value)).click()
        return self

    def should_have_registred(self, anna: User):
        self.b.element('.table').all('td').even.should(have.exact_texts(
            f'{anna.first_name} {anna.last_name}',
            f'{anna.email}',
            f'{anna.gender}',
            f'{anna.mobile}',
            '{0} {1},{2}'.format(anna.date_of_birth.strftime("%d"),
                                 anna.date_of_birth.strftime("%B"),
                                 anna.date_of_birth.year),
            f'{anna.subjects}',
            f'{anna.hobbies}',
            f'{anna.picture}',
            f'{anna.address}',
            f'{anna.state} {anna.city}'
        ))

        self.b.element('#closeLargeModal').click()
        self.b.element('#firstName').should(be.blank)
