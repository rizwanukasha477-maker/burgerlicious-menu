import flet as ft

# آپ کا مکمل مینو (برگر، ریپس، فرائز، پاستا اور اب تمام پیزا بھی شامل ہیں)
MENU = {
    "Pizza Traditional": [
        {"name": "Chicken Tikka", "size": "Small", "price": 600},
        {"name": "Chicken Tikka", "size": "Medium", "price": 1100},
        {"name": "Chicken Tikka", "size": "Large", "price": 1500},
        {"name": "Chicken Tikka", "size": "Family", "price": 1900},
        {"name": "Chicken Fajita", "size": "Small", "price": 600},
        {"name": "Afghani Boti", "size": "Small", "price": 600},
        {"name": "Veggie Lover", "size": "Small", "price": 600},
        {"name": "Cheese Lover", "size": "Small", "price": 600},
        {"name": "Hot & Spicy", "size": "Small", "price": 600},
    ],
    "Pizza Special": [
        {"name": "Malai Boti", "size": "Small", "price": 700},
        {"name": "Malai Boti", "size": "Medium", "price": 1250},
        {"name": "Malai Boti", "size": "Large", "price": 1700},
        {"name": "Malai Boti", "size": "Family", "price": 2199},
        {"name": "Burgerlicious Special Pizza", "size": "Small", "price": 750},
        {"name": "Burgerlicious Special Pizza", "size": "Medium", "price": 1300},
        {"name": "Burgerlicious Special Pizza", "size": "Large", "price": 1750},
        {"name": "Burgerlicious Special Pizza", "size": "Family", "price": 2250},
        {"name": "Super Supreme", "size": "Small", "price": 700},
        {"name": "Peri Peri", "size": "Small", "price": 700},
        {"name": "Picklr Pizza", "size": "Small", "price": 700},
        {"name": "Mughlai Boti", "size": "Small", "price": 700},
        {"name": "Kazoom Pizza", "size": "Small", "price": 700},
    ],
    "Pizza Extreme": [
        {"name": "Crown Crust", "size": "Small", "price": 780},
        {"name": "Crown Crust", "size": "Medium", "price": 1400},
        {"name": "Crown Crust", "size": "Large", "price": 1850},
        {"name": "Crown Crust", "size": "Family", "price": 2400},
        {"name": "Cheese Stuffer", "size": "Small", "price": 780},
        {"name": "Kabab Stuffer", "size": "Small", "price": 780},
        {"name": "Zinger Stuffer", "size": "Small", "price": 780},
        {"name": "Lazania Pizza", "size": "Small", "price": 780},
        {"name": "Behari Kabab", "size": "Small", "price": 780},
        {"name": "Crunchy Crispy", "size": "Small", "price": 780},
        {"name": "Burgerlicious Twister", "size": "Small", "price": 780},
    ],
    "Burger": [
        {"name": "Zinger Burger", "size": "Standard", "price": 380},
        {"name": "Patty Burger", "size": "Standard", "price": 300},
        {"name": "BBQ Burger", "size": "Standard", "price": 280},
        {"name": "Grill Burger", "size": "Standard", "price": 500},
        {"name": "Pizza Burger", "size": "Standard", "price": 550},
        {"name": "Burgerlicious Special Burger", "size": "Standard", "price": 750},
    ],
    "Wraps": [
        {"name": "Chicken Shawarma", "size": "Standard", "price": 200},
        {"name": "Malai Shawarma", "size": "Standard", "price": 300},
        {"name": "Zinger Shawarma", "size": "Small", "price": 280},
        {"name": "Zinger Shawarma", "size": "Large", "price": 380},
        {"name": "Chicken Pratha", "size": "Standard", "price": 280},
        {"name": "Malai Pratha", "size": "Standard", "price": 320},
        {"name": "Zinger Pratha", "size": "Standard", "price": 430},
    ],
    "Fries": [
        {"name": "Crunchy Fries", "size": "Small", "price": 500},
        {"name": "Crunchy Fries", "size": "Large", "price": 800},
        {"name": "Loaded Fries", "size": "Small", "price": 400},
        {"name": "Loaded Fries", "size": "Large", "price": 650},
        {"name": "Mayo Fries", "size": "Small", "price": 320},
        {"name": "Mayo Fries", "size": "Large", "price": 450},
        {"name": "Masala Fries", "size": "Small", "price": 280},
        {"name": "Plain Fries", "size": "Standard", "price": 250},
    ],
    "Pasta": [
        {"name": "Creamy Pasta", "size": "Small", "price": 400},
        {"name": "Creamy Pasta", "size": "Large", "price": 650},
        {"name": "Chicken Pasta", "size": "Small", "price": 400},
        {"name": "Chicken Pasta", "size": "Large", "price": 650},
        {"name": "Crunchy Pasta", "size": "Small", "price": 500},
        {"name": "Crunchy Pasta", "size": "Large", "price": 850},
    ],
    "Extra Topping": [
        {"name": "Extra Cheese/Topping", "size": "Medium", "price": 250},
        {"name": "Extra Cheese/Topping", "size": "Large", "price": 350},
        {"name": "Extra Cheese/Topping", "size": "XL", "price": 500},
    ]
}

