class Password:

    def __init__(self,password):
        self.__password = password
    def get_password(self, isAuth):
        if isAuth:
            return self.__password
        else:
            print("error")

    def set__password(self,password):
        if len(password) > 10:
            self.__password = password
        else:
            print("weak password")

    def print_len(self):
        print("your password len is", len(self.__password))

pwd = Password(1235)
pwd1 = Password("biotech")


pwd.print_len()

passd= pwd.get_password(False)
print(passd)

pwd.set_password("yyp1256")
pwd.print_len()