# This demo make a baoman emotics using face extractor
from extract_face import extract_face, extract_five
from baozou_maker import make_baoman, turn_to_gray

img_path = 'yaomin.jpg'
# accept <image path> and save new image in 'yaomin_face.png'
#extract_face(img_path)
extract_five(img_path)
# accept <image path> and save new image in 'yaomin_face_gray.png'
turn_to_gray(img_path.split('.')[0] + '_face.png')
# accpet <image path>, contrastness and brightness
# and save new image in 'yaomin_face_gray_baoman_panda.png' 
make_baoman(img_path.split('.')[0] + '_face_gray.png', 1.3, 2.3)
