from __init__ import Bundle

"""
[TODO] less ridiculous test
"""
def testCroix():
	cpt = 0
	def imageFactory(size):
		global cpt
		cpt += 1
		im = Image.new("RGB", size)
		w,h = size
		w -= 1
		h -=1
		draw = ImageDraw.Draw(im)
		#rectangle
		draw.line((0,0, 0,h), fill=128)
		draw.line((0,h, w,h), fill=128)
		draw.line((w,h, w,0), fill=128)
		draw.line((w,0, 0,0), fill=128)
		#cross
		draw.line((0,0, w,h), fill=128)
		draw.line((0,h, w,0), fill=128)
		del draw
		im.save("%i.png" % cpt)
		return im

	b = Bundle()
	b.add("bandeau", imageFactory((320, 24)))
	b.add("icone1" ,imageFactory((24, 24)))
	b.add("icone2" ,imageFactory((24, 24)))
	b.add("icone3" ,imageFactory((24, 24)))
	b.add("icone4" ,imageFactory((24, 24)))
	b.add("icone5" ,imageFactory((24, 24)))
	b.add("GrosIcone" ,imageFactory((32, 32)))
	b.add("pub" ,imageFactory((128, 64)))
	b.add("pub" ,imageFactory((150, 60)))

	print b
	print b.larger()
	b.build()

if __name__ == '__main__':
	testCroix()