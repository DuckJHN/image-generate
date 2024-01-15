
import argparse
import generate_image as generate_image
import error.argument_parse as exception
from error.argument_parse import check_input_arguments, check_enough_params
from enumeration.blur_enum import list_type
from handle.argument import param_cli

if __name__ == '__main__':

    parse = argparse.ArgumentParser(prog='SPARKMINDS',
                                    description='''Apply new feature to an image. 
                                    Features: rotate, resize, flip, noise, brightness, blur.''',
                                    epilog='''Thank you.''')

    exception.ErrorCatchingArgumentParser(parse)

    # Require
    parse.add_argument('--folder_path', nargs='?',
                       help='Path to the input folder images')
    parse.add_argument('--image_path', nargs='?',
                       help='Path to the input image')

    parse.add_argument('--output_path', help='Path to the output image')

    parse.add_argument('--limit', help='Limit image generate', default=5)

    # Options
    parse.add_argument('--resize', type=int, nargs='*', default=100,
                       help='Resize percentage in range [10 - 200].')
    parse.add_argument('--crop', type=int, nargs='?', default=100,
                       help='Cropped image by percentage (default: no Change)')

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
    parse.add_argument('--color', action=argparse.BooleanOptionalAction,
                       help='Turn off change color of images', default=False)
    parse.add_argument('--noise', type=int, nargs='*', default=0,
                       help='Level noise in range [0 - 100]')
    parse.add_argument('--blur', nargs='?', default='other',
                       help='Blur type in list [Gaussian, Median, Average]', choices=list_type())
    parse.add_argument('--kn', type=int, default=5,
                       help='Kernel blur default = 5')

    args = parse.parse_args()
    check_input_arguments(parse, args)

    """_summary_
        param required:
            input_path, output_path, limit
    """

    args = param_cli.check_and_set_default(parse, args)
    folder_path = args.folder_path
    image_path = args.image_path
    output_path = args.output_path
    limit = args.limit

    """_summary_
        param optional:
            For params: noise, resize, rotate, brightness, contrast
            1. If empty will take default parameters
            2. Complete the min and max fields
    """

    resize_percentage = args.resize
    crop_auto = args.crop
    rotation_angle = args.rotation

    constrast = args.constrast

    brightness = args.brightness
    color = args.color

    flip_horizontal = args.flip_horizontal
    flip_vertical = args.flip_vertical
    noise = args.noise

    blur_type = args.blur
    kernel = args.kn

    params_to_check = ['noise', 'resize',
                       'rotation', 'brightness', 'constrast']
    for param in params_to_check:
        check_enough_params(parse, args, param)

    if folder_path is not None:
        generate_image.generate_from_folder(input_path=folder_path, output_path=output_path,
                                            horizontal=flip_horizontal, vertical=flip_vertical,
                                            blur_type=blur_type, max_kernel=kernel,
                                            noise_max_level=noise,
                                            crop=crop_auto,
                                            brightness=brightness, color=color, constrast=constrast,
                                            max_percentage=resize_percentage, max_angle=rotation_angle,
                                            limit=limit)
    elif image_path is not None:
        generate_image.process_image(image_path=image_path, output_path=output_path,
                                     horizontal=flip_horizontal, vertical=flip_vertical,
                                     blur_type=blur_type, max_kernel=kernel,
                                     noise_max_level=noise,
                                     crop=crop_auto,
                                     brightness=brightness, color=color, constrast=constrast,
                                     max_percentage=resize_percentage, max_angle=rotation_angle,
                                     limit=limit)
