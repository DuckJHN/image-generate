import argparse
from constant.variable import *


def process_brightness(value):
    if value is None:
        return 60
    try:
        brightness = int(value)
        return max(0, min(brightness, 100))
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Brightness must be an integer in the range [0 - 100]")


def check_and_set_default(parse, args):
    if not args.noise:
        args.noise = [MIN_NOISE, MAX_NOISE]

    if not args.resize:
        args.resize = [MIN_RESIZE, MAX_RESIZE]

    if not args.rotation:
        args.rotation = [MIN_ROTATION, MAX_ROTATION]

    return args
