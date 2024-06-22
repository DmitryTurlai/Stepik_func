def is_valid(pin):
    if len(pin)>=4 and len(pin)<=6 and pin.isdigit() and ' ' not in pin:
        return True
    else:
        return False


