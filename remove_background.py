import os
import cv2


from PIL import Image
from rembg import remove


if not os.path.exists('input'):
    os.mkdir('input')

if not os.path.exists('output'):
    os.mkdir('output')


for input_image_name in os.listdir('input'):
    print(f'Opening image "{input_image_name}"')
    input_file = Image.open(f'input/{input_image_name}')
    
    print(f'Removing the image background')
    output_file = remove(input_file)
    
    print(f'Converting the image')
    converted_file = output_file.convert('RGB')
    
    input_image_name = input_image_name.replace('.jpg', '.png')
    input_image_name = input_image_name.replace('.jpeg', '.png')
    input_image_name = input_image_name.replace('.JPG', '.png')
    input_image_name = input_image_name.replace('.JPEG', '.png')
    input_image_name = input_image_name.replace('.jfif', '.png')
    input_image_name = input_image_name.replace('.gif', '.png')
    
    print(f'Saving the image in the output folder')
    converted_file.save(f'output/black_{input_image_name}')
    
    print(f'Reading the image')
    src = cv2.imread(f'output/black_{input_image_name}', 1)
    
    print(f'Convert image to image gray')
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    print(f'Applying thresholding technique')
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    
    print(f'Using cv2.split() to split channels of coloured image')
    b, g, r = cv2.split(src)
    
    print(f'Making list of Red, Green, Blue Channels and alpha')
    rgba = [b, g, r, alpha]
    
    print(f'Using cv2.merge() to merge rgba into a coloured/multi-channeled image')
    dst = cv2.merge(rgba, 4)
    
    print(f'Writing and saving to a new image')
    cv2.imwrite(f'output/transparent_{input_image_name}', dst)
    
    print(f'')