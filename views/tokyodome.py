import flet as ft
from module import str_f


def tokyodome(page):   
    def calcM(e):
        if textM.value == "":
            textD.value = ""
            textK.value = ""
        else:
            textD.value = str_f.float_to_str(round(float(textM.value) / 47000,5))
            textK.value = str_f.float_to_str(round(float(textM.value) / 1000000,7))
        
        ft.Page.update(page)

    def calcK(e):
        if textK.value== "":
            textD.value = ""
            textM.value = ""
        else:
            textD.value = str_f.float_to_str(round(float(textK.value) / 0.047,5))
            textM.value = str_f.float_to_str(round(float(textK.value) * 1000000,0))
        
        ft.Page.update(page)

    def calcD(e):
        if textD.value == "":
            textM.value = ""
            textK.value = ""
        else:
            textK.value = str_f.float_to_str(round(float(textD.value) * 0.047,3))
            textM.value = str_f.float_to_str(round(float(textD.value) * 47000))
        
        ft.Page.update(page)
        
    textD = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="東京ドーム[個分]",hint_text="ここに東京ドームの個数を入力...",icon=ft.icons.STADIUM_SHARP,on_change=calcD)
    textM = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="広さ[㎡]",hint_text="ここに広さを入力...",icon=ft.icons.ZOOM_OUT_MAP,on_change=calcM)
    textK = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER,label="広さ[㎢]",hint_text="ここに広さを入力...",icon=ft.icons.ZOOM_OUT_MAP,on_change=calcK)

    return ft.View("/tokyodome",[
        ft.AppBar(
            
            title=ft.Text("東京ドーム計算"),
            center_title=True,
            leading=ft.IconButton(icon=ft.icons.HOME,on_click=lambda _: ft.Page.go(page,"/home"),),
        ),

        ft.Row(
            [
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(ft.Text("東京ドーム",size=20,text_align=ft.TextAlign.CENTER),),
                            textD,
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
                
                ft.Container(width=100,disabled=True,content=ft.Icon(ft.icons.COMPARE_ARROWS,size=100,color="#43474e")),
                
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(ft.Text("広さ",size=20,text_align=ft.TextAlign.CENTER),),
                            textM,
                            textK,
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
        ft.Column([
            ft.Container(disabled=True,height=60),
            ft.Text("どれか1つでも埋めると自動的に計算されます。",color="#43474e",size=24,),
            ft.Text("このアプリの計算の正確性は保証しかねます。ご注意ください。",color="#43474e",size=24),
            ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=10000000,
        ),
    ])