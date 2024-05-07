# quicky_handy

template.pyを複製してviewsフォルダ内にアプリを作成してください。<br>
デバッグの際にはquicky_handyフォルダ内で`flet run`を実行してください。

以下、アプリの作成手順書です。

## アプリ作成の手引き

### template.pyを複製する
このとき、viewsフォルダ内に複製されているかの確認を忘れずに

### ファイルの名前、関数名、アドレス名を変更する
例えばファイル名を`bomb.py`にする場合
```python
import flet as ft

def bomb(page):
return ft.View("/bomb",[

])
```
のように変更する。

### main.pyを編集する
例えばファイル名を`photo`にする場合、main.pyを次のように変更する
```python
import flet as ft
from views import home
from views import microwave
from views import photo  # ここにimport文を追加


def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "quicky_handy"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER\

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        page.views.clear()
        if troute.match("/home"):
            page.views.append(home.home(page))
        elif troute.match("/microwave"):
            page.views.append(microwave.microwave(page))
        elif troute.mach("/photo"):  #ここにelif文を追加
            page.views.append(home.home(page))
        page.update()

    page.on_route_change = route_change    

    page.go("/home")
```
### views\home.pyを編集する
例えばファイル名を`pick`、アプリ名を`ゴミ拾い`にする場合、home.pyを次のように変更する<br>
Iconは https://gallery.flet.dev/icons-browser/ にて確認できる
```python
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
                ft.IconButton(                         # ft.IconBunnonを追加
                    icon=ft.icons.MICROWAVE_OUTLINED,  # Iconは変更するように
                    icon_size=50,tooltip="ゴミ拾い",
                    padding=ft.padding.all(15),
                    on_click=lambda _: ft.Page.go(page,"/pick"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ])
```


### 作ったファイルに戻り、プログラムを書いていく
`return ft.View`の中に要素を書き込んでいく。<br>
普通のFletでいうところの`page.add`の中に書くのと同じように書ける。<br>
いくつかの注意点を守ればスムーズに作成できるだろう。
1. returnの中でpage.○○は使用できない。
2. returnの中でViewは使用できない。
3. returnの中で宣言できない
    - returnの前に宣言しておくこと
    - というより、returnの中ではpythonの命令はほぼ使えない<br>
      (Fletのcontrolだけ使えるってイメージ)
4. returnの外でpage.○○を使用する際、引数にpageと書くこと。
    - 例 `page.update(page)`
5. `,`を忘れないこと
    - returnの中ではcontrolをリストで並べているので、control毎に<br>
      `,`が必要。エラーの6割がこれ
----------------------------------------------------------------------
microwaveを参考に作っていってほしいと思う。
