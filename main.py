import flet as ft

def main(page):
    def button_clicked(e):
        f = open ('./data/data.txt', 'r')
        temp = f.read()
        page.add(ft.Text(temp))
    page.add(ft.ElevatedButton(text="Temperature", on_click=button_clicked))
    
ft.app(target=main)