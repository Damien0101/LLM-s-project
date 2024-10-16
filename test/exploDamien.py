import os
from pdf2image import convert_from_path

rootdir = '/home/servietske/Desktop/Becode/LLM-s-project/data/pdf'

# Walk through all files in the directory
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # Check if the file has a .pdf extension
        if file.endswith('.pdf'):
            # Create the full original path
            old_file_path = os.path.join(subdir, file)
            
            # Convert PDF to images (one image per page)
            images = convert_from_path(old_file_path)
            
            # Save each page as a PNG with unique filenames based on page number
            for i, image in enumerate(images):
                # Create a new filename that includes the page number to prevent overwriting
                new_file_path = os.path.join(subdir, file.replace('.pdf', '.png'))
                
                # Save the converted image as PNG
                image.save(new_file_path, 'PNG')
                
                print(f"Saved: {new_file_path}")
