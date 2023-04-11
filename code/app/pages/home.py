import flet as ft
from componentes.NavigationBar import navigation_bar
from componentes.AppBar import appbar
from componentes.botões.ElevatedButton import HomeButton
from componentes.Container import *
from componentes.Card import *
from componentes.Graficos import grafico_temperatura, grafico_Etc, grafico_umidade, grafico_vento, grafico_radiacao
from componentes.Clima import temperatura, vento, umidade, pressao, radiacao


class HomePage:
    def build():
        return ft.View(
            "/",
            [
                Column(
                    controls=[
                        card_cultura,
                        line,
                        relatorio,
                        Row(
                            controls=[
                                Card(card_irrigacao, elevation=6),
                                Card(card_economia, elevation=6),
                            ],
                            alignment="center",
                        ),
                        Card(card_ET, elevation=6),
                        clima,
                        Card(temperatura, elevation=8),
                        Card(umidade, elevation=8),
                        Card(vento, elevation=8),
                        Card(pressao, elevation=8),
                        Card(radiacao, elevation=4),
                        dashboard,
                        grafico_Etc,
                        grafico_temperatura,
                        grafico_umidade,
                        grafico_radiacao,
                        grafico_vento,
                    ],
                    horizontal_alignment="center",
                ),
                navigation_bar,
            ],
            scroll="auto",
            appbar=appbar,
            horizontal_alignment="center",
        )
