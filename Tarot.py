import streamlit as st
import random

# --- Configuration ---
MAJOR_ARCANA = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
]
SUITS = ["Wands", "Cups", "Swords", "Pentacles"]
NUMBERS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "Queen", "King"]

# Use @st.cache_data so the deck is only built once per session
@st.cache_data
def get_deck():
    deck = [{"name": card, "type": "Major"} for card in MAJOR_ARCANA]
    for suit in SUITS:
        for num in NUMBERS:
            deck.append({"name": f"{num} of {suit}", "type": "Minor"})
    return deck

def draw_reading(num_cards=7):
    deck = get_deck()
    drawn = random.sample(deck, num_cards)
    return [{**card, "reversed": random.choice([True, False])} for card in drawn]

# --- App Interface ---
st.set_page_config(page_title="Tarot Reader", page_icon="🔮")

st.title("🔮 Digital Tarot")
st.caption("Focus on your question, then draw the cards.")

if 'reading' not in st.session_state:
    st.session_state.reading = None

# Draw Button
if st.button("🎴 Shuffle and Draw 7 Cards", type="primary", use_container_width=True):
    with st.spinner("Shuffling the deck..."):
        # Note: No st.rerun() needed here!
        st.session_state.reading = draw_reading(7)

# Display Logic
if st.session_state.reading:
    st.divider()
    
    # Use 4 columns for a more "spread-like" feel
    cols = st.columns(4)
    for i, card in enumerate(st.session_state.reading):
        with cols[i % 4]:
            orientation = "Reversed" if card["reversed"] else "Upright"
            icon = "🔄" if card["reversed"] else "✨"
            
            # Using st.container to create a 'card' look
            with st.container(border=True):
                st.markdown(f"**{card['name']}**")
                st.caption(f"{icon} {orientation}")
    
    # Summary Metrics
    st.divider()
    upright = sum(1 for c in st.session_state.reading if not c["reversed"])
    m1, m2 = st.columns(2)
    m1.metric("Upright Energy", f"{upright}/7")
    m2.metric("Reversed Energy", f"{7-upright}/7")
