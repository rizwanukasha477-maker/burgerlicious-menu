import streamlit as st

st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# KFC برانڈڈ اسٹائلنگ
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .kfc-header { background-color: #ffffff; padding: 15px; text-align: center; border-bottom: 5px solid #e4002b; position: sticky; top: 0; z-index: 1000; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); }
    .kfc-logo { color: #e4002b; font-size: 40px; font-weight: 900; font-family: 'Arial Black'; text-transform: uppercase; letter-spacing: -2px; margin: 0; }
    .category-title { color: #000; font-size: 28px; font-weight: 800; margin: 40px 0 20px 0; border-left: 8px solid #e4002b; padding-left: 15px; text-transform: uppercase; }
    .food-card { background: white; border-radius: 12px; margin-bottom: 25px; border: 1px solid #e2e2e2; transition: 0.3s; text-align: center; overflow: hidden; height: 400px; }
    .food-card:hover { box-shadow: 0px 10px 20px rgba(0,0,0,0.1); }
    .food-info { padding: 10px; }
    .food-name { font-size: 17px; font-weight: bold; color: #000; height: 45px; display: flex; align-items: center; justify-content: center; }
    .food-price { font-size: 19px; font-weight: 900; color: #e4002b; margin-bottom: 10px; }
    .order-btn { background-color: #e4002b; color: white !important; padding: 8px 15px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 12px; width: 80%; }
    </style>
    <div class="kfc-header">
        <div class="kfc-logo">BURGERLICIOUS</div>
        <span style="color:#000; font-weight:bold; letter-spacing:3px;">FOOD BAR</span>
    </div>
""", unsafe_allow_html=True)

# واٹس ایپ بٹن
st.markdown('<center><a href="https://wa.me/923084779900" style="background:#25D366; color:white; padding:12px 25px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:20px;">⚡ ORDER ON WHATSAPP</a></center>', unsafe_allow_html=True)

def item(name, price, img):
    st.markdown(f"""<div class="food-card">
        <img src="{img}" style="width:100%; height:170px; object-fit:cover;">
        <div class="food-info">
            <div class="food-name">{name}</div>
            <div class="food-price">Rs. {price}</div>
            <a href="https://wa.me/923084779900" class="order-btn">➕ ADD TO BUCKET</a>
        </div>
    </div>""", unsafe_allow_html=True)

# --- 🍔 برگرز ---
st.markdown("<div class='category-title'>🍔 BURGERS</div>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1: item("Zinger Burger", "380", "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400")
with b2: item("Patty Burger", "300", "https://images.unsplash.com/photo-1529692236671-f1f6e948302c?w=400")
with b3: item("BBQ Burger", "280", "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=400")
b4, b5, b6 = st.columns(3)
with b4: item("Grill Burger", "500", "https://images.unsplash.com/photo-1550547660-d9450f859349?w=400")
with b5: item("Pizza Burger", "550", "https://images.unsplash.com/photo-1619173292416-658253a63412?w=400")
with b6: item("Burgerlicious Special", "750", "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400")

# --- 🌯 WRAPS & ROLLS ---
st.markdown("<div class='category-title'>🌯 WRAPS & PRATHA ROLLS</div>", unsafe_allow_html=True)
w1, w2, w3 = st.columns(3)
with w1: item("Chicken Shawarma", "200", "https://images.unsplash.com/photo-1561651823-34fed022540e?w=400")
with w2: item("Malai Shawarma", "280", "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400")
with w3: item("Zinger Shawarma (L)", "380", "https://images.unsplash.com/photo-1662116765994-1e0200c028ba?w=400")
w4, w5, w6 = st.columns(3)
with w4: item("Chicken Pratha", "280", "https://images.unsplash.com/photo-1633383718081-22ac93e3dbf1?w=400")
with w5: item("Malai Pratha", "320", "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400")
with w6: item("Zinger Pratha", "430", "https://images.unsplash.com/photo-1628294895950-9805252327bc?w=400")

# --- 🍕 PIZZA ---
st.markdown("<div class='category-title'>🍕 PIZZA SELECTION</div>", unsafe_allow_html=True)
st.write("### Traditional (Tikka/Fajita)")
st.info("S: 600 | M: 1100 | L: 1500 | F: 1900")
st.write("### Special (Malai Boti/Supreme)")
st.info("S: 700 | M: 1250 | L: 1700 | F: 2199")
st.write("### Extreme (Crown Crust/Creamy)")
st.error("S: 780 | M: 1400 | L: 1850 | F: 2400")

# --- 🍟 FRIES & PASTA ---
st.markdown("<div class='category-title'>🍟 FRIES & PASTA</div>", unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
with f1: item("Crunchy Fries (L)", "800", "https://images.unsplash.com/photo-1573082833949-0f04c6292376?w=400")
with f2: item("Loaded Fries (L)", "650", "https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?w=400")
with f3: item("Mayo Fries (L)", "450", "https://images.unsplash.com/photo-1619719015339-133a130520f6?w=400")

st.markdown("<br><hr><center>© 2026 Burgerlicious Food Bar</center><br>", unsafe_allow_html=True)
