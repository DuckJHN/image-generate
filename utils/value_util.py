def getNumberOrDefault(*self, value, default):
    value = int(value) if value is not None else default
    return value


def getBooleanOrDefault(*self, value):
    value = bool(value) if value is not None else False
    return value
