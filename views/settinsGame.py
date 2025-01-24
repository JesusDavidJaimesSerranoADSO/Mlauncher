import flet as ft
from time import sleep

typeVersion = ft.Dropdown(
    label="escoja tipo de versoin",
    #on_change=dropdown_changed,
    options=[
        ft.dropdown.Option("Red"),
        ft.dropdown.Option("Green"),
        ft.dropdown.Option("Blue"),
    ],
    width=300,
    bgcolor="#f7f5f5",
)

optionVersion = ft.Dropdown(
    label="escoja la versoin",
    options=[
        ft.dropdown.Option("Red"),
        ft.dropdown.Option("Green"),
        ft.dropdown.Option("Blue"),
    ],
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

