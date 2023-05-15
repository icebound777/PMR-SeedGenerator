from db.option import Option


def get_option_default_value(option_str: str):
    return Option.get(Option.name == option_str).value
