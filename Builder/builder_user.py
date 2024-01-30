from abc import ABC, abstractmethod

class User:
    def __init__(self):
        self.__first_name = None
        self.__last_name = None
        self.__age = None
        self.__phone_number = None
        self.__address = None
        self.__email_address = None

    @property
    def firstName(self):
        return self.__first_name
    @property
    def lastName(self):
        return self.__last_name
    @property
    def age(self):
        return self.__age
    @property
    def phoneNumber(self):
        return self.__phone_number
    @property
    def address(self):
        return self.__address
    @property
    def emailAddress(self):
        return self.__email_address
    
class AbstractUserBuilder(ABC):
    @abstractmethod
    def set_firstName(self):
        pass
    @abstractmethod
    def set_lastName(self):
        pass
    @abstractmethod
    def set_age(self):
        pass
    @abstractmethod
    def set_phoneNumber(self):
        pass
    @abstractmethod
    def set_address(self):
        pass
    @abstractmethod
    def set_emailAddress(self):
        pass

class UserBuilder(AbstractUserBuilder):
    def __init__(self):
        self.user = User()
    def set_firstName(self, firstName=None):
        if not firstName:
            raise ValueError("First Name is required*")
        self.user._User__first_name = firstName
    def set_lastName(self, lastName=None):
        if not lastName:
            raise ValueError("Last Name is required")
        self.user._User__last_name = lastName
    def set_emailAddress(self, emailAddress=None):
        if not emailAddress:
            raise ValueError("Email Address is required*")
        self.user._User__email_address = emailAddress
    def set_age(self, age=None):
        self.user._User__age = age
    def set_address(self, address=None):
        self.user._User__address = address
    def set_phoneNumber(self, phoneNumber=None):
        self.user._User__phone_number = phoneNumber

class UserDirector:
    def __init__(self, builder=None):
        self.builder = builder
    def build_user(self, context):
        self.builder.set_firstName(context.firstName)
        self.builder.set_lastName(context.lastName)
        self.builder.set_emailAddress(context.emailAddress)
        self.builder.set_age(context.age)
        self.builder.set_address(context.address)
        self.builder.set_phoneNumber(context.phoneNumber)

class UserContext:
    def __init__(self, firstName=None, lastName=None, emailAddress=None, 
                 age=None, address=None, phoneNumber=None):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.age = age
        self.address = address
        self.phoneNumber = phoneNumber

director = UserDirector()

users = {
    'user1': {'firstName': 'abc',
              'lastName': 'def',
              'emailAddress': 'ghi@jkl.com',
              'age': 1,
              'address': 'xyz',
              'phoneNumber': '1234'},
    'user2': {'firstName': 'jhon',
              'lastName': 'doe',
              'emailAddress': 'jhon@doe.com'},
    'user3': {
              'firstName': 'siva',
              'lastName': 'prakash'}
    
}

for user in users:
    try:
        builder = UserBuilder()
        director.builder = builder
        user_context = UserContext(**users[user])
        director.build_user(user_context)
        user = builder.user
        print(f"first name: {user.firstName}")
        print(f"last name: {user.lastName}")
        print(f"email address: {user.emailAddress}")
        print(f"age: {user.age}")
        print(f"address: {user.address}")
        print(f"phone number: {user.phoneNumber}")
        print("****************************************")
    except ValueError as e:
        print(f"for {user}: {e}")

    


        
        
        
        
        
        

