# Olhar em volta - Por Sam Mahonri

# Este script deve estar sendo executado com um sensor de Mouse-Movement ativo em todos os frames de preferencia na Camera
# A Camera deve ser filha de um Empty
from bge import logic as G, render as R

def main(cont):
    
    # Inicializa
    
    own = cont.owner
    pai = own.parent
    mouse = own.sensors["mov"]
    
    # Limites de rotação do eixo Z Global da Camera
    limitE = -0.90 
    limitD = 0.90
    
    sWidth = R.getWindowWidth()//2
    mWidth = R.getWindowWidth()//4
    x = (mouse.position[0] - sWidth)
    buffer = 0
    ori = own.worldOrientation.to_euler()
    
    # Imprime Localização do cursor e o valor de 1/4 da tela
    
    print("X:",+x)
    print("m:",+mWidth)
    
    # Sensibilidade de acordo com posição do cursor
    
    if x > 0:
        buffer = -0.03 # Sensibilidade
    elif x < 0:
        buffer = 0.03
    else:
        buffer = 0
        
    # Aplica rotação do pai se estiver dentro dos limites
    
    if ((x < 0 and x < mWidth*-1) or (x > 0 and x > mWidth)) and not x == 0:   
        if ori.z > limitE and ori.z < limitD:
            pai.applyRotation([0,0,buffer], 1)
            if x < 0:
                R.setMousePosition(mWidth, mouse.position[1])
            elif x > 0:
                R.setMousePosition(mWidth*3, mouse.position[1])
            x = 0
            
    # Remover bugs automaticamente
        
    if ori.z < limitE and buffer > 0:
        pai.applyRotation([0,0,buffer], 1)
    elif ori.z > limitD and buffer < 0:
        pai.applyRotation([0,0,buffer], 1)
        
    
    
