def hide_card(card_number):
    num = card_number.replace(" ", "")[-4:]
    output = '************' + num
    return output

