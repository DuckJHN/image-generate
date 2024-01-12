import argparse


def check_input_arguments(parse, args):
    if not (args.folder_path or args.image_path):
        parse.error(
            'At least one of the arguments "input_path" or "image_path" is required.')


def check_enough_params(parser, args, param_name):
    if getattr(args, param_name) and len(getattr(args, param_name)) < 2:
        parser.error(f"Enough params: min or max : {param_name}")


class ErrorCatchingArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise Exception(f'Exiting because of an error: {message}')
        exit(status)
