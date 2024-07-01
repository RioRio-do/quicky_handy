import flet as ft
from views import home
from views import microwave
from views import ctax
from views import tokyodome
from views import bmi
from views import sign


def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "quicky_handy"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
        
    page.window.full_screen = True
    page.fonts = {
        "r": "/Roboto-Medium.ttf"
    }
        
    def route_change(route):
        troute = ft.TemplateRoute(route.route)
        page.views.clear()
        if troute.match("/home"):
            page.views.append(home.home(page))
        elif troute.match("/microwave"):
            page.views.append(microwave.microwave(page))
        elif troute.match("/ctax"):
            page.views.append(ctax.ctax(page))
        elif troute.match("/tokyodome"):
            page.views.append(tokyodome.tokyodome(page))
        elif troute.match("/bmi"):
            page.views.append(bmi.bmi(page))
        elif troute.match("/sign"):
            page.views.append(sign.sign(page))
        else:
            page.views.append(ft.Text("Page not found"))
        page.update()

    page.on_route_change = route_change

    page.go("/home")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", name="quicky_handy",)