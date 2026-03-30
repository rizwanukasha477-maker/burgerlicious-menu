import streamlit as st

st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# KFC انسپائرڈ ڈیزائن
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { background-color: #ffffff; }
    .brand-header { background-color: #e4002b; padding: 20px; text-align: center; border-bottom: 8px solid #000000; margin-bottom: 20px; }
    .brand-title { color: white; font-size: 50px; font-weight: 900; font-family: 'Arial Black'; margin: 0; letter-spacing: -2px; }
    .category-header { color: #e4002b; border-left: 10px solid #e4002b; padding-left: 15px; font-weight: bold; margin: 40px 0 20px 0; font-size: 32px; text-transform: uppercase; font-family: 'Condensed'; }
    .price-card { background: #f8f8f8; padding: 15px; border-radius: 10px; border: 1px solid #ddd; text-align: center; transition: 0.3s; }
    .price-card:hover { box-shadow: 0px 5px 15px rgba(0,0,0,0.1); }
    .price-text { color: #e4002b; font-size: 24px; font-weight: bold; }
    .whatsapp-float { background-color: #25D366; color: white !important; padding: 15px 30px; border-radius: 50px; text-align: center; display: block; text-decoration: none; font-weight: bold; font-size: 20px; margin: 20px auto; width: fit-content; box-shadow: 0px 4px 10px rgba(0,0,0,0.2); }
    </style>
    <div class="brand-header">
        <div class="brand-title">BURGERLICIOUS</div>
        <p style='color: white; font-weight: bold; margin-top: -5px;'>FOOD BAR</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('<a href="https://wa.me/923084779900" class="whatsapp-float">⚡ ORDER NOW ON WHATSAPP</a>', unsafe_allow_html=True)

# --- 🔥 BEST SELLERS (KFC Style) ---
st.markdown("<div class='category-header'>⭐ BEST SELLERS</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=500")
    st.markdown("<div class='price-card'><b>Zinger Burger</b><br><span class='price-text'>Rs. 380</span></div>", unsafe_allow_html=True)
with col2:
    st.image("https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=500")
    st.markdown("<div class='price-card'><b>Tower Burger</b><br><span class='price-text'>Rs. 550</span></div>", unsafe_allow_html=True)
with col3:
    st.image("https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600")
    st.markdown("<div class='price-card'><b>Burgerlicious Special Pizza</b><br><span class='price-text'>From Rs. 600</span></div>", unsafe_allow_html=True)

# --- 🎁 EXCLUSIVE DEALS ---
st.markdown("<div class='category-header'>🎁 BIG SAVER DEALS</div>", unsafe_allow_html=True)
d1, d2 = st.columns(2)
with d1:
    st.image("https://images.unsplash.com/photo-1610614819513-58e34989848b?w=600")
    st.info("🔥 **DEAL 1**: 2 Zinger + Fries + Drink | **Rs. 1000**")
with d2:
    st.image("https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=600")
    st.info("🔥 **DEAL 6**: 3 Zinger + Mayo Fries + Pasta + 1L Drink | **Rs. 2000**")

# --- 🍟 SNACKS & SIDES ---
st.markdown("<div class='category-header'>🍟 SNACKS & SIDES</div>", unsafe_allow_html=True)
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("**Hot Shots (10 Pcs)**: <span style='color:#e4002b; font-weight:bold;'>Rs. 550</span>", unsafe_allow_html=True)
    st.markdown("**Chicken Wings (10 Pcs)**: <span style='color:#e4002b; font-weight:bold;'>Rs. 550</span>", unsafe_allow_html=True)
with s2:
    st.markdown("**Chicken Pasta**: <span style='color:#e4002b; font-weight:bold;'>Rs. 600</span>", unsafe_allow_html=True)
    st.markdown("**Oven Baked Pasta**: <span style='color:#e4002b; font-weight:bold;'>Rs. 750</span>", unsafe_allow_html=True)
with s3:
    st.markdown("**Loaded Fries**: <span style='color:#e4002b; font-weight:bold;'>Rs. 500</span>", unsafe_allow_html=True)
    st.markdown("**Regular Fries**: <span style='color:#e4002b; font-weight:bold;'>Rs. 200</span>", unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; color: #999; border-top: 1px solid #eee; padding-top: 20px;'>Prices are inclusive of all taxes. © 2026 Burgerlicious Food Bar</p>", unsafe_allow_html=True)
