import streamlit as st

st.set_page_config(page_title="Burgerlicious Food Bar", page_icon="🍔", layout="wide")

# کسٹم ڈیزائن
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .brand-header { background: linear-gradient(90deg, #1a1a1a 0%, #333 100%); padding: 20px; border-radius: 15px; text-align: center; border-bottom: 4px solid #FFD700; margin-bottom: 20px; }
    .brand-title { color: #FFD700; font-size: 35px; font-weight: bold; margin: 0; font-family: 'Arial'; }
    .category-header { background: #FFD700; color: black; padding: 8px 15px; border-radius: 8px; font-weight: bold; margin: 20px 0 10px 0; font-size: 20px; text-align: center; }
    .price-tag { color: #FFD700; font-weight: bold; background: #262730; padding: 2px 8px; border-radius: 4px; }
    .whatsapp-btn { background-color: #25D366; color: white !important; padding: 15px; border-radius: 10px; text-align: center; display: block; text-decoration: none; font-weight: bold; font-size: 20px; margin-top: 20px; }
    </style>
    <div class="brand-header"><div class="brand-title">Burgerlicious.. ̲̅ᶠᴼᴼᴰ•ʙᴀʀ</div><p style='color:white;'>Up Town Ellah Abad</p></div>
""", unsafe_allow_html=True)

# واٹس ایپ بٹن
st.markdown('<a href="https://wa.me/923084779900" class="whatsapp-btn">🟢 Order via WhatsApp: 0308-4779900</a>', unsafe_allow_html=True)

# --- مینیو سیکشنز ---

# 1. برگرز
st.markdown("<div class='category-header'>🍔 BURGERS & SANDWICHES</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("● **Zinger Burger**: <span class='price-tag'>Rs. 380</span>", unsafe_allow_html=True)
    st.markdown("● **Cheese Zinger**: <span class='price-tag'>Rs. 450</span>", unsafe_allow_html=True)
    st.markdown("● **Tower Burger**: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)
    st.markdown("● **Pizza Burger**: <span class='price-tag'>Rs. 550</span>", unsafe_allow_html=True)
with col2:
    st.markdown("● **Chicken Burger**: <span class='price-tag'>Rs. 300</span>", unsafe_allow_html=True)
    st.markdown("● **Patty Burger**: <span class='price-tag'>Rs. 220</span>", unsafe_allow_html=True)
    st.markdown("● **Club Sandwich**: <span class='price-tag'>Rs. 750</span>", unsafe_allow_html=True)

# 2. پیزا (Up Town Pizza Treat)
st.markdown("<div class='category-header'>🍕 UP TOWN PIZZA TREAT</div>", unsafe_allow_html=True)
st.write("**Flavors:** Chicken Tikka, Fajita, BBQ, Afghani, Veggie")
cols = st.columns(4)
sizes = [("Small", "600/780"), ("Medium", "1100/1400"), ("Large", "1500/1850"), ("Family", "1900/2400")]
for i, (size, price) in enumerate(sizes):
    cols[i].metric(size, f"Rs. {price}")

# 3. ہاٹ ڈیلز
st.markdown("<div class='category-header'>🎁 EXCLUSIVE HOT DEALS</div>", unsafe_allow_html=True)
d1, d2 = st.columns(2)
with d1:
    st.success("🔥 **Deal 1**: 2 Zinger + Fries + Drink = **Rs. 1000**")
    st.success("🔥 **Deal 2**: 2 Chicken Burger + Fries + Drink = **Rs. 850**")
with d2:
    st.success("🔥 **Deal 3**: Large Pizza + 1L Drink = **Rs. 1650**")
    st.success("🔥 **Deal 6**: 3 Zinger + Mayo Fries + Pasta + 1L Drink = **Rs. 2000**")

# 4. سائڈز اور پاستا
st.markdown("<div class='category-header'>🍟 SIDES & PASTA</div>", unsafe_allow_html=True)
s1, s2 = st.columns(2)
with s1:
    st.markdown("● **Fries (Regular)**: <span class='price-tag'>Rs. 200</span>", unsafe_allow_html=True)
    st.markdown("● **Loaded Fries**: <span class='price-tag'>Rs. 500</span>", unsafe_allow_html=True)
with s2:
    st.markdown("● **Chicken Pasta**: <span class='price-tag'>Rs. 600</span>", unsafe_allow_html=True)
    st.markdown("● **Oven Baked Pasta**: <span class='price-tag'>Rs. 750</span>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: gray;'>Open: 12:00 PM - 12:00 AM</p>", unsafe_allow_html=True)
