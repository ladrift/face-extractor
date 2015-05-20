from extract_face import extract_face
from baozou_maker import make_baoman

img_path = 'yaomin.jpg'
extract_face(img_path)
make_baoman(img_path.split('.')[0] + 'face.png', 1.3, 2.3)
