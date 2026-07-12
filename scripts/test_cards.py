from services.cards import get_next_card

card = get_next_card(
    user_id=1,
    destination_id=1
)

print(card)