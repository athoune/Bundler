Image bundler
=============

Image bundling is a web optimization for using lot of small picture in a web page.
Image bundler take a folder with a lot of images and build a big one.
With CSS, you crop the part of the big picture you wont to use.
PNG compression is better in a large picture than in the sum of small ones.
Loading a lot of small files is inneficient : there is latency for establishing each connection,
and only few downloads can be parralilized.

GWT use this trick for an efficient toolbar's pictures downloading. 

A simple test with Adium's images :
 - Folder size : 420K
 - Pure image bundle : 248K
 - Optipnged image : 240K

60% diet for all this images.

Install
=======

`PIL`_ is the only dependency, the setup will fetch it.

::

  python setup.py build
  sudo python setup.py install

Usage
=====

::

  bundler someFolder

Bundler will try to open every file it can handle.

You should use `pngcrush`_ or `optipng`_ for a perfect optimisation.

Bundler builds a big PNG file, a cute CSS file and an ugly HTML test file.

Licence
=======

GPL v3.

.. _`PIL`: http://www.pythonware.com/products/pil/
.. _`pngcrush`: http://pmt.sourceforge.net/pngcrush/
.. _`optipng`: http://optipng.sourceforge.net/
