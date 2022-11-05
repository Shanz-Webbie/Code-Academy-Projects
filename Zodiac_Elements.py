zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements.update({"energy": "Not a Zodiac element"})

key_to_check = "energy"
if key_to_check in zodiac_elements:
  print(zodiac_elements["energy"])
