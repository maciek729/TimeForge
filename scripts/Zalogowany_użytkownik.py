class zalogowanyUzytkownik:
    _instance = None

    def __init__(self):
        if zalogowanyUzytkownik._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.zalogowany_id = None
            zalogowanyUzytkownik._instance = self

    @staticmethod
    def get_instance():
        if zalogowanyUzytkownik._instance is None:
            zalogowanyUzytkownik()
        return zalogowanyUzytkownik._instance

    def set_zalogowany_id(self, user_id):
        self.zalogowany_id = user_id

    def get_zalogowany_id(self):
        return self.zalogowany_id