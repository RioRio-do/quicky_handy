import flet as ft

def microwave(page):
    def calcS(e):
        textS2.value = round(int(textW1.value) / int(textW2.value) * int(textS1.value))
        ft.Page.update(page)
    
    def calcW(e):
        textW2.value = round(int(textW1.value) / int(textS2.value) * int(textS1.value))
        ft.Page.update(page)
        
    textW1 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="ワット数[W]",hint_text="ここにレンジのワット数を入力...",icon=ft.icons.ELECTRIC_BOLT,)
    textS1 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="加熱時間[秒]",hint_text="ここにレンジの加熱時間を入力...",icon=ft.icons.TIMER_SHARP)
    textW2 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="ワット数[W]",hint_text="ここにレンジのワット数を入力...",icon=ft.icons.ELECTRIC_BOLT,on_change=calcS)
    textS2 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="加熱時間[秒]",hint_text="ここにレンジの加熱時間を入力...",icon=ft.icons.TIMER_SHARP,on_change=calcW)
    
    return ft.View("/microwave",[
        ft.AppBar(
            
            title=ft.Text("電子レンジ出力変換機"),
            center_title=True,
            leading=ft.IconButton(icon=ft.icons.HOME,on_click=lambda _: ft.Page.go(page,"/home"),),
        ),

        ft.Row(
            [
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(ft.Text("変換前",size=20,text_align=ft.TextAlign.CENTER),),
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
                
                ft.Container(width=100,disabled=True,content=ft.Icon(ft.icons.ARROW_RIGHT_ALT,size=100,color="#43474e")),
                
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(ft.Text("変換後",size=20,text_align=ft.TextAlign.CENTER),),
                            textW2,
                            textS2,
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