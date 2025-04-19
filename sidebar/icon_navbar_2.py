import flet as ft
# define button class
class NavButton:
    def __init__(self, icon, text, action):
        self.container = ft.Container(
            ft.Row([
                ft.IconButton(icon=icon, icon_color="#dddee0", icon_size=30),
                ft.Text(text, color="#dddee0")
            ], alignment=ft.MainAxisAlignment.START),
            on_click=action,
            ink=True
        )
# defind background container
class Sidebar:
    def __init__(self, page):
        self.page = page
        self.container = ft.Container(
            content=self.create_buttons(),
            width=250, height=700, padding=10,
            alignment=ft.alignment.top_center,
            bgcolor="#1f2525",
            expand=False,
            border_radius=5,
        )
        self.page.add(self.container)
# define button clicked function
    def create_buttons(self):
        # Define actions for each button
        def print_action(name):
            print(f"{name} clicked")

        # Create main buttons -> class NavButton:
        menu_button = NavButton(ft.Icons.MENU, "Menu", lambda _: print_action("Menu"))
        home_button = NavButton(ft.Icons.HOME, "Home", lambda _: print_action("Home"))
        basic_setting_button = NavButton(ft.Icons.SETTINGS, "Basic Setting", lambda _: print_action("Basic Setting"))
        receiving_button = NavButton(ft.Icons.ADD_BOX, "Receiving Management", lambda _: print_action("Receiving Management"))
        stock_button = NavButton(ft.Icons.HOUSE, "Stock Management", lambda _: print_action("Stock Management"))
        warehouse_button = NavButton(ft.Icons.WAREHOUSE_ROUNDED, "Warehouse Working", lambda _: print_action("Warehouse Working"))
        delivery_button = NavButton(ft.Icons.DIRECTIONS_CAR_FILLED, "Delivery", lambda _: print_action("Delivery"))
        upload_button = NavButton(ft.Icons.FILE_UPLOAD_ROUNDED, "Upload", lambda _: print_action("Upload"))
        download_button = NavButton(ft.Icons.DOWNLOAD_ROUNDED, "Download", lambda _: print_action("Download"))

        return ft.Column([
            menu_button.container,
            home_button.container,
            basic_setting_button.container,
            receiving_button.container,
            stock_button.container,
            warehouse_button.container,
            delivery_button.container,
            upload_button.container,
            download_button.container
        ], spacing=20, scroll=ft.ScrollMode.ADAPTIVE)

def main(page: ft.Page):
    page.title = "Icon Navigation Bar"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    Sidebar(page)

ft.app(target=main)
