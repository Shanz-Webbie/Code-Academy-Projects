import pyaztro

def get_sign():
    astrology_sign = input("Enter your Astrology Sign:")
    return astrology_sign

def get_valadated_date():
    selected_date = input("Do you want your horoscope from yesterday, today, or tomorrow?")
    return selected_date


def main():
    astrology_sign = get_sign()
    selected_date = get_valadated_date()
    horoscope = pyaztro.Aztro(day= selected_date, sign= astrology_sign)
    print(horoscope.description)


main()