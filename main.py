import streamlit as st

st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# کسٹم ڈیزائن (Black & Gold Theme)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .brand-header { background: linear-gradient(135deg, #1a1a1a 0%, #000 100%); padding: 30px; border-radius: 20px; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .brand-title { color: #FFD700; font-size: 45px; font-weight: bold; margin: 0; text-transform: uppercase; letter-spacing: 2px; }
    .category-header { background: #FFD700; color: black; padding: 12px; border-radius: 10px; font-weight: bold; margin: 30px 0 20px 0; font-size: 24px; text-align: center; box-shadow: 0px 4px 10px rgba(255, 215, 0, 0.3); }
    .price-tag { color: #FFD700; font-weight: bold; font-size: 20px; }
    .item-card { background: #1f1f1f; padding: 15px; border-radius: 15px; border: 1px solid #333; margin-bottom: 20px; transition: 0.3s; }
    .whatsapp-btn { background-color: #25D366; color: white !important; padding: 20px; border-radius: 50px; text-align: center; display: block; text-decoration: none; font-weight: bold; font-size: 24px; margin: 30px 0; box-shadow: 0px 5px 15px rgba(37, 211, 102, 0.4); }
    </style>
    <div class="brand-header">
        <div class="brand-title">BURGERLICIOUS FOOD BAR</div>
        <p style='color: #ccc; font-size: 18px;'>The Ultimate Taste of Fast Food</p>
    </div>
""", unsafe_allow_html=True)

# واٹس ایپ آرڈر بٹن
st.markdown('<a href="https://wa.me/923084779900" class="whatsapp-btn">🟢 Order Now on WhatsApp</a>', unsafe_allow_html=True)

# --- 🍔 برگر سیکشن ---
st.markdown("<div class='category-header'>🍔 PREMIUM BURGERS</div>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1:
    st.image("https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=500", caption="Zinger Burger")
    st.markdown("<div class='item-card'>Zinger: <span class='price-tag'>Rs. 380</span></div>", unsafe_allow_html=True)
with b2:
    st.image("https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=500", caption="Tower Burger")
    st.markdown("<div class='item-card'>Tower: <span class='price-tag'>Rs. 550</span></div>", unsafe_allow_html=True)
with b3:
    st.image("https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=500", caption="Pizza Burger")
    st.markdown("<div class='item-card'>Pizza Burger: <span class='price-tag'>Rs. 550</span></div>", unsafe_allow_html=True)

# --- 🍕 پیزا سیکشن ---
st.markdown("<div class='category-header'>🍕 UP TOWN PIZZA TREAT</div>", unsafe_allow_html=True)
p1, p2 = st.columns(2)
with p1:
    st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600", caption="Chicken Tikka / Fajita")
    st.info("**Small: 600 | Medium: 1100 | Large: 1500**")
with p2:
    st.image("https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", caption="Extreme Flavors")
    st.info("**Small: 780 | Medium: 1400 | Large: 1850**")

# --- 🎁 ڈیلز سیکشن ---
st.markdown("<div class='category-header'>🎁 EXCLUSIVE HOT DEALS</div>", unsafe_allow_html=True)
d1, d2 = st.columns(2)
with d1:
    st.image("https://images.unsplash.com/photo-1610614819513-58e34989848b?w=600", caption="Deal 01")
    st.success("🔥 **Deal 1**: 2 Zinger + Fries + Drink = **Rs. 1000**")
with d2:
    st.image("https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=600", caption="Deal 06")
    st.success("🔥 **Deal 6**: 3 Zinger + Mayo Fries + Pasta + 1L Drink = **Rs. 2000**")

# --- 🍟 سائڈز اور پاستا ---
st.markdown("<div class='category-header'>🍟 SIDES & PASTA</div>", unsafe_allow_html=True)
s1, s2 = st.columns(2)
with s1:
    st.image("https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?w=500", caption="Loaded Fries")
    st.markdown("<div class='item-card'>Loaded Fries: <span class='price-tag'>Rs. 500</span></div>", unsafe_allow_html=True)
with s2:
    st.image("https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=500", caption="Chicken Pasta")
    st.markdown("<div class='item-card'>Chicken Pasta: <span class='price-tag'>Rs. 600</span></div>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>© 2026 Burgerlicious Food Bar | Quality You Can Taste</p>", unsafe_allow_html=True)
