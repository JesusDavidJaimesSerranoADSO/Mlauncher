from typing import List
import flet as ft
from controlles.gameOptions import selectionVersion

def escogiendoTipo(e):
    ap=[]
    typeVersion = selectionVersion(e.data)
    if type(typeVersion) == list():
        for i in typeVersion:
            ap.append(ft.dropdown.Option(i))
        optionVersion.options.append(ap)
   

typeVersion = ft.Dropdown(
    label="escoja tipo de versoin",
    on_change=escogiendoTipo,
    options=[
        ft.dropdown.Option("Vanilla"),
        ft.dropdown.Option("Forge"),
        ft.dropdown.Option("Fabric"),
    ],
    width=300,
    bgcolor="#f7f5f5",
)

optionVersion = ft.Dropdown(
    label="escoja la versoin",
    width=300,
    bgcolor="#f7f5f5",
)

runPlay = ft.FilledButton(
    text="Instalar Version",
    bgcolor = "#73b851"
)

progresBar = ft.Text("The Enchanted Nightingale")

settinsContent = ft.Container(
    ft.Column(
        controls=[typeVersion, optionVersion, runPlay, progresBar],
        #alignment=ft.MainAxisAlignment.CENTER,
    ),

    padding=10,
    height=600,
    width=720,
    bgcolor="#588bc7",
    #alignment=ft.alignment.center,
    )

