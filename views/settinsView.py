from typing import List
import flet as ft

class SettingsPanel(ft.Container):
    typeVersion = ft.Dropdown(
        label="elegir clase",
        options=[
            ft.dropdown.Option("Vanilla"),
            ft.dropdown.Option("Forge"),
        ],
        width=180, bgcolor="#f7f5f5",
    )

    optionVersion = ft.Dropdown(label="elegir versoin", width=210, bgcolor="#f7f5f5",)

    runProces = ft.FilledButton(text="Instalar Version", width=130, bgcolor = "#73b851")

    progresBar = ft.Text("")

    #------------------------------------------------------
    sv = ft.Dropdown(width= 250, bgcolor="#f7f5f5")
    versionSelected = ft.Row([ft.Text("version modificada:", width=400, text_align="left"), sv ])

    jpo = ft.TextField(hint_text="", width=570, bgcolor="#f7f5f5")
    javaPathOption = ft.Row([ft.Text("java Path:", width=80, text_align="left"), jpo ])

    jao = ft.TextField(hint_text="", width=570, bgcolor="#f7f5f5")
    javaArgOption = ft.Row([ft.Text("java Arg:", width=80, text_align="left"), jao ])

    saveProces = ft.FilledButton(
        text="Guardar", width=140, bgcolor = "#73b851",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
    )

    def __init__(self):


        rdownloadControls = ft.Row(
            controls=[self.typeVersion, self.optionVersion, self.runProces, self.progresBar],
            alignment=ft.MainAxisAlignment.START
        )

        #------------------------------------------------------
        
        optionsControl = ft.Container(
            content=ft.Column(
                controls=[self.versionSelected, self.javaPathOption, self.javaArgOption, self.saveProces],
            ),
            padding=10,
            bgcolor="#cacaca"
        )

        main_column = ft.Column(controls=[rdownloadControls, optionsControl],spacing=50)

        super().__init__(
            content=main_column, height=600, width=720, bgcolor="#588bc7", padding=20
        )
        
        


