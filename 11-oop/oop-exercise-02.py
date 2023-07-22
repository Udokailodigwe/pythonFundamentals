class User:
      def __init__(self, name):
        self.name = name
        self.__password = ""
      @property
      def password(self):
          if len(self.__password) == 0:
            return ""
          secret = self.__password[0]
          for i in range(len(self.__password) - 2):
            secret += "*"
          secret += self.__password[-1]
          return secret


      @password.setter
      def password(self, new_password):
          if len(new_password) < 6:
              for i in range(6 - len(new_password)):
                  new_password += "#"
              self.__password = new_password

      @password.deleter
      def password(self):
          del self.__password

user1 = User("Udoka")
user1.password = "w"
print(user1.password)