def main(page: ft.Page):
    page.title = "Burgerlicious.. ̲̅ᶠᴼᴼᴰ•ʙᴀʀ - Billing System"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1200
    page.window_height = 800
    
    cart = {}

    # UI الیمینٹس
    items_grid = ft.GridView(expand=1, runs_count=3, max_extent=220, child_aspect_ratio=1.2, spacing=10, run_spacing=10)
    cart_list = ft.ListView(expand=True, spacing=10)
    total_text = ft.Text(value="Rs. 0", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.ORANGE_700)
    
    order_type_segmented = ft.SegmentedButton(
        selected={"take_away"},
        segments=[
            ft.Segment(value="take_away", label=ft.Text("Take Away"), icon=ft.Icon(ft.icons.LOCAL_SHIPPING)),
            ft.Segment(value="dine_in", label=ft.Text("Dine In"), icon=ft.Icon(ft.icons.RESTAURANT)),
        ]
    )

    def update_cart_ui():
        cart_list.controls.clear()
        total_bill = 0
        for key, item in cart.items():
            item_total = item['price'] * item['quantity']
            total_bill += item_total
            
            cart_list.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"{item['name']}", weight=ft.FontWeight.BOLD, size=13, max_lines=1),
                            ft.Text(f"({item['size']}) - Rs. {item['price']}", size=11, color=ft.colors.GREY_600),
                        ], expand=True),
                        ft.Row([
                            ft.IconButton(ft.icons.REMOVE_CIRCLE_OUTLINE, on_click=lambda e, k=key: change_qty(k, -1), icon_size=18),
                            ft.Text(str(item['quantity']), size=13, weight=ft.FontWeight.BOLD),
                            ft.IconButton(ft.icons.ADD_CIRCLE_OUTLINE, on_click=lambda e, k=key: change_qty(k, 1), icon_size=18),
                        ], spacing=0),
                        ft.Text(f"Rs. {item_total}", size=13, weight=ft.FontWeight.BOLD),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=6,
                    border=ft.border.all(1, ft.colors.GREY_300),
                    border_radius=8
                )
            )
        total_text.value = f"Rs. {total_bill}"
        page.update()

    def add_to_cart(item):
        key = f"{item['name']}_{item['size']}"
        if key in cart:
            cart[key]['quantity'] += 1
        else:
            cart[key] = {
                "name": item['name'],
                "size": item['size'],
                "price": item['price'],
                "quantity": 1
            }
        update_cart_ui()

    def change_qty(key, delta):
        if key in cart:
            cart[key]['quantity'] += delta
            if cart[key]['quantity'] <= 0:
                del cart[key]
        update_cart_ui()

    def load_category_items(category_name):
        items_grid.controls.clear()
        for item in MENU[category_name]:
            items_grid.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(item['name'], weight=ft.FontWeight.BOLD, size=13, text_align=ft.TextAlign.CENTER, max_lines=2),
                            ft.Text(f"Size: {item['size']}", size=11, color=ft.colors.GREY_600),
                            ft.Text(f"Rs. {item['price']}", size=13, color=ft.colors.ORANGE_700, weight=ft.FontWeight.BOLD),
                        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=8,
                        on_click=lambda e, i=item: add_to_cart(i),
                    ),
                    elevation=2
                )
            )
        page.update()

    def clear_all(e):
        cart.clear()
        update_cart_ui()

    def print_action(print_type):
        if not cart: return
        bill_content = f"--- Burgerlicious ---\n--- {print_type} ---\nType: {list(order_type_segmented.selected)[0].upper()}\n\n"
        for item in cart.values():
            bill_content += f"{item['name']} ({item['size']}) x{item['quantity']} = {item['price']*item['quantity']}\n"
        bill_content += f"\nTotal: {total_text.value}\n----------------"
        
        page.open(ft.AlertDialog(title=ft.Text(f"{print_type} Generated"), content=ft.Text(bill_content)))

    # سائیڈ بار کے بٹنز اور ان کے آئیکنز
    sidebar_buttons = []
    icons_mapping = {
        "Pizza Traditional": ft.icons.LOCAL_PIZZA,
        "Pizza Special": ft.icons.LOCAL_PIZZA,
        "Pizza Extreme": ft.icons.LOCAL_PIZZA,
        "Burger": ft.icons.FASTFOOD,
        "Wraps": ft.icons.CORGI,
        "Fries": ft.icons.HOT_TUB,
        "Pasta": ft.icons.LOCAL_DINING,
        "Extra Topping": ft.icons.ADD_CIRCLE
    }

    for cat in MENU.keys():
        sidebar_buttons.append(
            ft.ElevatedButton(
                text=cat,
                icon=icons_mapping.get(cat, ft.icons.FASTFOOD),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                width=180,
                height=45,
                on_click=lambda e, c=cat: load_category_items(c)
            )
        )

    # ڈیفالٹ پہلی کیٹیگری لوڈ کریں
    load_category_items("Pizza Traditional")

    page.add(
        ft.Row([
            # 1. سائیڈ بار (کیٹیگریز کے لیے سکرول ایبل کالم)
            ft.Container(
                content=ft.Column(sidebar_buttons, spacing=10, alignment=ft.MainAxisAlignment.START, scroll=ft.ScrollMode.AUTO),
                width=210,
                padding=10,
                bgcolor=ft.colors.GREY_100,
                border_radius=10
            ),
            # 2. سینٹرل گرڈ (پروڈکٹس)
            ft.Container(
                content=items_grid,
                expand=2,
                padding=5
            ),
            # 3. دائیں طرف (کارٹ اور بلنگ کنٹرولز)
            ft.Container(
                content=ft.Column([
                    ft.Text("Burgerlicious Order", size=18, weight=ft.FontWeight.BOLD),
                    order_type_segmented,
                    ft.Divider(),
                    cart_list,
                    ft.Divider(),
                    ft.Row([
                        ft.Text("Total:", size=16, weight=ft.FontWeight.BOLD),
                        total_text
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([
                        ft.ElevatedButton("Clear", icon=ft.icons.DELETE_OUTLINE, on_click=clear_all, bgcolor=ft.colors.RED_50, color=ft.colors.RED_700),
                        ft.ElevatedButton("KOT", icon=ft.icons.KITCHEN, on_click=lambda e: print_action("Kitchen Token"), bgcolor=ft.colors.BLUE_50, color=ft.colors.BLUE_700),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.ElevatedButton("Print Final Bill", icon=ft.icons.PRINT, on_click=lambda e: print_action("Customer Bill"), width=300, height=45, bgcolor=ft.colors.ORANGE_500, color=ft.colors.WHITE),
                ], spacing=10),
                width=350,
                padding=15,
                bgcolor=ft.colors.GREY_50,
                border=ft.border.all(1, ft.colors.GREY_200),
                border_radius=10
            )
        ], expand=True)
    )

ft.app(target=main)
