import flet as ft
import os
from views.playView import PlayPanel
from views.settinsView import SettingsPanel
from views.printipalView import nab, button_play, button_settings, button_folder
from controllers.gameOptions import GameOptionsController
from controllers.config import GameConfig

class LauncherApp:
    def __init__(self):
        self.controller = GameOptionsController()
        self.page: ft.Page = None

    def __call__(self, page: ft.Page):

        self.page = page
        self.page.title = "XLauncher"
        self.page.window.width = 800
        self.page.window.height = 600
        self.page.window.resizable = False
        self.page.window.maximizable = False

        # Eventos
        button_play.on_click = self.open_play
        button_settings.on_click = self.open_settings
        button_folder.on_click = lambda e: os.startfile(GameConfig.MINECRAFT_DIRECTORY)
        PlayPanel.runButton.on_click = self.play
        SettingsPanel.typeVersion.on_change = self.search
        SettingsPanel.runProces.on_click = self.install
        SettingsPanel.sv.on_change = self.asearch
        SettingsPanel.saveProces.on_click = self.save
        #self.page.add(nab)
        # Inicialmente cargo la vista de juego
        self.open_play(None)

    def open_play(self, e):
        self.page.controls.clear()
        self.controller.prepareRun()
        self.page.add(ft.Row([nab, PlayPanel()]))
        self.page.update()

    def open_settings(self, e):
        self.page.controls.clear()
        self.controller.prepareSettings()
        self.page.add(ft.Row([nab, SettingsPanel()]))
        self.page.update()

    def play(self,e): self.controller.runGame()

    def search(self,e): 
        self.controller.selectedType()
        self.page.update()

    def install(self,e):
        if self.controller.valVersion(SettingsPanel.optionVersion.value):
            SettingsPanel.progresBar.value = "instalando..."
            self.page.update()
            self.controller.installVersion()
        else: SettingsPanel.progresBar.value =  "version existente"
        self.page.update()

    def asearch(self,e): 
        self.controller.versionSettings()
        self.page.update()

    def save(self,e): 
        self.controller.saveSettings()
        self.page.update()

def main(page: ft.Page):
    app = LauncherApp()
    page.app = app
    app(page)

if __name__ == "__main__":
    ft.app(target=main)