import streamlit as st

# ایپ کی سیٹنگز
st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# --- ڈیزائن اور برانڈنگ ---
st.markdown("""
    <style>
    .brand-header {
        background: linear-gradient(90deg, #1a1a1a 0%, #333 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border-bottom: 5px solid #FFD700;
        margin-bottom: 30px;
    }
    .brand-title { color: #FFD700; font-size: 42px; font-weight: bold; margin: 0; }
    .whatsapp-btn {
        background-color: #25D366;
        color: white !important;
        padding: 18px;
        border-radius: 50px;
        text-align: center;
        display: block;
        text-decoration: none;
        font-weight: bold;
        font-size: 24px;
        margin: 25px 0;
    }
    .price-tag { color: #FFD700; font-weight: bold; font-size: 18px; background: #222; padding: 5px 10px; border-radius: 5px; }
    .category-header { background: #FFD700; color: black; padding: 10px; border-radius: 10px; font-weight: bold; margin-top: 20px; }
    </style>
    <div class="brand-header">
        <div class="brand-title">Burgerlicious.. ̲̅ᶠᴼᴼᴰ•ʙᴀʀ</div>
    </div>
""", unsafe_allow_html=True)

# واٹس ایپ بٹن
whatsapp_num = "923084779900"
st.markdown(f'<a href="https://wa.me/{whatsapp_num}" target="_blank" class="whatsapp-btn">🟢 Order Now on WhatsApp</a>', unsafe_allow_html=True)

# مینیو ڈیٹا
st.markdown("<div class='category-header'>🍔 BURGERS & SANDWICHES</div>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1:
    st.image("https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500", caption="Zinger Burger")
    st.markdown("Zinger: <span class='price-tag'>Rs. 380</span>", unsafe_allow_html=True)
with b2:
    st.image("https://images.unsplash.com/photo-1550547660-d9450f859349?w=500", caption="Special Burgers")
    st.markdown("Pizza Burger: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)
with b3:
    st.image("https://images.unsplash.com/photo-1521390188846-e2a39b7ef43a?w=500", caption="Sandwiches")
    st.markdown("Club Sandwich: <span class='price-tag'>Rs. 750</span>", unsafe_allow_html=True)

st.write("---")
st.markdown("<div class='category-header'>🍕 UP TOWN PIZZA TREAT</div>", unsafe_allow_html=True)
p1, p2 = st.columns(2)
with p1:
    st.image("https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=600", caption="Traditional Flavors")
    st.write("S: 600 | M: 1100 | L: 1500 | F: 1900")
with p2:
    st.image("https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?w=600", caption="Extreme Flavors")
    st.write("S: 780 | M: 1400 | L: 1850 | F: 2400")

st.write("---")
st.markdown("<div class='category-header'>🎁 EXCLUSIVE HOT DEALS</div>", unsafe_allow_html=True)
st.info("🔥 **Deal-01**: 2 Zinger, 1 Fries, 1 Drink — **Rs. 1000**")
st.info("🔥 **Deal-06**: 3 Zinger, 1 Mayo Fries, 1 Full Pasta, 1L Drink — **Rs. 2000**")

st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>Designed for Burgerlicious Food Bar © 2026</p>", unsafe_allow_html=True)
