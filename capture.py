import cv2
from PIL import Image
camera_port = 0
def takePhoto(file):
	camera = cv2.VideoCapture(camera_port)
	return_value, image = camera.read()
	del(camera)
	image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	pil_im = Image.fromarray(image)
	pil_im.thumbnail((256, 256), Image.ANTIALIAS)
	pil_im = pil_im.convert('1') # convert image to black and white
	pil_im.show()
	pil_im.save(file)
takePhoto('test.jpeg')
