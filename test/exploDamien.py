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



