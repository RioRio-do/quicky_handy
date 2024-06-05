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
                ft.IconButton(
                    icon=ft.icons.ATTACH_MONEY,
                    icon_size=50,tooltip="税込税抜変換",
                    padding=ft.padding.all(15),
                    on_click=lambda _: ft.Page.go(page,"/ctax"),
                ),
                ft.IconButton(
                    icon=ft.icons.STADIUM_SHARP,
                    icon_size=50,tooltip="東京ドーム変換",
                    padding=ft.padding.all(15),
                    on_click=lambda _: ft.Page.go(page,"/tokyodome"),
                ),
                ft.IconButton(
                    icon=ft.icons.ASSIGNMENT_SHARP,
                    icon_size=50,tooltip="BMI計算",
                    padding=ft.padding.all(15),
                    on_click=lambda _: ft.Page.go(page,"/bmi"),
                ),
                ft.IconButton(
                    icon=ft.icons.STAR,
                    icon_size=50,tooltip="星座計算",
                    padding=ft.padding.all(15),
                    on_click=lambda _: ft.Page.go(page,"/sign"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ])