import flet as ft

def ctax(page):
    def calc(e):
        if cg.value == "ex":
            extax.value = round(float(intax.value) / (1 + (float(rate.value)) * 0.01) ,3)
            ft.Page.update(page)

        if cg.value == "in":
            intax.value = round(float(extax.value) * (1 + (float(rate.value)) * 0.01) ,3)
            ft.Page.update(page)

        if cg.value == "rt":
            rate.value = round(((float(intax.value) / float(extax.value)) * 100) - 100 ,3)
            ft.Page.update(page)
            
    extax = ft.Text("Loading...")
    intax = ft.Text("Loading...")
    rate = ft.Text("Loading...")
        
    cg = ft.RadioGroup(content=ft.Column([
        ft.Row([
            ft.Radio(value="ex"),
            extax,
        ]),
        ft.Row([
            ft.Radio(value="in"),
            intax,
        ]),
        ft.Row([
            ft.Radio(value="rt"),
            rate,
        ]),
    ]))    
    
    extax = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="税抜価格",hint_text="ここに税抜価格を入力...",on_change=calc,disabled=True if cg.value == "ex" else False,)
    intax = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="税込価格",hint_text="ここに税込価格を入力...",on_change=calc,disabled=True if cg.value == "in" else False,)
    rate = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="税率[%]",hint_text="ここに税率を入力...",on_change=calc,disabled=True if cg.value == "rt" else False,)
    
    cg = ft.RadioGroup(content=ft.Column([
        ft.Row([
            ft.Radio(value="ex"),
            extax,
        ]),
        ft.Row([
            ft.Radio(value="in"),
            intax,
        ]),
        ft.Row([
            ft.Radio(value="rt"),
            rate,
        ]),
    ])) 
    
    return ft.View("/ctax",[
        ft.AppBar(
            
            title=ft.Text("税込税抜計算"),
            center_title=True,
            leading=ft.IconButton(icon=ft.icons.HOME,on_click=lambda _: ft.Page.go(page,"/home"),),
        ),

        ft.Row(
            [
                ft.Container(
                    cg,
                    border_radius=10,
                    padding=20,
                    border=ft.border.all(1,"#43474e"),
                    width=400,
                    height=256,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Column([
            ft.Container(disabled=True,height=60),
            ft.Text("変換先にしたい数値にチェックを入れた状態で、\n他の2つを埋めると自動的に計算されます。",color="#43474e",size=24,),
            ft.Text("このアプリの計算の正確性は保証しかねます。ご注意ください。",color="#43474e",size=24),
            ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=10000000,
        ),
    ])