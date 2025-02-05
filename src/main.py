import flet as ft


def main(page: ft.Page):
    page.title = "Apartment Manager"
    page.theme_mode = "light"
    page.padding = 0

    # Login section
    def login_view():
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Welcome to Apartment ", size=32, weight="bold"),
                    ft.TextField(label="Email", icon=ft.icons.EMAIL),
                    ft.TextField(label="Password", password=True, icon=ft.icons.LOCK),
                    ft.ElevatedButton(text="Login", width=200),
                ],
                horizontal_alignment="center",
                spacing=20,
            ),
            padding=50,
            alignment=ft.alignment.center,
        )

    # Main app layout after login
    def app_view():
        return ft.Row(
            controls=[
                # Navigation rail
                ft.NavigationRail(
                    selected_index=0,
                    label_type="all",
                    extended=True,
                    destinations=[
                        ft.NavigationRailDestination(
                            icon=ft.icons.DASHBOARD_OUTLINED,
                            selected_icon=ft.icons.DASHBOARD,
                            label="Dashboard",
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.PEOPLE_OUTLINE,
                            selected_icon=ft.icons.PEOPLE,
                            label="Tenants",
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.MESSAGE_OUTLINED,
                            selected_icon=ft.icons.MESSAGE,
                            label="Messages",
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.SETTINGS_OUTLINED,
                            selected_icon=ft.icons.SETTINGS,
                            label="Settings",
                        ),
                    ],
                ),
                # Main content area
                ft.VerticalDivider(width=1),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Text("Dashboard", size=30, weight="bold"),
                                        ft.IconButton(icon=ft.icons.NOTIFICATIONS),
                                        ft.IconButton(icon=ft.icons.PERSON),
                                    ],
                                    alignment="spaceBetween",
                                ),
                                padding=20,
                            ),
                            ft.Container(
                                content=ft.GridView(
                                    runs_count=2,
                                    max_extent=200,
                                    child_aspect_ratio=1.0,
                                    spacing=20,
                                    run_spacing=20,
                                    controls=[
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Icon(
                                                            name=ft.icons.HOME_WORK,
                                                            size=30,
                                                        ),
                                                        ft.Text("Total Units", size=20),
                                                        ft.Text(
                                                            "24", size=30, weight="bold"
                                                        ),
                                                    ],
                                                    horizontal_alignment="center",
                                                    spacing=10,
                                                ),
                                                padding=20,
                                            )
                                        ),
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Icon(
                                                            name=ft.icons.PERSON,
                                                            size=30,
                                                        ),
                                                        ft.Text(
                                                            "Total Tenants", size=20
                                                        ),
                                                        ft.Text(
                                                            "18", size=30, weight="bold"
                                                        ),
                                                    ],
                                                    horizontal_alignment="center",
                                                    spacing=10,
                                                ),
                                                padding=20,
                                            )
                                        ),
                                    ],
                                ),
                                padding=20,
                            ),
                        ],
                    ),
                    expand=True,
                ),
            ],
            expand=True,
        )

    # Initial view is login
    page.add(login_view())


ft.app(target=main)
