import math

STANDALONE_PREFIXES = ["", "m", "b", "tr", "quadr", "quint", "sext", "sept", "oct", "non"]
SINGLE_PREFIXES = ["", "un", "duo", "tre", "quattuor", "quin", "se", "septe", "octo", "nove"]
TENS_PREFIXES = ["", "deci", "viginti", "triginta", "quadraginta", "quinquaginta", "sexaginta", "septuaginta",
                 "octoginta",
                 "nonaginta"]
HUNDREDS_PREFIXES = ["", "centi", "ducenti", "trecenti", "quadrigenti", "quingenti", "sescenti", "septingenti",
                     "octingenti",
                     "nongenti"]

SINGLE_JOINERS = ["", "", "", "sx", "", "", "sx", "mn", "", "mn"]
TENS_JOINERS = ["", "n", "ms", "ns", "ns", "ns", "n", "n", "mx", ""]
HUNDREDS_JOINERS = ["", "nx", "n", "ns", "ns", "ns", "n", "n", "mx", ""]


def get_illion_prefix(number: int) -> str:
    def get_number_part(digit: int) -> int:
        return int(number / (10 ** (digit - 1))) % 10

    if number < 10: return STANDALONE_PREFIXES[number]
    single_number_part = get_number_part(1)
    tens_number_part = get_number_part(2)
    hundreds_number_part = get_number_part(3)

    single_part = SINGLE_PREFIXES[single_number_part]
    tens_part = TENS_PREFIXES[tens_number_part]
    hundreds_part = HUNDREDS_PREFIXES[hundreds_number_part]

    if single_number_part > 0 and (tens_number_part + hundreds_number_part) > 0:
        joiner_list = HUNDREDS_JOINERS[hundreds_number_part] if tens_number_part == 0 else TENS_JOINERS[
            tens_number_part]
        joiner = list(set(SINGLE_JOINERS[single_number_part]).intersection(set(joiner_list)))
        if len(joiner) > 0:
            single_part += joiner[0]

    result = single_part + tens_part + hundreds_part
    if result.endswith(("a", "i")):
        result = result[:-1]
    return result


def format_illions(number: int) -> str:
    if number < 1_000_000: return str(number)
    illion_number = int(math.log10(number) / 3) - 1
    illion_prefix = get_illion_prefix(illion_number)
    illion_digits = number / (10 ** ((illion_number + 1) * 3))
    return f'{illion_digits:.2f} {illion_prefix}illion'
