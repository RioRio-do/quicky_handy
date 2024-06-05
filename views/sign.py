import flet as ft

def sign(page):
    def judge(e):
        if textS1.value != "" and textW1.value != "":
            month = int(textW1.value)
            day = int(textS1.value)
            sign = get_zodiac_sign(month, day)
            textD1.value = f"星座: {sign}"
            page.update()

    def get_zodiac_sign(month, day):
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "みずがめ座"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return "うお座"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "おひつじ座"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "おうし座"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "ふたご座"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "かに座"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "しし座"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "おとめ座"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "てんびん座"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "さそり座"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "いて座"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "やぎ座"
        else:
            return "不明な星座"

    textW1 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, label="月[半角数字]", hint_text="ここに誕生日の月を入力...", icon=ft.icons.STAR, on_change=judge)
    textS1 = ft.TextField(keyboard_type=ft.KeyboardType.NUMBER, label="日[半角数字]", hint_text="ここに誕生日の日を入力...", icon=ft.icons.STAR, on_change=judge)
    textD1 = ft.Text(size=25)
    sign_image = ft.Image(src="sign.jpeg", width=350, height=300)
    
    return ft.View("/sign", [
        ft.AppBar(
            title=ft.Text("星座計算"),
            center_title=True,
            leading=ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: page.go("/home")),
        ),
        ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(ft.Text("現在のデータ", size=20, text_align=ft.TextAlign.CENTER)),
                                textW1,
                                textS1,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        border_radius=10,
                        padding=20,
                        border=ft.border.all(1, "#43474e"),
                        width=360,
                        height=256,
                    ),
                    textD1,
                    sign_image,
                ],
            ),
            width=100000,
            height=100000,
            alignment=ft.alignment.center,
        ),
    ])
