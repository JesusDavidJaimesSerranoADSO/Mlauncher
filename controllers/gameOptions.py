import subprocess
import time
import minecraft_launcher_lib as mc
from flet import dropdown 
from views.playView import PlayPanel
from views.settinsView import SettingsPanel
from controllers.config import GameConfig


class GameOptionsController:

    def __init__(self):
        self.config =  GameConfig()

    def prepareRun(self):
        PlayPanel.selectedVersion.options.clear()
        for i in mc.utils.get_installed_versions(self.config.MINECRAFT_DIRECTORY): 
            PlayPanel.selectedVersion.options.append(dropdown.Option(i['id']))
        self.config.readCache()
        PlayPanel.selectedName.value = self.config.USERNAME
        PlayPanel.selectedVersion.value = self.config.VERSION

    def runGame(self):
        self.config.USERNAME = PlayPanel.selectedName.value
        self.config.VERSION = PlayPanel.selectedVersion.value
        self.config.SVERSION = PlayPanel.selectedVersion.value
        self.config.writeCache()
        self.config.getProfile()
        if mc.utils.is_version_valid(self.config.VERSION,self.config.MINECRAFT_DIRECTORY):
            minecraft_command = mc.command.get_minecraft_command(
                self.config.VERSION, self.config.MINECRAFT_DIRECTORY, self.config.get_settings)
            subprocess.run(minecraft_command, creationflags=subprocess.CREATE_NO_WINDOW)

    def prepareSettings(self):
        self.config.SVERSION = self.nmlVersion(self.config.VERSION)
        self.config.getProfile()
        SettingsPanel.sv.options.clear()
        for i in mc.utils.get_installed_versions(self.config.MINECRAFT_DIRECTORY): 
            SettingsPanel.sv.options.append(dropdown.Option(i['id']))
        SettingsPanel.sv.value = self.config.VERSION
        SettingsPanel.jpo.value = self.config.RUTA_JAVA
        SettingsPanel.jao.value = self.config.ARGUMENTO_RAM

    def versionSettings(self):
        self.config.SVERSION = self.nmlVersion(SettingsPanel.sv.value)
        self.config.getProfile()
        SettingsPanel.sv.options.clear()
        for i in mc.utils.get_installed_versions(self.config.MINECRAFT_DIRECTORY): 
            SettingsPanel.sv.options.append(dropdown.Option(i['id']))
        SettingsPanel.jpo.value = self.config.RUTA_JAVA
        SettingsPanel.jao.value = self.config.ARGUMENTO_RAM

    def saveSettings(self):
        self.config.SVERSION = self.nmlVersion(SettingsPanel.sv.value)
        self.config.RUTA_JAVA = SettingsPanel.jpo.value
        self.config.ARGUMENTO_RAM = SettingsPanel.jao.value
        self.config.updateProfile()
        self.versionSettings()

    def selectedType(self):
        SettingsPanel.optionVersion.options.clear()
        SettingsPanel.optionVersion.value = ""
        tv = SettingsPanel.typeVersion.value
        if tv == "Vanilla": 
            for i in mc.utils.get_version_list():
                SettingsPanel.optionVersion.options.append(dropdown.Option(i['id']))
        elif tv == "Forge":
            for i in mc.forge.list_forge_versions():
                SettingsPanel.optionVersion.options.append(dropdown.Option(i))
        elif tv == "Fabric":
            return []
        
    def installVersion(self):
        vs = SettingsPanel.optionVersion.value
        tv = SettingsPanel.typeVersion.value
        try:
            if tv == "Vanilla":
                if mc.utils.is_vanilla_version(vs):
                    self.config.USERNAME = PlayPanel.selectedName.value
                    self.config.SVERSION = SettingsPanel.optionVersion.value
                    self.config.VERSIONTYPE = SettingsPanel.typeVersion.value
                    mc.install.install_minecraft_version(vs, self.config.MINECRAFT_DIRECTORY)
                    self.config.createProfile()
            elif tv == "Forge":
                if mc.forge.is_forge_version_valid(vs):
                    self.config.USERNAME = PlayPanel.selectedName.value
                    self.config.SVERSION = SettingsPanel.typeVersion.value
                    self.config.VERSIONTYPE = SettingsPanel.typeVersion.value
                    mc.forge.install_forge_version(vs, self.config.MINECRAFT_DIRECTORY)
                    self.config.createProfile()
            SettingsPanel.progresBar.value =  "version ya instalada"
        except:
            SettingsPanel.progresBar.value =  "error de descargar "   
    
    def nmlVersion(self,full_id: str) -> str:
        parts = full_id.split('-')
        if len(parts) >= 3:
            return f"{parts[0]}-{parts[-1]}"
        return full_id
    
    def valVersion(self, a):
        r = True
        for i in mc.utils.get_installed_versions(self.config.MINECRAFT_DIRECTORY):
            vc = self.nmlVersion(i["id"])
            if a == vc : r = False
            if a == "" or a == None or a == "None" : r = False
        return r


  

        

