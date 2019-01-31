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


//fantoma escalera
//Contenedor del fantoma
:P x_fantoma 10./2
:P z_fantoma 1/2

:P y_fantoma1 10./2
:VOLU fantoma1 BOX $x_fantoma $y_fantoma1 $z_fantoma NIST_PMMA
:PLACE fantoma1 1 mundo RM0 0. 0. $pmma_dist1
:COLOUR fantoma1 0. 0. 0.7

:P y_fantoma2 8/2
:VOLU fantoma2 BOX $x_fantoma $y_fantoma2 $z_fantoma NIST_PMMA
:PLACE fantoma2 1 mundo RM0 0. -1 $pmma_dist2
:COLOUR fantoma2 0. 0. 0.7

:P y_fantoma3 6/2
:VOLU fantoma3 BOX $x_fantoma $y_fantoma3 $z_fantoma NIST_PMMA
:PLACE fantoma3 1 mundo RM0 0. -2 $pmma_dist3
:COLOUR fantoma3 0. 0. 0.7

:P y_fantoma4 4/2
:VOLU fantoma4 BOX $x_fantoma $y_fantoma4 $z_fantoma NIST_PMMA
:PLACE fantoma4 1 mundo RM0 0. -3 $pmma_dist4
:COLOUR fantoma4 0. 0. 0.7

:P y_fantoma5 2/2
:VOLU fantoma5 BOX $x_fantoma $y_fantoma5 $z_fantoma NIST_PMMA
:PLACE fantoma5 1 mundo RM0 0. -4 $pmma_dist5
:COLOUR fantoma5 0. 0. 0.7

//detector medipix detras del pmma
:P x_detector 14./2
:P y_detector 14./2
:P z_detector (2/2)
:VOLU detector BOX $x_detector $y_detector $z_detector "NIST_Cadmium Telluride"
:PLACE detector 1 mundo RM0 0. 0. $detect_dist
:COLOUR detector 0.6 0.1 0.1
