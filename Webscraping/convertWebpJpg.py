import os
from PIL import Image

rootdir = 'Sort'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		if '.webp' in file:
			try:
				filename = os.path.join(subdir, file)
				im = Image.open(filename).convert("RGB")
				im.save(filename.split('.')[0]+".jpg", "jpeg")				
			except Exception as ex:
				print (ex)
			
			try:
				im.save(filename.split('.')[0]+".png", "png")
			except Exception as ex:
				print (ex)
				
