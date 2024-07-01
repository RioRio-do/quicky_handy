import flet as ft


def bmi(page):
    def judge(e):
        if textS1.value != "" and textW1.value != "":
            textD1.value = (float(textS1.value)) / ((float(textW1.value) / 100) * (float(textW1.value) / 100))
            textD1.value = f"BMI: {round(textD1.value, 2)}" 
            page.update(page)

    textW1 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="身長[cm]",hint_text="ここに現在の身長を入力...",icon=ft.icons.ACCESSIBILITY_NEW,on_change=judge)
    textS1 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="体重[kg]",hint_text="ここに現在の体重を入力...",icon=ft.icons.ASSIGNMENT_SHARP,on_change=judge)
    textD1 = ft.Text(size=25)
    bmi_image = ft.Image(src="bmi.png",width=350,height=300)
    return ft.View("/bmi",[
        ft.AppBar(
            
            title=ft.Text("bmi計算"),
            center_title=True,
            leading=ft.IconButton(icon=ft.icons.HOME,on_click=lambda _: ft.Page.go(page,"/home"),),
        ),
        ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(ft.Text("現在のデータ",size=20,text_align=ft.TextAlign.CENTER),),
                                textW1,
                                textS1,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        border_radius=10,
                        padding=20,
                        border=ft.border.all(1,"#43474e"),
                        width=360,
                        height=256,
                    ),
                    textD1,
                    bmi_image,
                        
                ],
            
            ),

        width = 100000,
        height = 100000,
        alignment=ft.alignment.center,
        ),
    ])

