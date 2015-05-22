# This demo make a baoman emotics using face extractor
from extract_face import extract_face
from baozou_maker import make_baoman, turn_to_gray

img_path = 'yaomin.jpg'
# accept <image path> and save new image in 'yaominface.png'
extract_face(img_path)
# accept <image path> and save new image in 'yaominface_gray.png'
turn_to_gray(img_path.split('.')[0] + 'face.png')
# accpet <image path>, contrastness and brightness
# and save new image in 'baoman_panda.png' 
make_baoman(img_path.split('.')[0] + 'face_gray.png', 1.3, 2.3)
