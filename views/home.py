import flet as ft

def home(page):
    return ft.View("/home",[
        ft.Column(
            controls=[
                ft.Text("QUICKY HANDY α",color="#004F88",style=ft.TextStyle(font_family="r",size=86,),weight=ft.FontWeight.W_500,text_align=ft.TextAlign.CENTER,width=10000,height=104),
                ft.Text("―ちょっぴり便利な計算機―",color="#004F88",style=ft.TextStyle(font_family="r",size=32,),weight=ft.FontWeight.W_500,text_align=ft.TextAlign.CENTER,width=10000),
                ft.Container(disabled=True,height=50),
                ft.Column(
                    [
                        ft.Text("――――アプリ――――",color="#004F88",style=ft.TextStyle(font_family="r",size=48,),weight=ft.FontWeight.W_500,),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.MICROWAVE_OUTLINED,
                                    icon_size=72,
                                    padding=ft.padding.all(24),
                                    on_click=lambda _: ft.Page.go(page,"/microwave"),
                                ),
                                ft.Text("レンジ計算機",color="#004F88",style=ft.TextStyle(font_family="r",size=32,),weight=ft.FontWeight.W_700,),
                                ft.Text(" :  電子レンジのワット数と加熱時間を計算します。",color="#004F88",style=ft.TextStyle(font_family="r",size=24,),weight=ft.FontWeight.W_400,),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ATTACH_MONEY,
                                    icon_size=72,
                                    padding=ft.padding.all(24),
                                    on_click=lambda _: ft.Page.go(page,"/ctax"),
                                ),
                                ft.Text("税込税抜計算機",color="#004F88",style=ft.TextStyle(font_family="r",size=32,),weight=ft.FontWeight.W_700,),
                                ft.Text(" :  指定した税率分の税込、税抜を計算します。",color="#004F88",style=ft.TextStyle(font_family="r",size=24,),weight=ft.FontWeight.W_400,),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.STADIUM_SHARP,
                                    icon_size=72,
                                    padding=ft.padding.all(24),
                                    on_click=lambda _: ft.Page.go(page,"/tokyodome"),
                                ),
                                ft.Text("東京ドーム計算機",color="#004F88",style=ft.TextStyle(font_family="r",size=32,),weight=ft.FontWeight.W_700,),
                                ft.Text(" :  「東京ドーム〇個分」をメートル法に計算します。",color="#004F88",style=ft.TextStyle(font_family="r",size=24,),weight=ft.FontWeight.W_400,),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ASSIGNMENT_SHARP,
                                    icon_size=72,
                                    padding=ft.padding.all(24),
                                    on_click=lambda _: ft.Page.go(page,"/bmi"),
                                ),
                                ft.Text("BMI計算機",color="#004F88",style=ft.TextStyle(font_family="r",size=32,),weight=ft.FontWeight.W_700,),
                                ft.Text(" :  身長と体重からBMIを計算します。　　　　　　　　　　　　　　　　",color="#004F88",style=ft.TextStyle(font_family="r",size=24,),weight=ft.FontWeight.W_400,),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.STAR,
                                    icon_size=72,tooltip="",
                                    padding=ft.padding.all(24),
                                    on_click=lambda _: ft.Page.go(page,"/sign"),
                                ),
                                ft.Text("星座計算機",color="#004F88",style=ft.TextStyle(font_family="r",size=32,),weight=ft.FontWeight.W_700,),
                                ft.Text(" :  誕生日から星座を計算します。　　　　　　　　　　　　　　　　",color="#004F88",style=ft.TextStyle(font_family="r",size=24,),weight=ft.FontWeight.W_400,),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                    ],
                    #alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=800,
                ),
                ft.Text("――――使い方――――",color="#004F88",style=ft.TextStyle(font_family="r",size=48,),weight=ft.FontWeight.W_500,),
                ft.Text("使いたいアプリのアイコンをクリックしてください。",color="#004F88",size=24),
                ft.Text("このアプリの計算の正確性は保証しかねます。ご注意ください。",color="#004F88",size=24),
                
                
                
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            
        ),
    ],
    scroll="HIDDEN",
    )