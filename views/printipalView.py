import flet as ft

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
#button_play.on_click=openPlay
button_settings = buttons("SETTINGS")
#button_settins.on_click=opensettins
button_folder = buttons("FOLDER_OPEN")
#button_folder.on_click=openFolder

nab = ft.Container(
    content=ft.Column(
        controls=[button_play, button_settings,button_folder],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    ),

    margin=-10,
    padding=0,
    height=600,
    width=80,
    bgcolor="#1d1e40",
    alignment=ft.alignment.center,
    
)