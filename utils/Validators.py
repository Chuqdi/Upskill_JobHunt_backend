from django.core.validators import EmailValidator, RegexValidator, URLValidator



class Validate():
    @staticmethod
    def validateEmail(email):
        try:
            EmailValidator()(email)
            return True
        except Exception as e:
            return False

    @staticmethod     
    def validateUrl(url):
        regex = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        try:
            URLValidator()(url)
            return True
        except Exception as e:
            return False

