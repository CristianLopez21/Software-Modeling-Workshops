"""This module has class definition of Video games availables in the store 

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
class Videogame:
    """This class is abstracction of a video game in the store 
    
    Constructor class: Videogame
    Attributes:
        name: str
        code: str
        price: float
        compatibleMachine: str
        difficulty: str
    """
    
    def __init__(
        self,
        name: str,
        code: str,
        price: float,
        compatibleMachine: str,
        difficulty: str,
    ):
        self.name = name
        self.code = code
        self.price = price
        self.compatibleMachine = compatibleMachine
        self.difficulty = difficulty
