#!/usr/bin/env python
# -*- coding: utf8 -*-

"""

donc algo par tri ca doit etre pas mal
15:16
premiere ligne des gros
15:16
genre si ta surface totale c S
15:16
tu mets 3/2 * sqrt(S) en base
15:16
tu mets les gros en ligne
15:17
tu croppes qd t trop pres du bord
15:17
et tu entasse le reste
15:17
(les gros; dans l'ordre de la hauteur plutot)

"""

__author__ = "mlecarme"
__version__ = "0.2"

import Image
import ImageDraw
import glob
import os
import os.path
import mimetypes


class MultiMap:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data.setdefault(key, []).append(value)

    def __getitem__(self, key):
        return self.data[key]

    def __repr__(self):
        return str(self.data)

    def keys(self):
        return self.data.keys()

    def max(self):
        return self.data[max(self.data.keys())]


class Bundle:
    """
    [TODO] using a template for css and html
    """
    def __init__(self):
        self.images = set()
        self.byWidth = MultiMap()
        self.byHeight = MultiMap()

    def add(self, path, image):
        img = Img(path, image)
        self.images.add(img)
        w, h = image.size
        self.byWidth.add(w, img)
        self.byHeight.add(h, img)

    def __repr__(self):
        return "<Bundle images:%s byWidth:%s byHeight:%s>" % (str(self.images), str(self.byWidth), str(self.byHeight))

    def larger(self):
        return max(self.byWidth.keys())

    def build(self):
        height = 0
        width = 0
        stuff = self.byHeight.keys()
        maxWidth = max(self.byWidth.keys())
        width = maxWidth
        stuff.sort()
        stuff.reverse()
        surface = 0
        lineH = 0
        for s in stuff:
            for img in self.byHeight[s]:
                w, h = img.image.size
                surface += w * h
                if h > lineH:
                    lineH = h
                if (w + width) > maxWidth:
                    height += lineH
                    width = 0
                    lineH = h
                width += w
        height += lineH - stuff[0]
        print  "size:", maxWidth, height
        print "optimisation :", (surface * 1.0 / (maxWidth * height)) * 100
        big = Image.new("RGBA", (maxWidth, height))
        height = 0
        width = 0
        lineH = 0
        css = """
.redborder {
    border: 1px dotted red;
}
        """
        html = """
<html>
<head>
<link rel="stylesheet" id="csspersolink" type="text/css" href="bundle.css" />
</head>
<body bgcolor="lime">
<h1>Bundler</h1>

        """
        for s in stuff:
            print "height:", s
            for img in self.byHeight[s]:
                w, h = img.image.size
                if h > lineH:
                    lineH = h
                if (width + w) > maxWidth:
                    height += lineH
                    width = 0
                    lineH = h
                #print "pasting", big, (w,h), (width, height)
                big.paste(img.image, (width, height))
                idt = img.path.replace("/", "_")
                idt = idt.replace(" ", "_")
                ids = idt.split('.')
                if len(ids) > 1:
                    idt = ".".join(ids[:-1])
                css += """
.%s {
    background: transparent url(bundle.png) no-repeat -%ipx -%ipx;
    width: %ipx;
    height: %ipx;
}
                """ % (idt, width, height, w, h)
                html += """<h2>%s</h2><div class="%s redborder">&nbsp</div>
""" % (img.path, idt)
                width += w
        big.save('bundle.png')
        f = open('bundle.css', 'w')
        f.write(css)
        f.close()
        html += """
        </body>
</html>
"""
        f = open('bundle.html', 'w')
        f.write(html)
        f.close()


def redBorder(im):
    w, h = im.size
    w -= 1
    h -= 1
    draw = ImageDraw.Draw(im)
    color = 255
    #rectangle
    draw.line((0, 0, 0, h), fill=color)
    draw.line((0, h, w, h), fill=color)
    draw.line((w, h, w, 0), fill=color)
    draw.line((w, 0, 0, 0), fill=color)
    del draw


class Img:
    def __init__(self, path, image):
        self.path = path
        self.image = image

    def __repr__(self):
        return "<Img path:%s image:%s>" % (str(self.path), str(self.image))


def bundle_pattern(pattern):
    b = Bundle()
    print pattern
    for name in glob.iglob(pattern):
        print name
        im = Image.open(name)
        #redBorder(im)
        b.add(name, im)
    b.build()


def bundle(folder):
    if not os.path.isdir(folder):
        raise Exception("I need a folder")
    Image.preinit()
    mimes = Image.MIME.values()
    b = Bundle()
    for stuff in os.listdir(folder):
        mime = mimetypes.guess_type(stuff)
        #print mime, stuff
        if mime[0] in mimes:
            print stuff
            path = os.path.join(folder, stuff)
            im = Image.open(path)
            b.add(path, im)
    b.build()

if __name__ == '__main__':
    bundle("/Applications/TextMate.app/Contents/Resources")
