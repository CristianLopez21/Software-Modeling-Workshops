"""This module has class definition of arcade machine in the store 

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

class ArcadeMachine:
    """This class is abstracction of a arcade machine in the store 

    Constructor class: ArcadeMachine
    Attributes:
        code: str
        material: str
        ledlights: str
        rom: str
        ram: str
        emulator: str
        size: str
        price: str
        color: str
        players: int
        speakers: str
        screen: str
        connectivity: str
        controls: str
        power: str
        weight: str
    """

    def __init__(
        self,
        name: str,
        code: str,
        ledlights: str,
        rom: str,
        ram: str,
        emulator: str,
        size: str,
        price: str,
        color: str,
        players: int,
        speakers: str,
        screen: str,
        connectivity: str,
        controls: str,
        power: str,
        weight: str,
        what_box: str,
        description: str,
    ):
        self.name = name
        self.code = code
        self.ledlights = ledlights
        self.rom = rom
        self.ram = ram
        self.emulator = emulator
        self.size = size
        self.price = price
        self.color = color
        self.players = players
        self.speakers = speakers
        self.screen = screen
        self.connectivity = connectivity
        self.controls = controls
        self.power = power
        self.weight = weight
        self.what_box = what_box
        self.description = description
        self.material = None
