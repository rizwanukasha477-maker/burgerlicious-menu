import streamlit as st
import urllib.parse

# یہاں اپنا واٹس ایپ نمبر لکھیں (مثلاً: 923001234567)
MY_NUMBER = "923084779900" 

st.set_page_config(page_title="Burgerlicious", page_icon="🍔", layout="centered")

# ہیڈر
st.markdown(f"<h1 style='text-align: center; color: yellow; background-color: black; padding: 10px; border-radius: 10px;'>Burgerlicious.. FOOD BAR</h1>", unsafe_allow_html=True)
st.write("---")

# مینیو ڈیٹا
items = [
    {"name": "Supreme Pizza", "price": 1200, "cat": "🍕"},
    {"name": "Beef Burger", "price": 650, "cat": "🍔"},
    {"name": "Zinger Burger", "price": 550, "cat": "🍔"},
    {"name": "Loaded Fries", "price": 450, "cat": "🍟"},
    {"name": "White Pasta", "price": 850, "cat": "🍝"},
    {"name": "Drumsticks (3pcs)", "price": 400, "cat": "🍗"},
    {"name": "Nuggets (6pcs)", "price": 300, "cat": "🍗"}
]

if 'cart' not in st.session_state:
    st.session_state.cart = []

# مینیو ڈسپلے
st.subheader("🔥 مینیو سے انتخاب کریں")
for item in items:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"{item['cat']} **{item['name']}** - Rs. {item['price']}")
    with col2:
        if st.button("Add", key=item['name']):
            st.session_state.cart.append(item)

# کارٹ اور چیک آؤٹ
st.write("---")
if st.session_state.cart:
    st.subheader("🛒 آپ کا آرڈر")
    total = 0
    summary = "نئی آرڈر لسٹ:\n"
    for i, entry in enumerate(st.session_state.cart):
        st.write(f"{i+1}. {entry['name']} - Rs. {entry['price']}")
        total += entry['price']
        summary += f"- {entry['name']}\n"
    
    st.write(f"**کل قیمت: Rs. {total}**")
    
    name = st.text_input("آپ کا نام")
    addr = st.text_area("گھر کا پتہ")
    
    if st.button("آرڈر واٹس ایپ کریں"):
        msg = f"{summary}\nکل رقم: {total}\nنام: {name}\nپتہ: {addr}"
        url = f"https://wa.me/{MY_NUMBER}?text={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{url}" target="_blank" style="background-color:green; color:white; padding:15px; text-decoration:none; display:block; text-align:center; border-radius:10px;">کلک کریں اور آرڈر بھیجیں</a>', unsafe_allow_html=True)
