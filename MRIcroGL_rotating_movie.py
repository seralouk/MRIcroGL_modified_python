#* Author: Serafeim Loukas, EPFL, serafeim.loukas@epfl.ch, 28 Feb 2020
#* Script to save png rotated rendered brain images -- to be used for gif construction

import gl
gl.resetdefaults()

#* Where to save results
save_to = '/Users/loukas/Documents/MRIcroGL_movie/results/' # do not forget the last slash

#* Set rendering view mode
gl.view(64)

#* Open background image
gl.loadimage('spm152')

#* Open overlay: show positive regions
gl.overlayload('/Users/loukas/Documents/MRIcroGL_movie/AAL_masked_region_32.nii')
#gl.minmax(1, 4, 4)
#gl.opacity(1,50)

#* Do not show the colorbar
gl.colorbarposition(0)

# Rotation parameter x, wait and save as png
x0=1 # from 
x = 360 # to 
step = 20 # with step
for x in range(x0,x,step):
  gl.azimuthelevation(x, 0)
  #* 'wait' command is optional
  gl.wait(10)
  #* change resolution
  gl.bmpzoom(0.5)
  #* Save rotated rendered brain views
  gl.savebmp(save_to + 'rot_' + str(x) + '.png')

#* Create a gif using imagemagick or similar software¨
#* Call the following commad from the terminal after CDing into 'save_to' directory
#convert -delay 90 *rot_* rotating_brain.gif