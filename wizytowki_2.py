from faker import Faker
fake = Faker(['pl_PL'])

class Card:
    def __init__(self, first_name, last_name, company_name, position, e_mail):
      self.first_name = first_name
      self.last_name = last_name
      self.company_name = company_name
      self.position = position
      self.e_mail = e_mail
      self.lenght = int(len(first_name)) + int(len(last_name)) + 1

    def __str__(self):
      return f'{self.first_name} {self.last_name} {self.e_mail}'
    def contact(self):
        self.first_name
        self.last_name
        self.e_mail
        print (f'Skonktaktuj się z {self.first_name} {self.last_name} {self.e_mail}')
    @property
    def lenght(self):
        return self.lenght
    @lenght.setter
    def lenght(self, value):
       value = int(len(self.first_name)) + int(len(self.last_name)) + 1
       self.lenght = value

person_1 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company_name=fake.company(), position=fake.job(), e_mail=fake.email())
person_2 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company_name=fake.company(), position=fake.job(), e_mail=fake.email())
person_3 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company_name=fake.company(), position=fake.job(), e_mail=fake.email())
person_4 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company_name=fake.company(), position=fake.job(), e_mail=fake.email())
person_5 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company_name=fake.company(), position=fake.job(), e_mail=fake.email())



