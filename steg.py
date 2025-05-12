from stegano import lsb

image = 'original.JPG'
new_img = 'newpic.jpg'

msg = 'This is my message'
lsb.hide(image, message=msg).save(new_img)