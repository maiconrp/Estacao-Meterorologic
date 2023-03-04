from flet import NavigationBar, NavigationDestination, icons
import flet as ft
from flet import *

class NavigationBarTemplate:
    """
    Classe para criar uma barra de navegação com configurações comuns
    
    Atributos:
        ATRIBUTO       TIPO                            DEFINIÇÃO
        destinations   (List[NavigationDestination])   lista de destinos de navegação
    """

    def __init__(self, destinations, bgcolor='#FFFFFF', width=390, height=70, border_radius=10):
        self.destinations = destinations
        self.bgcolor = bgcolor
        self.width = width
        self.height = height
        self.border_radius = border_radius

    def build(self):
        """
        Cria um objeto <NavigationBar> com as configurações especificadas no construtor
        
        Retorna: NavigationBar: barra de navegação criada
        """
        return ft.NavigationBar(
            destinations=self.destinations,
            bgcolor = self.bgcolor,
            width = self.width,
            height = self.height,
            #border_radius = self.border_radius
            )
    
destinations = [
    ft.NavigationDestination(Image(src=f"/icons/culture.svg"), label="Cultura"),
    ft.NavigationDestination(Image(src=f"/icons/home.svg"), label="Home"),
    ft.NavigationDestination(icon=(ft.Image(src=f"/icons/icon.png")), label="Perfil"),
]

navigation_bar = NavigationBarTemplate(
    destinations,
    bgcolor = 'white',
    border_radius = border_radius.only(bottomLeft=15, bottomRight=15)
    ).build()
