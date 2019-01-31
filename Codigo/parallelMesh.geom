//Detector volumen de Si voxelizado detras del pmma
:P x_container 14./2
:P y_container 14./2
:P z_container (0.21875)/2
:P pixel 0.0546875
:P pixel_medios (0.0546875)/2

:VOLU container BOX $x_container $y_container $z_container G4_AIR
:PLACE container 1 mundo RM0 0. 0. $detect_dist
:VOLU rejilla BOX $pixel_medios $pixel_medios $pixel_medios G4_Si
:PLACE_PARAM rejilla 1 container PHANTOM 256 256 4 $pixel $pixel $pixel
