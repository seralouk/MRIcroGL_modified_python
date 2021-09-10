## Author: Serafeim Loukas, EPFL, serafeim.loukas@epfl.ch, 28 Feb 2020

#### MRIcroGL (https://github.com/neurolabusc/MRIcroGL) Modified Python Script to save png rotated rendered brain images -- to be used for gif construction

#### Instructions: 

- 1) Modify the MRIcroGL_rotating_movie.py python script by setting some paths 
- 2) Open MRIcroGL app, 
- 3) Go to: Scripting -> New, 
- 4) Paste the python code there and then 5) Scripting -> Run

Hack: Before you execute the code, resize (manually) the MRIcroGL window such as that the brain view has the desired dimension. This will ensure that the output saved brain rotated  images, will keep the window's dimensions and field of view.

### UPDATE on Sep, 10th: 
I have added a new function in the directory "Overlay_on_spm152" that overlays an activation map onto the spm152 structural template with negative and positive colors! 
