
import argparse
import generate_image
import error.argument_parse as exception

parse = argparse.ArgumentParser(prog='SPARKMINDS',
                                description='''Apply new feature to an image. 
                                Features: rotate, resize, flip, noise, brightness, blur.''',
                                epilog='''Thank you.''')


exception.ErrorCatchingArgumentParser(parse)

parse.add_argument('input_path', help='Path to the input image')

parse.add_argument('output_path', help='Path to the output image')


parse.add_argument('limit', help='Limit image generate')

# Options
parse.add_argument('--resize', type=float,
                   help='Resize percentage for images.')
parse.add_argument('--crop', type=bool,
                   help='Cropped image auto')

parse.add_argument('--rotation', type=float, help='Rotation angle for images.')

parse.add_argument('--flip-horizontal', '-fh',
                   action=argparse.BooleanOptionalAction, help='Flip images horizontally.')
parse.add_argument('--flip-vertical', '-fv',
                   action=argparse.BooleanOptionalAction, help='Flip images vertically.')

parse.add_argument('--constrast', type=float,
                   help='Constrast images in range [0.1 - 1.5]')


parse.add_argument('--brightness', type=float,
                   help="Brightness images in range [-0.5, 0.5]")

parse.add_argument('--saturation', type=float,
                   help="Saturation images in range [0.1, 0.5]")
parse.add_argument('--hue', type=float,
                   help="hue images in range [-20, 20]")


parse.add_argument('--noise', type=int,
                   help='Level noise in range [0 -100]')
parse.add_argument('--bt', type=str,
                   help='Blur type in list [Gaussian, Median, Average]')
parse.add_argument('--kn', type=int,
                   help='Kernel blur default = 5')


args = parse.parse_args()


input_path = args.input_path
output_path = args.output_path
limit = args.limit

resize_percentage = args.resize
crop_auto = args.crop
rotation_angle = args.rotation
constrast = args.constrast
brightness = args.brightness
saturation = args.saturation
hue = args.hue

flip_horizontal = args.flip_horizontal
flip_vertical = args.flip_vertical
noise = args.noise

blur_type = args.bt
kernel = args.kn

print(f"Input Path: {input_path}")
print(f"Output Path: {output_path}")
print(f"Number of images: {limit}")

print(f"Resize Percentage: {resize_percentage}")
print(f"Constrast image param: {constrast}")
print(f"Brightness image param: {brightness}")

generate_image.generate(input_path=input_path, output_path=output_path,
                        horizontal=flip_horizontal, vertical=flip_vertical,
                        blur_type=blur_type, max_kernel=kernel,
                        noise_max_level=noise,
                        crop=crop_auto,
                        max_percentage=resize_percentage, max_angle=rotation_angle, limit=limit)
