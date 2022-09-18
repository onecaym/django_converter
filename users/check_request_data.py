from django.contrib.auth import get_user_model


class Check_Data():

    def __init__(self):
        check = self

    # Check if user with current username already exist. Returns TRUE or FALSE.
    def exist_user(self, username):
        User = get_user_model()
        all_users = User.objects

        response = all_users.filter(username=username).exists()
        return(response)

    # While registration this method checks users passwords match
    def match_passwords(self, password1, password2):
        return password1 == password2
