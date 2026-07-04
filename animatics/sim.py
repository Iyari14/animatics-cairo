import cairo

WIDTH = 1920
HEIGHT = 1080

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

context.set_source_rgb(0.98, 0.96, 0.91)
context.paint()

surface.write_to_png("frame.png")

class Sim:
  def construction(self, mobjects=[]):
    pass
  def run(self):
    WIDTH = 1920
    HEIGHT = 1080
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    context = cairo.Context(surface)
    context.set_source_rgb(0.98, 0.96, 0.91)
    context.paint()
    surface.write_to_png("frame0.png")
