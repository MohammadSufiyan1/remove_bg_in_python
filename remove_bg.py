from rembg import remove
from PIL import Image
input_img_location = 'C:\\Users\\G.S Technology\\Desktop\\srk.jpg' #input image location (path)
output_img_location = 'C:\\Users\\G.S Technology\\Desktop\\shahrukh1.png' #ouput image loaction(path) extention name use .png
input = Image.open(input_img_location) #image open
output = remove(input)                 #remove background process
output.save(output_img_location)       #final store data remove background image and check your image output location
