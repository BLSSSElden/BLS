def count_vowels(text:str) -> int:
    vowels = set("aeiouAEIOUаеёиоуыэюяАЕЁЮЯЫУЭ")
    return sum([1 for char in text if char in vowels])