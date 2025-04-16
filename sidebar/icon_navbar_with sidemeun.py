# icon navigation bar
# reference: Python Tutorial: Navbar Using Flet
# https://www.youtube.com/watch?v=4Rg3VWcsppc
# Flet Tutorial - Create SideMenu Navigation
# https://www.youtube.com/watch?v=II7HnGeozDI
import flet as ft

def main(page: ft.Page):
    page.title = "Icon navigation Bar"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    # Define the intial width of container_1
    container_width = 250
    # define logic click meun button change container_1 width
    # define submeun (basing setting)
    def toggle_basicsetting_submenu(e):
        """Toggles the visibility of the warehouse submenu."""
        basicsetting_submenu.visible = not basicsetting_submenu.visible
        page.update()
    # define submeun buttom (basic setting)
    Company_information = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Company Information", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Company information clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    user_role = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.SUPERVISED_USER_CIRCLE, icon_color = "#dddee0", icon_size = 20),
            ft.Text("User Role", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("User role clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    permission_settings = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Permission Settings", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Permission settings clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    user_management = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.PEOPLE, icon_color = "#dddee0", icon_size = 20),
            ft.Text("User Management", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("User Management clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    commodity_category = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FORMAT_LIST_BULLETED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Commdity Category", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Commodity Category clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    commodity_management = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Commdity Management", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Commodity Management clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    supplier_info = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Supplier Info", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Supplier Info clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    warehouse_setting = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.WAREHOUSE_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Warehouse Setting", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Warehouse setting clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    owner_information = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Owner Information", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Owner Information clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    freight_setting  = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Freight Settings", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Freight setting clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    customer_info = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Customer Info", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Customer info clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    print_settings = ft.Container(
        ft.Row([
            ft.IconButton(icon = ft.Icons.LOCAL_PRINT_SHOP, icon_color = "#dddee0", icon_size = 20),
            ft.Text("Print settings", color = "#dddee0")
        ],alignment = ft.MainAxisAlignment.START),
        on_click = lambda _:print("Print setting clicked"),
        ink = True,
        padding = ft.padding.only(left=20))
    basicsetting_submenu_items = ft.Column(
        [
            Company_information,
            user_role,
            permission_settings,
            user_management,
            commodity_category,
            commodity_management,
            supplier_info,
            warehouse_setting,
            owner_information,
            freight_setting,
            customer_info,
            print_settings
        ], visible = False)
    # define submeun (warehouse working)
    def toggle_warehouse_submenu(e):
        """Toggles the visibility of the warehouse submenu."""
        warehouse_submenu.visible = not warehouse_submenu.visible
        page.update()
    # define submeun button
    warehouse_submenu_items = ft.Column([
        ft.Container(
            ft.Row([
                ft.IconButton(icon = ft.Icons.FACTORY_ROUNDED, icon_color = "#dddee0", icon_size = 20),
                ft.Text("Warehouse Processing", color = "#dddee0")
            ],alignment = ft.MainAxisAlignment.START),
            on_click = lambda _:print("Warehouse Processing clicked"),
            ink = True,
            padding = ft.padding.only(left=20)
        ),
        ft.Container(
            ft.Row([
                ft.IconButton(icon = ft.Icons.MOVE_DOWN, icon_color = "#dddee0", icon_size = 20),
                ft.Text("Inventory Move", color = "#dddee0")
            ],alignment = ft.MainAxisAlignment.START),
            on_click = lambda _:print("Warehouse Processing clicked"),
            ink = True,
            padding = ft.padding.only(left=20)
        ),
        ft.Container(
            ft.Row([
                ft.IconButton(icon=ft.Icons.PLAY_ARROW, icon_color="#dddee0", icon_size=20),
                ft.Text("Inventory Freeze", color="#dddee0")
            ], alignment=ft.MainAxisAlignment.START),
            on_click=lambda _: print("Inventory Freeze clicked"),
            ink=True,
            padding=ft.padding.only(left=20)
        ),
        ft.Container(
            ft.Row([
                ft.IconButton(icon=ft.Icons.EDIT_NOTE, icon_color="#dddee0", icon_size=20),
                ft.Text("Inventory Adjust", color="#dddee0")
            ], alignment=ft.MainAxisAlignment.START),
            on_click=lambda _: print("Inventory Adjust clicked"),
            ink=True,
            padding=ft.padding.only(left=20)
        ),
        ft.Container(
            ft.Row([
                ft.IconButton(icon=ft.Icons.FACT_CHECK, icon_color="#dddee0", icon_size=20),
                ft.Text("Inventory Take", color="#dddee0")
            ], alignment=ft.MainAxisAlignment.START),
            on_click=lambda _: print("Inventory Take clicked"),
            ink=True,
            padding=ft.padding.only(left=20)
        )
    ], visible = False)
    # difine button
    menu = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon = ft.Icons.MENU, icon_color = "#dddee0", icon_size = 25),
        ft.Text("Menu", color = "#dddee0")]),on_click =lambda _ :print("Meun button clicked"), ink = True)
    home = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon = ft.Icons.HOME, icon_color = "#dddee0", icon_size = 25),
                ft.Text("Home", color='#dddee0')]), on_click=lambda _: print("Home clicked"), ink=True)
    basic_setting = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon= ft.Icons.SETTINGS, icon_color = "#dddee0", icon_size = 25),
                ft.Text("Basic Setting", color= "#dddee0")]), on_click= toggle_basicsetting_submenu, ink=True)
    Receiving = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon= ft.Icons.ADD_BOX, icon_color = "#dddee0", icon_size = 25),
                ft.Text("Receiving Management", color= "#dddee0")]),on_click=lambda _: print("Receiving Management clicked"), ink=True)
    Stock = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon= ft.Icons.HOUSE, icon_color = "#dddee0", icon_size =25),
                ft.Text("Stock Management", color= "#dddee0")]),on_click=lambda _: print("stock Management clicked"), ink=True)
    Warehouse = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon= ft.Icons.WAREHOUSE_ROUNDED, icon_color = "#dddee0", icon_size = 25),
                ft.Text("Warehouse Working", color = "#dddee0")]),on_click=toggle_warehouse_submenu, ink=True)
    Delivery = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon= ft.Icons.DIRECTIONS_CAR_FILLED, icon_color = "#dddee0", icon_size = 25),
                ft.Text("Delivery Management", color = "#dddee0")]),on_click=lambda _: print("Delivery clicked"), ink=True)
    Help = ft.Container(
        ft.Row(
            [
                ft.IconButton(icon= ft.Icons.HELP, icon_color = "#dddee0", icon_size = 20),
                ft.Text("Help", color= "#dddee0")]),on_click=lambda _: print("Help clicked"), ink=True)
    icon_button = ft.Column([menu, home, basic_setting, basicsetting_submenu_items, Receiving, Stock, Warehouse, warehouse_submenu_items, Delivery, Help], spacing = 20,
        scroll = ft.ScrollMode.ADAPTIVE) # Enable scrolling for the Column)
    # sidebar Container
    container_1 = ft.Container(
        content = icon_button,
        width = container_width, height = 700, padding = 10,
        alignment=ft.alignment.top_center,
        bgcolor = "#1f2525",
        expand = False,
        border_radius = 5,
    )
    page.add(container_1)
    # Define warehouse_submenu_items
    warehouse_submenu = warehouse_submenu_items
    # Define basic_setting_itmes
    basicsetting_submenu = basicsetting_submenu_items
ft.app(target = main)
