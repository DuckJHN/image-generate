import argparse
from constant.message import *


def check_input_arguments(parse, args):
    if not (args.folder_path or args.image_path):
        parse.error(INPUT_PATH_REQUIRED)


def check_enough_params(parser, args, param_name):
    if getattr(args, param_name) and len(getattr(args, param_name)) < 2:
        parser.error(f"Enough params: min or max of {param_name}")


class ArgumentParserError(Exception):
    pass


class ErrorCatchingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)
