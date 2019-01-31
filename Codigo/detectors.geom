//En este archivo se va a realizar la simulacion de un tubo que genere rayosX
#include NIST_materials.txt
#include NIST_elements.txt

:P pmma_dist5 616.2
:P pmma_dist4 616.2+1
:P pmma_dist3 616.2+2
:P pmma_dist2 616.2+3
:P pmma_dist1 616.2+4


:P detect_dist 700.

//Mundo de 90 centimetros lleno de aire
:P x_mundo 1800./2
:P y_mundo 1800./2
:P z_mundo 1800./2
:VOLU mundo BOX $x_mundo $y_mundo $z_mundo G4_AIR
:VIS mundo OFF
:ROTM RM0 0. 0. 0.



//detector medipix detras del pmma
:P x_detector 14./2
:P y_detector 14./2
:P z_detector (2/2)
:VOLU detector BOX $x_detector $y_detector $z_detector G4_Si
:PLACE detector 1 mundo RM0 0. 0. $detect_dist
:COLOUR detector 0.6 0.1 0.1
