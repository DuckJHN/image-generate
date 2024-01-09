import argparse


def process_brightness(value):
    if value is None:
        return 60
    try:
        brightness = int(value)
        return max(0, min(brightness, 100))
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Brightness must be an integer in the range [0 - 100]")
