
import argparse
import generate_image as generate_image
import error.argument_parse as exception
from enumeration.blur_enum import list_type
from handle.argument.param_cli import process_brightness


parse = argparse.ArgumentParser(prog='SPARKMINDS',
                                description='''Apply new feature to an image. 
                                Features: rotate, resize, flip, noise, brightness, blur.''',
                                epilog='''Thank you.''')

exception.ErrorCatchingArgumentParser(parse)

parse.add_argument('input_path', help='Path to the input image')

parse.add_argument('output_path', help='Path to the output image')


parse.add_argument('limit', help='Limit image generate', default=5)

# Options
parse.add_argument('--resize', type=int, nargs='*', default=100,
                   help='Resize percentage in range [10 - 200].')
parse.add_argument('--crop', action='store_true',
                   help='Cropped image auto (default: False)')

parse.add_argument('--rotation', type=int, nargs='*', default=0,
                   help='Rotation angle [0-360].')

parse.add_argument('--flip-horizontal',
                   action=argparse.BooleanOptionalAction, help='Flip images horizontally.')
parse.add_argument('--flip-vertical',
                   action=argparse.BooleanOptionalAction, help='Flip images vertically.')

parse.add_argument('--constrast', nargs='*', type=int, default=None,
                   help='Constrast images in range [0 - 100]')


parse.add_argument('--brightness', nargs='*', default=None, type=int,
                   help='Brightness of images in the range [0 - 100]')


parse.add_argument('--noise', type=int, nargs='*', default=0,
                   help='Level noise in range [0 - 100]')
parse.add_argument('--blur', nargs='?', default='Gaussian',
                   help='Blur type in list [Gaussian, Median, Average]', choices=list_type())
parse.add_argument('--kn', type=int, default=5,
                   help='Kernel blur default = 5')


args = parse.parse_args()

"""_summary_
    param required:
        input_path, output_path, limit
"""
input_path = args.input_path
output_path = args.output_path
limit = args.limit

resize_percentage = args.resize
crop_auto = args.crop
rotation_angle = args.rotation

constrast = args.constrast

brightness = args.brightness

flip_horizontal = args.flip_horizontal
flip_vertical = args.flip_vertical
noise = args.noise

blur_type = args.blur
kernel = args.kn


generate_image.generate(input_path=input_path, output_path=output_path,
                        horizontal=flip_horizontal, vertical=flip_vertical,
                        blur_type=blur_type, max_kernel=kernel,
                        noise_max_level=noise,
                        crop=crop_auto,
                        brightness=brightness, constrast=constrast,
                        max_percentage=resize_percentage, max_angle=rotation_angle,
                        limit=limit)
