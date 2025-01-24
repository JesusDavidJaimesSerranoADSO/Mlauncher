import flet as ft

def main(page: ft.Page):
    page.title = "XLauncher"
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False
    page.window.maximizable = False

    def buttons(icono: ft.Icons):
        b = ft.IconButton(
            icon=icono,
            icon_size=40,
            selected=False,
            style=ft.ButtonStyle(
                color={"selected": "#30496b", "": "#32568a"}
                ),
            
        )
        return b

    button_play = buttons("PLAY_CIRCLE_FILL_OUTLINED")
    button_settins = buttons("SETTINGS")
    button_folder = buttons("FOLDER_OPEN")

    nab = ft.Container(
        content=ft.Column(
            controls=[button_play, button_settins,button_folder],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),

        margin=-10,
        padding=0,
        height=600,
        width=80,
        bgcolor="#1d1e40",
        alignment=ft.alignment.center,
    )

    page.add(
        ft.Row(
            [
                nab
            ],
        )
    )

ft.app(main)