from pylab import *
import hello

pix = zeros((80, 640, 3), 'uint8')
pix[:,:,0] = 255
pix[:,:,1] = 128 + 50 * randn(80,640);
pix[:,:,2] = 0

rr = hello.RingRenderer()
rr.cx = 400
rr.cy = 40
rr.render(pix, 90)

imshow(pix, interpolation='nearest')

show()
