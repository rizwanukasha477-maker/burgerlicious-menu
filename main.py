import streamlit as st

st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# کسٹم اسٹائلنگ (صرف برانڈ نیم کے ساتھ)
st.markdown("""
    <style>
    .brand-header { background: linear-gradient(135deg, #1a1a1a 0%, #000 100%); padding: 35px; border-radius: 20px; text-align: center; border-bottom: 5px solid #FFD700; margin-bottom: 30px; }
    .brand-title { color: #FFD700; font-size: 45px; font-weight: bold; margin: 0; text-transform: uppercase; letter-spacing: 2px; }
    .category-header { background: #FFD700; color: black; padding: 12px; border-radius: 10px; font-weight: bold; margin: 35px 0 15px 0; font-size: 26px; text-align: center; }
    .price-tag { color: #FFD700; font-weight: bold; font-size: 18px; }
    .whatsapp-btn { background-color: #25D366; color: white !important; padding: 18px; border-radius: 50px; text-align: center; display: block; text-decoration: none; font-weight: bold; font-size: 22px; margin: 20px 0; box-shadow: 0px 5px 15px rgba(37,211,102,0.3); }
    </style>
    <div class="brand-header">
        <div class="brand-title">BURGERLICIOUS FOOD BAR</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<a href="https://wa.me/923084779900" class="whatsapp-btn">🟢 Order on WhatsApp: 0308-4779900</a>', unsafe_allow_html=True)

# --- 🍔 برگرز اور سینڈوچز ---
st.markdown("<div class='category-header'>🍔 BURGERLICIOUS SPECIAL BURGERS</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=500")
    st.markdown("**Zinger Burger**: <span class='price-tag'>Rs. 380</span>", unsafe_allow_html=True)
    st.markdown("**Cheese Zinger**: <span class='price-tag'>Rs. 450</span>", unsafe_allow_html=True)
    st.markdown("**Tower Burger**: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)
with col2:
    st.image("https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=500")
    st.markdown("**Pizza Burger**: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)
    st.markdown("**Chicken Burger**: <span class='price-tag'>Rs. 300</span>", unsafe_allow_html=True)
    st.markdown("**Patty Burger**: <span class='price-tag'>Rs. 220</span>", unsafe_allow_html=True)
with col3:
    st.image("https://images.unsplash.com/photo-1521390188846-e2a39b7ef43a?w=500")
    st.markdown("**Club Sandwich**: <span class='price-tag'>Rs. 750</span>", unsafe_allow_html=True)
    st.markdown("**Zinger Sandwich**: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)

# --- 🍕 پیزا سیکشن ---
st.markdown("<div class='category-header'>🍕 BURGERLICIOUS PIZZA TREAT</div>", unsafe_allow_html=True)
p_col1, p_col2 = st.columns(2)
with p_col1:
    st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600", caption="Traditional Flavors")
    st.info("**S: 600 | M: 1100 | L: 1500 | F: 1900**")
with p_col2:
    st.image("https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", caption="Premium & Extreme Flavors")
    st.info("**S: 780 | M: 1400 | L: 1850 | F: 2400**")

# --- 🍝 پاستا اور سائڈز ---
st.markdown("<div class='category-header'>🍝 SIDES & PASTA SPECIALS</div>", unsafe_allow_html=True)
s1, s2, s3 = st.columns(3)
with s1:
    st.image("https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=500")
    st.markdown("**Chicken Pasta**: <span class='price-tag'>Rs. 600</span>", unsafe_allow_html=True)
    st.markdown("**Oven Baked Pasta**: <span class='price-tag'>Rs. 750</span>", unsafe_allow_html=True)
with s2:
    st.image("https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?w=500")
    st.markdown("**Regular Fries**: <span class='price-tag'>Rs. 200</span>", unsafe_allow_html=True)
    st.markdown("**Mayo/Loaded Fries**: <span class='price-tag'>Rs. 500</span>", unsafe_allow_html=True)
with s3:
    st.image("https://images.unsplash.com/photo-1562967962-e2e14bd8494d?w=500")
    st.markdown("**Hot Shots (10 Pcs)**: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)
    st.markdown("**Wings (10 Pcs)**: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)

# --- 🎁 تمام ہاٹ ڈیلز ---
st.markdown("<div class='category-header'>🎁 BURGERLICIOUS HOT DEALS</div>", unsafe_allow_html=True)
deal_col1, deal_col2 = st.columns(2)
with deal_col1:
    st.success("🔥 **Deal 1**: 2 Zinger + Fries + Drink = **Rs. 1000**")
    st.success("🔥 **Deal 2**: 2 Chicken Burger + Fries + Drink = **Rs. 850**")
    st.success("🔥 **Deal 3**: Large Pizza + 1L Drink = **Rs. 1650**")
with deal_col2:
    st.success("🔥 **Deal 4**: 2 Pizza Burgers + Fries + Drink = **Rs. 1250**")
    st.success("🔥 **Deal 5**: Medium Pizza + Zinger + 1L Drink = **Rs. 1550**")
    st.success("🔥 **Deal 6**: 3 Zinger + Mayo Fries + Full Pasta + 1L Drink = **Rs. 2000**")

st.markdown("<p style='text-align: center; color: gray; margin-top: 50px;'>© 2026 Burgerlicious Food Bar | High Quality Fast Food</p>", unsafe_allow_html=True)
