import flet as ft
import os
from views.playGame import playContent, selectedVersion, selectedName, runPlay
from views.settinsGame import settinsContent, optionVersion, typeVersion, runProces, progresBar
from views.Buttons import nab, button_play, button_settins, button_folder
from controlles.gameOptions import MINECRAFT_DIRECTORY,selectionVersion, installedList, runMinecraft, valoreNulos, installedVersion,installVersion

def main(page: ft.Page):

    def openPlay(e):
        listaVersiones()
        page.remove_at(0) if page.controls != [] else False
        indexar(playContent)

    def opensettins(e):
        optionVersion.options=[]
        typeVersion.options=[]
        page.remove_at(0) if page.controls != [] else False
        indexar(settinsContent)

    def openFolder(e):
        os.startfile(MINECRAFT_DIRECTORY)

    def listaVersiones():
        selectedVersion.options = []
        for i in installedList():
            selectedVersion.options.append(ft.dropdown.Option(i))
           
    def iniciarJuego(e):
        userName = selectedName.value
        version = selectedVersion.value
        runMinecraft(version, userName)

    def escogiendoTipo(e):
        optionVersion.options=[]
        typeVersion = selectionVersion(e.data)
        if isinstance(typeVersion, list):
            for i in typeVersion:
                optionVersion.options.append(ft.dropdown.Option(i))   
            page.update()
    
    def instalarVersion(e):
        if valoreNulos(optionVersion.value):
            if installedVersion(optionVersion.value):
                progresBar.value = "instalando..."
                page.update()
                progresBar.value = installVersion(optionVersion.value, typeVersion.value)
                page.update()
            else: 
                progresBar.value = "version ya existente"
                page.update()

    def indexar(paguinaPrincipal):
        page.add(
            ft.Row(
                [
                    nab,
                    paguinaPrincipal
                ],
            )
        )

    page.title = "XLauncher",
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False
    page.window.maximizable = False
    runPlay.on_click=iniciarJuego
    typeVersion.on_change=escogiendoTipo
    button_play.on_click=openPlay
    button_settins.on_click=opensettins
    runProces.on_click = instalarVersion
    button_folder.on_click=openFolder
    listaVersiones()

    indexar(playContent)
    
ft.app(main)