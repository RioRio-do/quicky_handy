import flet as ft

def home(page):
    return ft.View("/home",[
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.MICROWAVE_OUTLINED,
                    icon_size=50,tooltip="レンジ変換",
                    padding=ft.padding.all(15),
                    on_click=lambda _: ft.Page.go(page,"/microwave"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ])