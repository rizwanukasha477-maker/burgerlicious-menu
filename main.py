import streamlit as st

st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# KFC برانڈڈ اسٹائلنگ
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .kfc-header { background-color: #ffffff; padding: 15px; text-align: center; border-bottom: 5px solid #e4002b; position: sticky; top: 0; z-index: 1000; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); }
    .kfc-logo { color: #e4002b; font-size: 40px; font-weight: 900; font-family: 'Arial Black'; text-transform: uppercase; letter-spacing: -2px; margin: 0; }
    .category-title { color: #000; font-size: 28px; font-weight: 800; margin: 40px 0 20px 0; border-left: 8px solid #e4002b; padding-left: 15px; text-transform: uppercase; }
    .food-card { background: white; border-radius: 12px; padding: 0px; margin-bottom: 25px; border: 1px solid #e2e2e2; transition: 0.3s; text-align: center; overflow: hidden; height: 420px; }
    .food-card:hover { box-shadow: 0px 10px 20px rgba(0,0,0,0.1); }
    .food-info { padding: 10px; }
    .food-name { font-size: 18px; font-weight: bold; color: #000; height: 50px; display: flex; align-items: center; justify-content: center; }
    .food-price { font-size: 20px; font-weight: 900; color: #e4002b; margin-bottom: 10px; }
    .order-btn { background-color: #e4002b; color: white !important; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 13px; width: 85%; }
    </style>
    <div class="kfc-header">
        <div class="kfc-logo">BURGERLICIOUS</div>
        <span style="color:#000; font-weight:bold; letter-spacing:3px;">FOOD BAR</span>
    </div>
""", unsafe_allow_html=True)

st.markdown('<center><a href="https://wa.me/923084779900" style="background:#25D366; color:white; padding:15px 30px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:20px;">⚡ Order Now via WhatsApp</a></center>', unsafe_allow_html=True)

# فنکشن برائے فوڈ کارڈ
def item(name, price, img):
    st.markdown(f"""<div class="food-card">
        <img src="{img}" style="width:100%; height:180px; object-fit:cover;">
        <div class="food-info">
            <div class="food-name">{name}</div>
            <div class="food-price">Rs. {price}</div>
            <a href="https://wa.me/923084779900" class="order-btn">➕ ADD TO BUCKET</a>
        </div>
    </div>""", unsafe_allow_html=True)

# --- 🍔 برگرز اور سینڈوچز ---
st.markdown("<div class='category-title'>🍔 BURGERS & SANDWICHES</div>", unsafe_allow_html=True)
b1, b2, b3, b4 = st.columns(4)
with b1: item("Zinger Burger", "380", "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400")
with b2: item("Cheese Zinger", "450", "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=400")
with b3: item("Tower Burger", "550", "https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=400")
with b4: item("Pizza Burger", "550", "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400")

b5, b6, b7, b8 = st.columns(4)
with b5: item("Chicken Burger", "300", "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400")
with b6: item("Patty Burger", "220", "https://images.unsplash.com/photo-1529692236671-f1f6e948302c?w=400")
with b7: item("Club Sandwich", "750", "https://images.unsplash.com/photo-1521390188846-e2a39b7ef43a?w=400")
with b8: item("Zinger Sandwich", "550", "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400")

# --- 🍕 پیزا ---
st.markdown("<div class='category-title'>🍕 BURGERLICIOUS PIZZA TREAT</div>", unsafe_allow_html=True)
p1, p2 = st.columns(2)
with p1:
    st.markdown("""<div style="border:1px solid #ddd; padding:20px; border-radius:15px; text-align:center;">
        <img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600" style="width:100%; border-radius:10px;">
        <h3>Traditional Flavors</h3>
        <p>Tikka / Fajita / BBQ / Veggie</p>
        <p style="color:#e4002b; font-weight:bold;">S: 600 | M: 1100 | L: 1500 | F: 1900</p>
        <a href="https://wa.me/923084779900" class="order-btn">SELECT SIZE</a>
    </div>""", unsafe_allow_html=True)
with p2:
    st.markdown("""<div style="border:1px solid #ddd; padding:20px; border-radius:15px; text-align:center;">
        <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600" style="width:100%; border-radius:10px;">
        <h3>Premium Flavors</h3>
        <p>Extreme / Creamy Max / Euro / Seekh Kabab</p>
        <p style="color:#e4002b; font-weight:bold;">S: 780 | M: 1400 | L: 1850 | F: 2400</p>
        <a href="https://wa.me/923084779900" class="order-btn">SELECT SIZE</a>
    </div>""", unsafe_allow_html=True)

# --- 🍝 پاستا اور سائڈز ---
st.markdown("<div class='category-title'>🍟 SNACKS, SIDES & PASTA</div>", unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
with s1: item("Chicken Pasta", "600", "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400")
with s2: item("Oven Baked Pasta", "750", "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=400")
with s3: item("Hot Shots (10 Pcs)", "550", "https://images.unsplash.com/photo-1562967962-e2e14bd8494d?w=400")
with s4: item("Chicken Wings (10 Pcs)", "550", "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=400")

s5, s6 = st.columns(2)
with s5: item("Mayo/Loaded Fries", "500", "https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?w=400")
with s6: item("Regular Fries", "200", "https://images.unsplash.com/photo-1573082833949-0f04c6292376?w=400")

# --- 🎁 تمام ہاٹ ڈیلز ---
st.markdown("<div class='category-title'>🎁 BIG SAVER DEALS</div>", unsafe_allow_html=True)
d1, d2, d3 = st.columns(3)
with d1: item("Deal 1: 2 Zinger + Fries + Drink", "1000", "https://images.unsplash.com/photo-1610614819513-58e34989848b?w=400")
with d2: item("Deal 2: 2 Chicken Burger + Fries + Drink", "850", "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=400")
with d3: item("Deal 3: Large Pizza + 1L Drink", "1650", "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=400")

d4, d5, d6 = st.columns(3)
with d4: item("Deal 4: 2 Pizza Burgers + Fries + Drink", "1250", "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400")
with d5: item("Deal 5: Medium Pizza + Zinger + 1L Drink", "1550", "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400")
with d6: item("Deal 6: 3 Zinger + Mayo Fries + Pasta + 1L Drink", "2000", "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400")

st.markdown("<br><hr><center>© 2026 Burgerlicious Food Bar | Prices include taxes</center><br>", unsafe_allow_html=True)
