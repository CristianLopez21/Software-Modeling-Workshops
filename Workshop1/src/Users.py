"""This module has class definition of the Users that acces to the store system and their functionalities  

Author: Cristian Santiago Lopez Cadena <crslopezc@udistrital.edu.co>

This file is part of ArcadeMachine store project.

ArcadeMachine store project. is free software: you can redistribute it and/or modify it under the terms of 
the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

ArcadeMachine store project. is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ArcadeMachine store project. 
If not, see <https://www.gnu.org/licenses/>.

"""

customers = {}
admins = {}

class User:
    """This class is the abstraction of the user that access to the store system
    
    Constructor class: User
    Attributes:
        username: str
        password: str
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @staticmethod
    def CreateAccount():
        """This method creates a new user account depending on the role"""
        role = input("Enter your role 1.customer  2.admin: ")
        if role == "1":
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            firstname = None
            lastname = None
            addres = None
            addres2 = None
            country = None
            city = None
            postalcode = None
            phonenum = None
            customer = Customer(
                firstname,
                lastname,
                addres,
                addres2,
                country,
                city,
                postalcode,
                phonenum,
                username,
                password,
            )
            customers[username] = customer.__dict__

            print("Customer successfully created: ")

        elif role == "2":
            access = input("Please enter the password to create a admin user: ")
            if access == "admin":
                username = input("Please enter your username: ")
                password = input("Please enter your password: ")
                admin = Admin(username, password)
                admins[username] = admin.__dict__
                
                print(f"Admin successfully created")
            else:
                print("Invalid passwor, you cant create a admin user")


class Customer(User):
    """This class is the concrete class of the customer that access to the store system
    
    Constructor class: Customer
    Attributes:
        firstname: str
        lastname: str
        addres: str
        addres2: str
        country: str
        city: str
        postalcode: str
        phonenum: str
    """

    def __init__(
        self,
        firstname: str,
        lastname: str,
        addres: str,
        addres2: str,
        country: str,
        city: str,
        postalcode: str,
        phonenum: str,
        username: str,
        password: str,
    ):
        super().__init__(username, password)
        self.firstname = firstname
        self.lastname = lastname
        self.addres = addres
        self.addres2 = addres2
        self.country = country
        self.city = city
        self.postalcode = postalcode
        self.phonenum = phonenum

    def add_shipinginformation(username):
        """This method allows the customer to add shipping information
        
        Args:
            username: str
        """ 
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        addres = input("Enter your address: ")
        addres2 = input("(Apartment, suite, unit: ")
        country = input("Enter your country: ")
        city = input("Enter your city: ")
        postalcode = input("Enter your postal code: ")
        phonenum = input("Enter your phone number: ")
        customers[username]['firstname'] = firstname
        customers[username]['lastname'] = lastname
        customers[username]['addres'] = addres
        customers[username]['addres2'] = addres2
        customers[username]['country'] = country
        customers[username]['city'] = city
        customers[username]['postalcode'] = postalcode
        customers[username]['phonenum'] = phonenum

        print("Shipping information successfully added")


class Admin(User):
    """This class is the concrete class of the admin that access to the store system 
    
    Constructor class: Admin
    Attributes:
        grants: bool
    """

    def __init__(self, username: str, password: str):
        super().__init__(username, password)
        self.grants = True
