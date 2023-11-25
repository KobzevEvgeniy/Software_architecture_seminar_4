class Person:
    def __init__(self, fio, card_number, login, hash_pass, email):
        self.id = id
        self.fio = fio
        self.card_number = card_number
        self.login = login
        self.hash_pass = hash_pass
        self.email = email

    def get_fio(self):
        return self.fio

    def get_card_number(self):
        return self.card_number

    def get_login(self):
        return self.login

    def get_hash_pass(self):
        return self.hash_pass

    def det_email(self):
        return self.email

    def set_login(self, new_login):
        self.login = new_login

    def set_hash_pass(self, new_hash_pass):
        self.hash_pass = new_hash_pass

    def set_email(self, new_email):
        self.email = new_email

    def authorization_person(self):
        pass

    def get_info_person(self):
        return f"FIO: {self.fio}\nemail: {self.email}" \
               f"\nlogin:{self.login}" \
               f"\npassword:{self.hash_pass}" \
               f"\ncard:{self.card_number} "
