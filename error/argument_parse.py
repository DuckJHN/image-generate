import argparse


def check_input_arguments(parse, args):
    if not (args.folder_path or args.image_path):
        parse.error(
            'At least one of the arguments "input_path" or "image_path" is required.')


class ErrorCatchingArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise Exception(f'Exiting because of an error: {message}')
        exit(status)
