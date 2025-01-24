import os
import subprocess
import minecraft_launcher_lib as mc

LAUNCHER_VERSION = '1.0.0'
MINECRAFT_DIRECTORY = mc.utils.get_minecraft_directory()
TOKEN = '5998213610:AAHUfeee08ryYWrRhLJ0yI8SL8F0RQu0wKs' 

def valoreNulos(valor):
    if valor == "":
        return False
    elif valor == None:
        return False
    elif valor == "none":
        return False
    else: return True


def validateDirectorio():
    return mc.utils.is_minecraft_installed(MINECRAFT_DIRECTORY)

def installedList():
    ver=[]
    for i in mc.utils.get_installed_versions(MINECRAFT_DIRECTORY):
        ver.append(i["id"])
    return ver

def selectionVersion(type):
    if type == "Vanilla":
        return vanillaList()
    elif type == "Forge":
        return forgeList()

def vanillaList():
    ver=[]
    for i in mc.utils.get_version_list():
        ver.append(i["id"])
    return ver

def forgeList():
    ver=[]
    for i in mc.forge.list_forge_versions():
        ver.append(i)
    return ver

def installedVersion(vers):
    for i in mc.utils.get_installed_versions(MINECRAFT_DIRECTORY):
        if i["id"] == vers:
            return False

def validVersion(vers):
    return mc.utils.is_version_valid(vers, MINECRAFT_DIRECTORY)

def installerVanilla(vers:str):
    if validVersion(vers):
        try:
            mc.install.install_minecraft_version(vers, MINECRAFT_DIRECTORY)
            return "version ya instalada"
        except:
            return "error al descargar la versio"

def installerForge(vers:str):
    if validVersion(vers):
        try:
            mc.forge.install_forge_version(vers, MINECRAFT_DIRECTORY)
            return "version ya instalada"
        except:
            return "error al descargar la versio"

def runMinecraft(version, username):
    if valoreNulos(version) and valoreNulos(username):
        options = {
            "username": username,
            "uuid": '',
            "token": TOKEN,
            "jvmArguments": [
                f"-Xmx{4}G",
                f"-Xms{4}G",
            ]
        }

            # Ejecutar Minecraft
        minecraft_command = mc.command.get_minecraft_command(
            version, MINECRAFT_DIRECTORY, options
        )
        subprocess.run(minecraft_command, creationflags=subprocess.CREATE_NO_WINDOW)

