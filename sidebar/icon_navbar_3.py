import flet as ft

class NavigationBar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.container_width = 250
        self.basicsetting_submenu_visible = False
        self.warehouse_submenu_visible = False

        # Submenu items for Basic Setting
        self.company_info = self._create_submenu_item(ft.Icons.FACTORY_ROUNDED, "Company Information", lambda _: print("Company information clicked"))
        self.user_role = self._create_submenu_item(ft.Icons.SUPERVISED_USER_CIRCLE, "User Role", lambda _: print("User role clicked"))
        self.permission_settings = self._create_submenu_item(ft.Icons.LOCK_ROUNDED, "Permission Settings", lambda _: print("Permission settings clicked"))
        self.user_management = self._create_submenu_item(ft.Icons.PEOPLE, "User Management", lambda _: print("User Management clicked"))
        self.commodity_category = self._create_submenu_item(ft.Icons.FORMAT_LIST_BULLETED, "Commodity Category", lambda _: print("Commodity Category clicked"))
        self.commodity_management = self._create_submenu_item(ft.Icons.LOCAL_OFFER_ROUNDED, "Commodity Management", lambda _: print("Commodity Management clicked"))
        self.supplier_info = self._create_submenu_item(ft.Icons.LOCAL_SHIPPING_ROUNDED, "Supplier Info", lambda _: print("Supplier Info clicked"))
        self.warehouse_setting = self._create_submenu_item(ft.Icons.WAREHOUSE_ROUNDED, "Warehouse Setting", lambda _: print("Warehouse setting clicked"))
        self.owner_information = self._create_submenu_item(ft.Icons.ACCOUNT_CIRCLE_ROUNDED, "Owner Information", lambda _: print("Owner Information clicked"))
        self.freight_setting = self._create_submenu_item(ft.Icons.LOCAL_SHIPPING_ROUNDED, "Freight Settings", lambda _: print("Freight setting clicked"))
        self.customer_info = self._create_submenu_item(ft.Icons.PERSON_PIN_CIRCLE_ROUNDED, "Customer Info", lambda _: print("Customer info clicked"))
        self.print_settings = self._create_submenu_item(ft.Icons.LOCAL_PRINT_SHOP, "Print settings", lambda _: print("Print setting clicked"))

        self.basicsetting_submenu_items = ft.Column(
            [
                self.company_info,
                self.user_role,
                self.permission_settings,
                self.user_management,
                self.commodity_category,
                self.commodity_management,
                self.supplier_info,
                self.warehouse_setting,
                self.owner_information,
                self.freight_setting,
                self.customer_info,
                self.print_settings,
            ],
            visible=self.basicsetting_submenu_visible,
        )

        # Submenu items for Warehouse Working
        self.warehouse_processing = self._create_submenu_item(ft.Icons.BUILD_ROUNDED, "Warehouse Processing", lambda _: print("Warehouse Processing clicked"))
        self.inventory_move = self._create_submenu_item(ft.Icons.MOVE_DOWN, "Inventory Move", lambda _: print("Inventory Move clicked"))
        self.inventory_freeze = self._create_submenu_item(ft.Icons.PLAY_ARROW, "Inventory Freeze", lambda _: print("Inventory Freeze clicked"))
        self.inventory_adjust = self._create_submenu_item(ft.Icons.EDIT_NOTE, "Inventory Adjust", lambda _: print("Inventory Adjust clicked"))
        self.inventory_take = self._create_submenu_item(ft.Icons.FACT_CHECK, "Inventory Take", lambda _: print("Inventory Take clicked"))

        self.warehouse_submenu_items = ft.Column(
            [
                self.warehouse_processing,
                self.inventory_move,
                self.inventory_freeze,
                self.inventory_adjust,
                self.inventory_take,
            ],
            visible=self.warehouse_submenu_visible,
        )

        # Main navigation buttons
        self.menu_button = self._create_navigation_item(ft.Icons.MENU, "Menu", lambda _: print("Menu button clicked"))
        self.home_button = self._create_navigation_item(ft.Icons.HOME, "Home", lambda _: print("Home clicked"))
        self.basic_setting_button = self._create_navigation_item(ft.Icons.SETTINGS, "Basic Setting", self.toggle_basicsetting_submenu)
        self.receiving_button = self._create_navigation_item(ft.Icons.ADD_BOX, "Receiving Management", lambda _: print("Receiving Management clicked"))
        self.stock_button = self._create_navigation_item(ft.Icons.HOUSE, "Stock Management", lambda _: print("stock Management clicked"))
        self.warehouse_button = self._create_navigation_item(ft.Icons.WAREHOUSE_ROUNDED, "Warehouse Working", self.toggle_warehouse_submenu)
        self.delivery_button = self._create_navigation_item(ft.Icons.DIRECTIONS_CAR_FILLED, "Delivery Management", lambda _: print("Delivery clicked"))
        self.help_button = self._create_navigation_item(ft.Icons.HELP, "Help", lambda _: print("Help clicked"))

        self.icon_column = ft.Column(
            [
                self.menu_button,
                self.home_button,
                self.basic_setting_button,
                self.basicsetting_submenu_items,
                self.receiving_button,
                self.stock_button,
                self.warehouse_button,
                self.warehouse_submenu_items,
                self.delivery_button,
                self.help_button,
            ],
            spacing=20,
            scroll=ft.ScrollMode.ADAPTIVE,
        )

        self.container = ft.Container(
            content=self.icon_column,
            width=self.container_width,
            height=700,
            padding=10,
            alignment=ft.alignment.top_center,
            bgcolor="#1f2525",
            expand=False,
            border_radius=5,
        )

    def _create_navigation_item(self, icon, text, on_click):
        return ft.Container(
            ft.Row(
                [
                    ft.IconButton(icon=icon, icon_color="#dddee0", icon_size=25),
                    ft.Text(text, color="#dddee0"),
                ]
            ),
            on_click=on_click,
            ink=True,
        )

    def _create_submenu_item(self, icon, text, on_click):
        return ft.Container(
            ft.Row(
                [
                    ft.IconButton(icon=icon, icon_color="#dddee0", icon_size=20),
                    ft.Text(text, color="#dddee0"),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            on_click=on_click,
            ink=True,
            padding=ft.padding.only(left=20),
        )

    def toggle_basicsetting_submenu(self, e):
        """Toggles the visibility of the basic setting submenu."""
        self.basicsetting_submenu_visible = not self.basicsetting_submenu_visible
        self.basicsetting_submenu_items.visible = self.basicsetting_submenu_visible
        self.page.update()

    def toggle_warehouse_submenu(self, e):
        """Toggles the visibility of the warehouse submenu."""
        self.warehouse_submenu_visible = not self.warehouse_submenu_visible
        self.warehouse_submenu_items.visible = self.warehouse_submenu_visible
        self.page.update()

def main(page: ft.Page):
    page.title = "Icon navigation Bar"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT

    navigation_bar = NavigationBar(page)
    page.add(navigation_bar.container)

if __name__ == "__main__":
    ft.app(target=main)
