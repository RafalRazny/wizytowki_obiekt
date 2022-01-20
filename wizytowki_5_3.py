from faker import Faker
fake = Faker(['pl_PL'])

class BaseContact:
  def __init__(self, first_name, last_name, phone_number, e_mail):
      self.first_name = first_name
      self.last_name = last_name
      self.phone_number = phone_number
      self.e_mail = e_mail
  def __str__(self):
      return f'{self.phone_number} {self.first_name} {self.last_name}'
  def contact(self):
      self.phone_number
      self.first_name
      self.last_name
      print (f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}')
  @property
  def label_length(self):
      return int(len(self.first_name)) + int(len(self.last_name))

class BusinessContact(BaseContact):
    def __init__(self, position, company_name, company_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.company_number = company_number
    def __str__ (self):
        return f'{self.company_number} {self.first_name} {self.last_name}'
    def contact(self):
        self.company_number
        self.first_name
        self.last_name
        print (f'Wynieram numer {self.company_name} i dzwonię do {self.first_name} {self.last_name}')
    @property
    def label_length(self):
        return int(len(self.first_name)) + int(len(self.last_name))

def create_contacts (amount, a):
    if a == BaseContact:
        for i in range(amount):
            i = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), e_mail=fake.email())
            print(i)
    elif a == BusinessContact:
        for z in range(amount):
            z = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company_number=fake.phone_number(), e_mail=fake.email(), position=fake.job(), company_name=fake.company(), phone_number=fake.phone_number())
            print(z)


    
print(create_contacts(4, BusinessContact))