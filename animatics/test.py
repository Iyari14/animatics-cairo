import cairo
import gi
gi.require_version('Rsvg', '2.0')
from gi.repository import Rsvg

# 1. Create a standard Cairo surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 600)
ctx = cairo.Context(surface)

# 2. Paint a clean background
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# 3. Load the compiled SVG file
handle = Rsvg.Handle.new_from_file("formula.svg")

ctx.save()
ctx.translate(100, 100)
ctx.scale(1.5, 1.5)
handle.render_cairo(ctx)
ctx.restore()

surface.write_to_png("output.png")
