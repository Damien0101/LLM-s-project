import os
from pdf2image import convert_from_path

rootdir = 'data/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.pdf'):
            old_file_path = os.path.join(subdir, file)
            
            images = convert_from_path(old_file_path)
            
            for i, image in enumerate(images):
                new_file_path = os.path.join(subdir, file.replace('.pdf', f'_page_{i + 1}.png'))
                
                image.save(new_file_path, 'PNG')
                
                print(new_file_path)

'''import pytesseract
import cv2

easy_text_path = "/data/image/'BOT_WM hey! Admin Portal FR.png'"
easy_img = cv2.imread(easy_text_path)
text = pytesseract.image_to_string(easy_img)
print(text)'''