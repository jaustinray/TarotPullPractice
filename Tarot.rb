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

def add_suit_and_number(tarot_deck)
    tarot_deck.each do |card_name, attributes|
        if attributes[:type] == "Minor Arcana"
            suit = card_name.match(/(Wands|Cups|Swords|Pentacles)/)[1]
            number = card_name.match(/(Ace|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Page|Knight|Queen|King)/)[1]
            attributes[:suit] = suit
            attributes[:number] = number
        end
    end
end 

cards = tarot_deck.keys + major_arcana

random_cards = cards.sample(7)

puts "Your cards are:"
random_cards.each do |cards|
    puts "- #{cards}"
end