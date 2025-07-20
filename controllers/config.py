import json
import os
import ast
import minecraft_launcher_lib as mc

class GameConfig:

    LAUNCHER_VERSION = '1.0.0'
    LAUNCHERNAME = "XLauncher"
    MINECRAFT_DIRECTORY = mc.utils.get_minecraft_directory()
    RUTA_JSON = MINECRAFT_DIRECTORY + "\\launcher_profiles.json"
    RUTA_JAVA = mc.utils.get_java_executable()
    TOKEN = '5998213610:AAHUfeee08ryYWrRhLJ0yI8SL8F0RQu0wKs' 
    USERNAME = None
    VERSION = None
    SVERSION = None
    VERSIONTYPE = None
    ARGUMENTO_RAM = [f"-Xmx{4}G", f"-Xms{4}G"]
    
    @property
    def get_settings(self):
        return {
            "name":            self.USERNAME,
            "version":         self.SVERSION,
            "gameDirectory":   self.MINECRAFT_DIRECTORY,
            "javaExecutable":  self.RUTA_JAVA,
            "javaArguments":   self.ARGUMENTO_RAM,
            "versionType":     "custom",
            "uuid":            self.TOKEN,
            "token":           self.TOKEN,
            "profileId":       self.TOKEN,
        }
    
    def __init__(self):
        if mc.utils.is_minecraft_installed(self.MINECRAFT_DIRECTORY):
            if not os.path.exists(self.RUTA_JSON):
                with open(self.RUTA_JSON, "w") as file:
                    json.dump({"profiles":{}}, file, indent=4)
        if not os.path.exists("./assets/data.json"):  
            with open("./assets/data.json", "w") as file:
                    json.dump({"username":"","version":"", }, file, indent=4)

    def createProfile(self): 
        try:
            if mc.vanilla_launcher._is_vanilla_launcher_profile_valid(self.get_settings):
                print("si es valido")
                mc.vanilla_launcher.add_vanilla_launcher_profile(self.MINECRAFT_DIRECTORY, self.get_settings)
        except Exception as inst:
            print(inst)

    def getProfile(self):
        dd = mc.vanilla_launcher.load_vanilla_launcher_profiles(self.MINECRAFT_DIRECTORY)
        for i in dd:
            if i["version"] == self.SVERSION:
                self.RUTA_JAVA = i["javaExecutable"]
                self.ARGUMENTO_RAM = self.limArg(i["javaArguments"])
                print(i["javaArguments"])
                return
            else:
                self.RUTA_JAVA = ""
                self.ARGUMENTO_RAM = ""

    def updateProfile(self):
        with open(self.RUTA_JSON, "r") as f:
            data = json.load(f)
        for j,i in data["profiles"].items():
            if i["lastVersionId"] == self.SVERSION:
                i["javaDir"] = self.RUTA_JAVA 
                i["javaArgs"] = self.ARGUMENTO_RAM
        with open(self.RUTA_JSON, "w") as file:
            json.dump(data, file, indent=4)


    def writeCache(self):
        with open("./assets/data.json", "w") as file:
            json.dump({"username":self.USERNAME,"version":self.VERSION, }, file, indent=4)


    def readCache(self):
        with open("./assets/data.json", "r") as file:
            d = json.load(file)
            self.USERNAME = d["username"]; self.VERSION = d["version"]

    def limArg(self,texto):
        # Une los elementos con espacios
        return " ".join(texto)

        

