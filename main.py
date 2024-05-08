import flet as ft
from views import home
from views import microwave
from views import ctax


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
        elif troute.match("/ctax"):
            page.views.append(ctax.ctax(page))
        page.update()

    page.on_route_change = route_change    

    page.go("/home")


if __name__ == "__main__":
    ft.app(target=main)