import streamlit as st

st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# KFC پریمیم برانڈنگ اسٹائل
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .kfc-header { background-color: #ffffff; padding: 20px; text-align: center; border-bottom: 6px solid #e4002b; position: sticky; top: 0; z-index: 1000; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); }
    .kfc-logo { color: #e4002b; font-size: 45px; font-weight: 900; font-family: 'Arial Black'; text-transform: uppercase; letter-spacing: -2px; margin: 0; }
    .category-title { color: #000; font-size: 32px; font-weight: 800; margin: 50px 0 25px 0; border-left: 10px solid #e4002b; padding-left: 15px; text-transform: uppercase; }
    .food-card { background: white; border-radius: 15px; padding: 0px; margin-bottom: 30px; border: 1px solid #eeeeee; transition: 0.4s; text-align: center; overflow: hidden; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); }
    .food-card:hover { transform: translateY(-10px); box-shadow: 0px 15px 30px rgba(0,0,0,0.15); }
    .food-info { padding: 15px; }
    .food-name { font-size: 20px; font-weight: bold; color: #000; min-height: 50px; display: flex; align-items: center; justify-content: center; line-height: 1.2; }
    .food-price { font-size: 24px; font-weight: 900; color: #e4002b; margin: 10px 0; }
    .order-btn { background-color: #e4002b; color: white !important; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 15px; width: 90%; transition: 0.3s; }
    .order-btn:hover { background-color: #000; }
    .deal-badge { background: #ffc107; color: black; padding: 5px 10px; border-radius: 5px; font-weight: bold; font-size: 14px; position: absolute; margin: 10px; }
    </style>
    <div class="kfc-header">
        <div class="kfc-logo">BURGERLICIOUS</div>
        <div style="color:#000; font-weight:bold; letter-spacing:4px; font-size:14px;">FOOD BAR</div>
    </div>
""", unsafe_allow_html=True)

# واٹس ایپ فلوٹنگ بٹن
st.markdown('<center><a href="https://wa.me/923084779900" style="background:#25D366; color:white; padding:18px 35px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; margin:25px 0; font-size:20px; box-shadow: 0px 5px 15px rgba(37,211,102,0.4);">📞 Order via WhatsApp: 0308-4779900</a></center>', unsafe_allow_html=True)

def food_item(name, price, img_url):
    st.markdown(f"""<div class="food-card">
        <img src="{img_url}" style="width:100%; height:220px; object-fit:cover;">
        <div class="food-info">
            <div class="food-name">{name}</div>
            <div class="food-price">Rs. {price}</div>
            <a href="https://wa.me/923084779900" class="order-btn">➕ ADD TO BUCKET</a>
        </div>
    </div>""", unsafe_allow_html=True)

# --- 🍔 برگرز اور سینڈوچز ---
st.markdown("<div class='category-title'>🍔 BURGERS & SANDWICHES</div>", unsafe_allow_html=True)
b1, b2, b3, b4 = st.columns(4)
with b1: food_item("Zinger Burger", "380", "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=500")
with b2: food_item("Cheese Zinger Burger", "450", "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=500")
with b3: food_item("Tower Burger", "550", "https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=500")
with b4: food_item("Pizza Burger", "550", "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500")

b5, b6, b7, b8 = st.columns(4)
with b5: food_item("Chicken Burger", "300", "https://images.unsplash.com/photo-1550547660-d9450f859349?w=500")
with b6: food_item("Patty Burger", "220", "https://images.unsplash.com/photo-1529692236671-f1f6e948302c?w=500")
with b7: food_item("Club Sandwich", "750", "https://images.unsplash.com/photo-1521390188846-e2a39b7ef43a?w=500")
with b8: food_item("Zinger Sandwich", "550", "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=500")

# --- 🍕 پیزا ---
st.markdown("<div class='category-title'>🍕 PIZZA TREAT</div>", unsafe_allow_html=True)
p1, p2 = st.columns(2)
with p1:
    st.markdown("""<div class="food-card">
        <img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=800" style="width:100%; height:300px; object-fit:cover;">
        <div class="food-info">
            <div class="food-name">Traditional Flavors</div>
            <p>Tikka, Fajita, BBQ, Veggie</p>
            <div class="food-price">S:600 | M:1100 | L:1500 | F:1900</div>
            <a href="https://wa.me/923084779900" class="order-btn">SELECT SIZE & ORDER</a>
        </div>
    </div>""", unsafe_allow_html=True)
with p2:
    st.markdown("""<div class="food-card">
        <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800" style="width:100%; height:300px; object-fit:cover;">
        <div class="food-info">
            <div class="food-name">Premium Flavors</div>
            <p>Extreme, Creamy Max, Euro, Seekh Kabab</p>
            <div class="food-price">S:780 | M:1400 | L:1850 | F:2400</div>
            <a href="https://wa.me/923084779900" class="order-btn">SELECT SIZE & ORDER</a>
        </div>
    </div>""", unsafe_allow_html=True)

# --- 🍝 پاستا اور سائڈز ---
st.markdown("<div class='category-title'>🍟 SNACKS & PASTA</div>", unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
with s1: food_item("Chicken Pasta", "600", "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=500")
with s2: food_item("Oven Baked Pasta", "750", "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=500")
with s3: food_item("Hot Shots (10 Pcs)", "550", "https://images.unsplash.com/photo-1562967962-e2e14bd8494d?w=500")
with s4: food_item("Chicken Wings (10 Pcs)", "550", "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=500")

# --- 🎁 ڈیلز (تصویروں کی درستگی کے ساتھ) ---
st.markdown("<div class='category-header' style='font-size:32px; color:#e4002b; font-weight:800; margin-top:50px;'>🎁 EXCLUSIVE HOT DEALS</div>", unsafe_allow_html=True)
d_col1, d_col2, d_col3 = st.columns(3)
with d_col1:
    food_item("DEAL 1: 2 Zinger + Fries + Drink", "1000", "https://images.unsplash.com/photo-1610614819513-58e34989848b?w=500")
with d_col2:
    food_item("DEAL 2: 2 Chicken Burger + Fries + Drink", "850", "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=500")
with d_col3:
    food_item("DEAL 3: Large Pizza + 1L Drink", "1650", "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=500")

d_col4, d_col5, d_col6 = st.columns(3)
with d_col4:
    food_item("DEAL 4: 2 Pizza Burgers + Fries + Drink", "1250", "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500")
with d_col5:
    food_item("DEAL 5: Medium Pizza + Zinger + 1L Drink", "1550", "https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=500")
with d_col6:
    # ڈیل 6: 3 زنگر والی ڈیل میں
