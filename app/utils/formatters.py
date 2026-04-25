from decimal import Decimal


def money(value):
    amount = Decimal(value or 0)
    formatted = f"{amount:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatted}"
