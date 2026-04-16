import streamlit as st
import random

st.set_page_config(page_title="IAGEO Mobile", layout="centered")

# =========================
# STYLE MOBILE
# =========================
st.markdown("""
<style>
.big-text {font-size:28px !important; text-align:center;}
.btn {width:100%; height:60px; font-size:20px;}
</style>
""", unsafe_allow_html=True)

st.title("🎮 IAGEO Mobile")

# =========================
# INIT
# =========================
if "xp" not in st.session_state:
    st.session_state.xp = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "coins" not in st.session_state:
    st.session_state.coins = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "avatar" not in st.session_state:
    st.session_state.avatar = "👶"

if "answered" not in st.session_state:
    st.session_state.answered = False

if "result" not in st.session_state:
    st.session_state.result = ""

# =========================
# AVATAR CUSTOM
# =========================
st.markdown("## 👤 Ton Avatar")

avatar_choice = st.selectbox(
    "Choisir ton avatar",
    ["👶", "🧒", "🧠", "🦸", "🤖"]
)

st.session_state.avatar = avatar_choice

st.markdown(f"<div class='big-text'>{st.session_state.avatar}</div>", unsafe_allow_html=True)

# =========================
# BARRE PROGRESSION
# =========================
xp_needed = st.session_state.level * 50

st.write(f"⭐ XP : {st.session_state.xp}/{xp_needed}")
st.write(f"🔥 Streak : {st.session_state.streak}")
st.write(f"💰 Coins : {st.session_state.coins}")

st.progress(st.session_state.xp / xp_needed)

st.markdown("---")

# =========================
# QUESTION
# =========================
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 5)

if "b" not in st.session_state:
    st.session_state.b = random.randint(1, 5)

a = st.session_state.a
b = st.session_state.b

st.markdown("## 🌍 Mission")
st.write("👾 Un monstre apparaît !")

st.markdown(f"<div class='big-text'>⚔️ {a} × {b} = ?</div>", unsafe_allow_html=True)

rep = st.number_input("", min_value=0, step=1)

# =========================
# ACTION
# =========================
if not st.session_state.answered:

    if st.button("🚀 ATTAQUER"):

        correct = a * b

        if rep == correct:
            st.session_state.result = "win"
            st.session_state.xp += 10
            st.session_state.streak += 1
            st.session_state.coins += 5
        else:
            st.session_state.result = "lose"
            st.session_state.streak = 0

        st.session_state.answered = True
        st.rerun()

# =========================
# RESULTAT
# =========================
if st.session_state.answered:

    if st.session_state.result == "win":
        st.success("💥 Victoire !")
        st.balloons()
    else:
        st.error("😢 Raté !")

    st.markdown(f"<div class='big-text'>👉 {a} × {b} = {a*b}</div>", unsafe_allow_html=True)

    # =========================
    # COFFRE
    # =========================
    if st.session_state.streak >= 3:
        if st.button("🎁 OUVRIR COFFRE"):
            reward = random.randint(10, 30)
            st.session_state.coins += reward
            st.success(f"💰 +{reward} coins")

    # =========================
    # NEXT
    # =========================
    if st.button("➡ CONTINUER"):

        if st.session_state.xp >= xp_needed:
            st.session_state.level += 1
            st.session_state.xp = 0

        st.session_state.a = random.randint(1, 12)
        st.session_state.b = random.randint(1, 12)
        st.session_state.answered = False

        st.rerun()