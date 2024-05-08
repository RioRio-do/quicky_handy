import flet as ft

def ctax(page):
    def calc(e):
        if extax.value == "" and intax.value != "" and rate.value != "":
            extax.value = round(intax.value / (1 + (rate.value) * 0.01) ,3)
            ft.Page.update(page)

        if extax.value != "" and intax.value == "" and rate.value != "":
            intax.value = round(extax.value * (1 + (rate.value) * 0.01) ,3)
            ft.Page.update(page)

        if extax.value != "" and intax.value != "" and rate.value == "":
            rate.value = round(((intax.value / extax.value) * 100) - 100 ,3)
            ft.Page.update(page)
            
        
        
    extax = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="税抜価格",hint_text="ここに税抜価格を入力...",icon=ft.icons.TIMER_SHARP,on_change=calc)
    intax = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="税込価格",hint_text="ここに税込価格を入力...",icon=ft.icons.TIMER_SHARP,on_change=calc)
    rate = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="税率[%]",hint_text="ここに税率を入力...",icon=ft.icons.TIMER_SHARP,on_change=calc)
    
    
    return ft.View("/ctax",[
        ft.AppBar(
            
            title=ft.Text("税込税抜変換器"),
            center_title=True,
            bgcolor="#e2f38e",
            leading=ft.IconButton(icon=ft.icons.HOME,on_click=lambda _: ft.Page.go(page,"/home"),),
        ),

        ft.Row(
            [
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(ft.Text("変換前",size=20,text_align=ft.TextAlign.CENTER),),
                            extax,
                            intax,
                            rate,
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
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ])