import flet as ft

class PlayPanel(ft.Stack):

    selectedVersion = ft.Dropdown(
            width=300,
            bgcolor="#f7f5f5",
        )

    selectedName = ft.TextField(hint_text="nombre de usuario", bgcolor="#f7f5f5")

    runButton = ft.FilledButton(
        text="JUGAR MINECRAFT",
        scale= 2,
        bgcolor = "#73b851",
    )

    def __init__(self):

        super().__init__(
        [
            ft.Image(
                    src="assets/mcBag.png",
                    width=720,
                    height=590,
                    fit=ft.ImageFit.FILL,
                ),
            ft.Container(
                ft.Row(
                    controls=[self.selectedName, self.selectedVersion],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                margin=ft.margin.symmetric(vertical=150)
            ),
            ft.Container(
                ft.Column(
                    controls=[self.runButton],
                    alignment=ft.MainAxisAlignment.END,
                    

                ),
                margin=ft.margin.symmetric(vertical=130, horizontal=280),

                
            ),
        ],

        height=600,
        width=720,
        )

        
        




