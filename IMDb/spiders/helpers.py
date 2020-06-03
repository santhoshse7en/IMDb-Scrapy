import unidecode

errors = {'None': None, 'list': [], 'dict': {}}


def catch(default, func, handle=lambda e: e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except:
        return errors[default]


def digits(text: str) -> bool:
    if text is None:
        return None
    digit = ''.join(i for i in text if i.isdigit())
    if digit.isdigit() == True:
        return int(digit)


def unicode(text: str) -> bool:
    if text is None:
        return None
    return unidecode.unidecode(text).strip()
