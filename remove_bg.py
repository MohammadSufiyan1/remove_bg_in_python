from rembg import remove
from PIL import Image
input_img_location = 'C:\\Users\\G.S Technology\\Desktop\\srk.jpg'         #Input Image Path
output_img_location = 'C:\\Users\\G.S Technology\\Desktop\\shahrukh1.png'  #Edit the output path and name of the image use .png in the extension name
input = Image.open(input_img_location) 
output = remove(input)                 
output.save(output_img_location)      
