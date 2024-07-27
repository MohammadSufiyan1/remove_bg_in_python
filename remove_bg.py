from rembg import remove
from PIL import Image
input_img_location = 'C:\\Users\\G.S Technology\\Desktop\\srk.jpg' 
output_img_location = 'C:\\Users\\G.S Technology\\Desktop\\shahrukh1.png' 
input = Image.open(input_img_location) 
output = remove(input)                 
output.save(output_img_location)      
