#@ ImagePlus(label="Image to process: ") imp
#@ BigDecimal(label="Final width (in): ", value=0) final_width
#@ BigDecimal(label="Final height (in): ", value=0) final_height
#@ BigDecimal(label="DPI: ") final_dpi
#@ UIService ui
#@ LogService log

import ij.IJ

error = False

final_width = final_width.floatValue()
final_height = final_height.floatValue()
aspect_ratio = float(imp.getWidth())/float(imp.getHeight())

if (final_width != 0) & (final_height == 0):
    final_height = final_width/aspect_ratio
elif (final_height != 0) & (final_width == 0):
    final_width = final_height*aspect_ratio
else:
    log.warn("Set only one dimension to be changed!")
    log.warn("The dimension to automatically determine must be set to 0.")
    error=True

log.info("Final Height (in): %s" % final_height)
log.info("Final Width (in): %s" % final_width)

if not error:
    pixel_width = final_width * final_dpi.floatValue()
    pixel_height = final_height * final_dpi.floatValue()
    log.info("Pixel Width: %s" % pixel_width)
    log.info("Pixel Height: %s" % pixel_height)

    imp_interp = ij.IJ.run(imp, "Scale...", "x=- y=- width="+str(pixel_width)+" height="+str(pixel_height)+" interpolation=None create title=Interpolated");
    ij.IJ.run(imp_interp, "Set Scale...", "distance="+str(final_dpi)+" known=1 unit=inch");
