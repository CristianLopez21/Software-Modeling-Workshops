"""This file contains the main menu of the program and some functionalities of this

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

from Users import User, Customer, customers, admins
from catalog import Catalog


if __name__ == "__main__":

    MENU1 = """
    1. Show Machines
    2. Show Games
    3. Exit
    """
    MENU2 = """
    1. Show Machines
    2. Show Games
    3. Add Machine
    4. Add VideoGame
    5. Exit
    """

    option1 = int(
        input(
            "------------ Welcome to the Arcade Machine Store------------\n 1. Create Account\n 2. Login\n 3. Exit\n"
        )
    )
    while option1 != 3:
        if option1 == 1:
            User.CreateAccount()

        elif option1 == 2:

            username = input("Enter your username: ")
            password_log = input("Enter your password: ")

            if username in customers:
                if customers[username]["password"] == password_log:
                    print(
                        f"_________________Welcome {username} to the ArcadeMachine store_________________"
                    )
                    option2 = int(input(MENU1))
                    while option2 != 3:
                        if option2 == 1:
                            Catalog.show_machines()
                            buy = int(
                                input(
                                    "To buy a machine select\n 1. Purchase.\n 2. Exit\n "
                                )
                            )
                            while buy != 2:
                                if buy == 1:
                                    Catalog.purchase()
                                    if Catalog.purchase() == False:
                                        buy == 2
                                    else:
                                        Customer.add_shipinginformation(username)
                                        print("Your purchase has been completed")
                                else:
                                    print("Invalid option")

                        elif option2 == 2:
                            Catalog.show_videogames()
                        else:
                            print("Invalid option")
                        option2 = int(input(MENU1))
                else:
                    print("Invalid password")

            elif username in admins:
                if admins[username]["password"] == password_log:
                    print(
                        f"_______________Welcome {username} to the ArcadeMachine store_________________"
                    )
                    option2 = int(input(MENU2))
                    while option2 != 5:
                        if option2 == 1:
                            Catalog.show_machines()
                            buy = int(
                                input(
                                    "To buy a machine select\n 1. Purchase.\n 2. Exit\n"
                                )
                            )
                            while buy != 2:
                                if buy == 1:
                                    Catalog.purchase()
                                    Customer.add_shipinginformation(username)
                                    print("Your purchase has been completed")
                                else:
                                    print("Invalid option")
                                buy = int(
                                    input(
                                        "To buy a machine select 1. Purchase.\n 2. Exit"
                                    )
                                )

                        elif option2 == 2:
                            Catalog.show_videogames()
                        elif option2 == 3:
                            Catalog.add_machine()
                        elif option2 == 4:
                            Catalog.add_videogame()
                        else:
                            print("Invalid option")
                        option2 = int(input(MENU2))
                else:
                    print("Invalid password")

        else:
            print("Invalid option")
        option1 = int(
            input(
                "------------ Welcome to the Arcade Machine Store------------\n 1. Create Account\n 2. Login\n 3. Exit\n"
            )
        )
