import sys
sys.path.append('../')

from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDao import FacturaDao


#main ing
pcd  = PersonaDaoControl()
cd = FacturaDao()

try:    
        

  
    pcd._persona._apellidos = "Juan"
    pcd._persona._nombres = "Perez"
    pcd._persona._telefono = "090009990"
    pcd._persona._tipoIdentificacion = "CEDULA"

    pcd.save
    pcd._persona = None        
    #print(pcd._lista)
    pcd._persona._apellidos = "Luis"
    pcd._persona._nombres = "Perez"
    pcd._persona._telefono = "099191991"
    pcd._persona._tipoIdentificacion = "EDUCATIVO"

    pcd.save


except Exception as error:
    print("errores")
    print(error)



