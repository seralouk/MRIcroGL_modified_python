#* Author: Serafeim Loukas, EPFL, serafeim.loukas@epfl.ch, 17 June 2020
#* Script to overlay an activation map onto the spm152 structural volume, with 
#* specific predefined parameters and settings.
import gl, os
gl.resetdefaults()

#* Where to save results
save_to = '/Users/loukas/Desktop/' # do not forget the last slash

#* Set Multi panel view mode
gl.view(16)

#* Changes the background color, for example backcolor(255, 0, 0) will set a bright red background
gl.backcolor(255, 255, 255)

#* Open background image
gl.loadimage('spm152')

#* Do not smooth the overlay when loading it
gl.overlayloadsmooth(0)

#* Open overlay: show positive regions
gl.overlayload('/Users/loukas/Desktop/angle_map_1.nii')

#* Make the layer (0 for background, 1 for 1st overlay) transparent(0), translucent (~50) or opaque (100).
gl.opacity(1,60)

#* Set colorbar position (0=off, 1=top, 2=right).
gl.colorbarposition(2)

#* Set the colorscheme for the target overlay (0=background layer) to a specified name.
gl.colorname(1,'myHSV')

#* Sets the color range for the overlay (layer 0 = background).
gl.minmax(1, 0, 6.283)

#* Save rotated rendered brain views
gl.savebmp(save_to + 'my_angle_map' + '.png')
