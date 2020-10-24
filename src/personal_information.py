class PersonalInformation:

    def __init__(self, first_name, last_name, identification_number):
        self.first_name = first_name
        self.last_name = last_name
        self.identification_number = identification_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_identification_number(self):
        return self.identification_number
