""" This module has class definition to manage the catalog of arcade machines and videogames

Author: Cristian Santiago Lopez Cadena <crslopezc@udistrital.edu.co>

This file is part of ArcadeMachine store project.

ArcadeMachine store project. is free software: you can redistribute it and/or modify it under the terms of 
the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

ArcadeMachine store project. is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ArcadeMachine store project. 
If not, see <https://www.gnu.org/licenses/>."""


from machine import ArcadeMachine
from videogame import Videogame
from Users import Customer

# Global dictionary to store arcade machines
arcade_machines = {}
videogames = {}


class Catalog:
    """This class is the catalog of the arcade machines and videogames
    
    Constructor class: Catalog
    Attributes:
        id: str
    
    """

    def __init__(self, id: str):
        self.catalogid = id

    @staticmethod
    def show_machines():
        """This method shows the arcade machines available in the store"""
        for machine in arcade_machines.values():
            print(
                f"----------------------{machine['name']}----------------------)\n{machine}\n"
            )

    @staticmethod
    def show_games_available(code):
        """This method shows the videogames available for a specific arcade machine"""
        if arcade_machines[code] == videogames["compatibleMachine"]:
            print(
                f"----------------------{videogames['name']}----------------------)\n{videogames}\n"
            )

    @staticmethod
    def show_videogames():
        """This method shows the videogames available in the store"""
        for videogame in videogames.values():
            print(
                f"----------------------{videogame['name']}----------------------)\n{videogame}\n"
            )

    @staticmethod
    def purchase():
        """This method allows the user to purchase an arcade machine"""
        machinecode = input("Enter the code of the arcade machine that you want to buy: ")
        if machinecode in arcade_machines:
            machine = arcade_machines[machinecode]
            print(
                f"----------------------{machine['name']}----------------------)\n{machine}\n"
            )
            material = input(
                "Select the material of the arcade machine: 1. Wood, 2. Aluminum, 3. Carbon Fiber"
            )
            if material == 1:
                machine["material"] = "Wood"
            elif material == 2:
                machine["material"] = "Aluminum"
            elif material == 3:
                machine["material"] = "Carbon Fiber"
            else:
                print("Invalid option")

            Catalog.show_games_available(machinecode)
            games = input(
                "Select the games that you want purchase for the Arcade Machine enter the code of the game separate for commas: "
            )
            games = games.split(",")

        else:
            print("Arcade Machine not found")
            return False

    @staticmethod
    def add_machine():
        """This method allows the user to add a new arcade machine"""

        name = input("Enter the name of the Arcade machine: ")
        code = input("Enter the code of the Arcade machine: ")
        ledlights = input("The Arcade machine have LED lights: ")
        rom = input("Enter the characteristics of the Arcade machine's hard drive: ")
        ram = input(
            "Enter the characteristics of the Ram memory from the Arcade machine: "
        )
        emulador = input("The arcade machine have an emulator: ")
        size = input(
            "Enter the size, we recommended use the format (Depth(D) x Width(W) x Heigh(H)): "
        )
        price = float(input("Enter the price in a decimal format: "))
        color = input(
            "Enter the color of the Arcade Machine, you can put here if the machine have a custom cover theme: "
        )
        players = int(input("Enter the number of players that can use the machine: "))
        speakers = input("The machine have speakers: ")
        screen = input("Enter information about the screen of the Arcade Machine: ")
        connectivity = input("The machine have internet connectivity: ")
        controls = input("Enter information about the controls of the Arcade Machine: ")
        power = input("Enter the consumption of electricity the arcade machine: ")
        weight = input("Enter the weight of the Arcade Machine: ")
        what_box = input(
            "Enter information about the contents of the box or packaging: "
        )
        description = input(
            "Here you can enter all the information you consider relevant to the arcade machine, such as a description and extra features.: "
        )

        # Creamos una instancia de la clase ArcadeMachine
        arcade_machine = ArcadeMachine(
            name,
            code,
            ledlights,
            rom,
            ram,
            emulador,
            size,
            price,
            color,
            players,
            speakers,
            screen,
            connectivity,
            controls,
            power,
            weight,
            what_box,
            description,
        )

        # Agregamos la nueva máquina
        arcade_machines[code] = arcade_machine.__dict__

        print("Arcade machine saved successfully")

    @staticmethod
    def add_videogame():
        """This method allows the user to add a new videogame"""

        name = input("Enter the name of the videogame: ")
        code = input("Enter the code of the videogame: ")
        price = float(input("Enter the price of the videogame: "))
        compatibleMachine = input(
            "Enter the compatible machines (comma-separated): "
        ).split(",")
        difficulty = input("Enter the difficulty of the videogame: ")

        videogame = Videogame(name, code, price, compatibleMachine, difficulty)
        videogames[code] = videogame.__dict__

        print("Videogame saved successfully")
