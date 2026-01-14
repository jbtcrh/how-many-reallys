import math

STANDALONE_PREFIXES = ["m", "b", "tr", "quadr", "quint", "sext", "sept", "oct", "non"]
SINGLE_PREFIXES = ["un", "duo", "tre", "quattuor", "quin", "sex", "septen", "octo", "novem"]
TENS_PREFIXES = ["dec", "vigint", "trigint", "quadragint", "quinquagint", "sexagint", "septuagint", "octogint",
                 "nonagint"]
HUNDREDS_PREFIXES = ["cent", "ducent", "trecent", "quadrigent", "quingent", "sescent", "septingent", "octingent",
                     "nongent"]


def get_illion_prefix(number: int) -> str:
    def get_illion_part(digit: int, prefixes: list[str]) -> str:
        number_part = int(number / (10 ** (digit - 1))) % 10
        return "" if number_part == 0 else prefixes[number_part - 1]

    if number < 10: return STANDALONE_PREFIXES[number - 1]
    return (get_illion_part(1, SINGLE_PREFIXES) +
            get_illion_part(2, TENS_PREFIXES) +
            get_illion_part(3, HUNDREDS_PREFIXES))


def format_illions(number: int) -> str:
    if number < 1_000_000: return str(number)
    illion_number = int(math.log10(number) / 3) - 1
    illion_prefix = get_illion_prefix(illion_number)
    illion_digits = number / (10 ** ((illion_number + 1) * 3))
    return f'{illion_digits:.2f} {illion_prefix}illion'
