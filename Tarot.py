import streamlit as st
import random

# --- Tarot Deck Configuration ---

MAJOR_ARCANA = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
]

SUITS = ["Wands", "Cups", "Swords", "Pentacles"]
NUMBERS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

def create_tarot_deck():
    """Build the complete 78-card tarot deck."""
    deck = []
    
    # Add Major Arcana
    for card in MAJOR_ARCANA:
        deck.append({
            "name": card,
            "type": "Major Arcana",
            "suit": None,
            "number": None
        })
    
    # Add Minor Arcana
    for suit in SUITS:
        for number in NUMBERS:
            deck.append({
                "name": f"{number} of {suit}",
                "type": "Minor Arcana",
                "suit": suit,
                "number": number
            })
    
    return deck

def draw_reading(deck, num_cards=7):
    """Draw random cards with random orientations."""
    drawn = random.sample(deck, num_cards)
    reading = []
    
    for card in drawn:
        reading.append({
            **card,
            "reversed": random.choice([True, False])
        })
    
    return reading

def card_display(card):
    """Format card for display."""
    emoji = "🔄" if card["reversed"] else "⬆️"
    status = "Reversed" if card["reversed"] else "Upright"
    return f"{emoji} **{card['name']}** ({status})"

# --- Streamlit App ---

st.set_page_config(page_title="Tarot Reader", page_icon="🔮")
st.title("🔮 Tarot Card Reader")
st.markdown("Draw 7 cards for your reading. Click below to shuffle and reveal.")

# Initialize session state
if 'reading' not in st.session_state:
    st.session_state.reading = None

# Draw button
if st.button("🎴 Draw Cards", type="primary", use_container_width=True):
    deck = create_tarot_deck()
    st.session_state.reading = draw_reading(deck, 7)
    st.rerun()

# Display reading
if st.session_state.reading:
    st.divider()
    st.subheader("Your Reading")
    
    # Display cards in a grid
    cols = st.columns(2)
    for i, card in enumerate(st.session_state.reading):
        with cols[i % 2]:
            st.info(card_display(card))
    
    # Summary
    st.divider()
    upright = sum(1 for c in st.session_state.reading if not c["reversed"])
    reversed_count = 7 - upright
    st.metric("Upright Cards", upright)
    st.metric("Reversed Cards", reversed_count)
