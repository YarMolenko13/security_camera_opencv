import argparse

FACE_CASCADE_NAME = 'haarcascade_frontalface_alt.xml'
EYES_CASCADE_NAME = 'haarcascade_eye_tree_eyeglasses.xml'
SECONDS_TO_RECORD_AFTER_DETECTION = 6

FACE_HIGHLIGHT_COLOR: tuple
FACE_IS_ELIPSE: bool
FACE_LINE_THICKNESS = 1

EYES_HIGHLIGHT: bool
EYES_HIGHLIGHT_COLOR: tuple
EYES_LINE_THICKNESS = 1

TEXT_COLOR: tuple

parser = argparse.ArgumentParser(description='Security camera project')
parser.add_argument('--face-is-el', help='face highlight by elipse', default="False")
parser.add_argument('--face-h-color', help='face color BGR touple (like "255,23,10")', default='0, 0, 255')
parser.add_argument('--eyes-highlight', help='eyes highlight', default="True")
parser.add_argument('--eyes-h-color', help='eyes color BGR touple (like "255,23,10")', default='0, 255, 0')
parser.add_argument('--text-color', help='text color BGR touple (like "255,23,10")', default='255, 78, 33')
args = parser.parse_args()

FACE_IS_ELIPSE = True if args.face_is_el == 'True' else False
FACE_HIGHLIGHT_COLOR = tuple(map(lambda x: int(x.strip()), args.face_h_color.split(',')))
EYES_HIGHLIGHT = False if args.eyes_highlight == 'False' else True
EYES_HIGHLIGHT_COLOR = tuple(map(lambda x: int(x.strip()), args.eyes_h_color.split(',')))
TEXT_COLOR = tuple(map(lambda x: int(x.strip()), args.text_color.split(',')))

print(args)

# python main.py --face-h-color 255,255,255 --eyes-h-color 128,255,255
# python main.py --face-h-color 36,255,238 --eyes-h-color 131,55,54 --face-is-el True --text-color 0,0,0