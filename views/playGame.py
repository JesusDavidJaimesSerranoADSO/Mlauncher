import flet as ft
from controlles.gameOptions import installedList, runMinecraft, LAUNCHER_VERSION

ventana = ft.Page

def listaVersiones():
    ap = []
    for i in installedList():
        ap.append(ft.dropdown.Option(i))
    return ap
    
def iniciarJuego(e):
    userName = selectedName.value
    version = selectedVersion.value
    runMinecraft(version, userName)
    ventana.window.visible = True


selectedVersion = ft.Dropdown(
    options = listaVersiones(),
    width=300,
    bgcolor="#f7f5f5",

)

selectedName = ft.TextField(hint_text="nombre de usuario", bgcolor="#f7f5f5")

runPlay = ft.FilledButton(
    text="JUGAR MINECRAFT",
    scale= 2,
    bgcolor = "#73b851",
    on_click=iniciarJuego

)

playContent = ft.Stack(
    [
        ft.Image(
                src="assets/mcBag.png",
                width=720,
                height=600,
                fit=ft.ImageFit.FILL,
            ),
        ft.Container(
            ft.Row(
                controls=[selectedName, selectedVersion],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.margin.symmetric(vertical=150)
        ),
        ft.Container(
            ft.Column(
                controls=[runPlay],
                alignment=ft.MainAxisAlignment.END,
                

            ),
            margin=ft.margin.symmetric(vertical=130, horizontal=280),

            
        ),
    ],

    height=600,
    width=720,
)