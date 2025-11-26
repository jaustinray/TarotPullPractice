tarot_deck = {}

suits = ["Wands", "Cups", "Swords", "Pentacles"]
numbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

major_arcana = [
  "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers",
  "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
  "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
]

suits.each do |suit|
    numbers.each do |number|
        card_name = "#{number} of #{suit}"
        tarot_deck[card_name] = {
            type: "Minor Arcana",
            number: number,
            suit: suit,
        }
    end
end

major_arcana.each do |card_name|
  tarot_deck[card_name] = {
    type: "Major Arcana",
    number: "",
  }
end

# Sample card names
sampled_card_names = tarot_deck.keys.sample(7)

# For each sampled card, randomly decide if it's reversed
random_cards_with_orientation = sampled_card_names.map do |card_name|
  { name: card_name, reversed: [true, false].sample }
end

puts "Your cards are:"
random_cards_with_orientation.each do |card_info|
    output = "- #{card_info[:name]}"
    output += " (Reversed)" if card_info[:reversed]
    puts output
end
