from django.contrib.auth import get_user_model


class Check_Data():

    def __init__(self):
        check = self

    def exist_user(self, username):
        User = get_user_model()
        users = User.objects
        print(username)

        response = users.filter(username=username).exists()
        return(response)

    def match_passwords(self, password1, password2):
        return password1 == password2
