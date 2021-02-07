# Olhar em volta - Por Sam Mahonri

# Este script deve estar sendo executado com um sensor de Mouse-Movement ativo em todos os frames de preferencia na Camera
# A Camera deve ser filha de um Empty
from bge import logic as G, render as R

def main(cont):
    
    # Inicializa
    
    own = cont.owner
    pai = own.parent
    mouse = own.sensors["mov"]
    limits = {"e":-0.90,"d":0.90}
    screen = {"s2":R.getWindowWidth()//2,"s4":R.getWindowWidth()//4}
    x = (mouse.position[0] - screen["s2"])
    sens = 0
    ori = own.worldOrientation.to_euler()
        
    # Sensibilidade de acordo com posição do cursor
    
    if x > 0:
        sens = -0.03
    elif x < 0:
        sens = 0.03
    else:
        sens = 0
        
    # Aplica rotação do pai se estiver dentro dos limites
    
    if ((x < 0 and x < screen["s4"]*-1) or (x > 0 and x > screen["s4"])) and x != 0:   
        if ori.z > limits["e"] and ori.z < limits["d"]:
            pai.applyRotation([0,0,sens], 1)
            if x < 0:
                R.setMousePosition(screen["s4"], mouse.position[1])
            elif x > 0:
                R.setMousePosition(screen["s4"]*3, mouse.position[1])
            x = (mouse.position[0] - screen["s2"])
            
    # Remover bugs automaticamente
        
    if ori.z < limits["e"] and sens > 0:
        pai.applyRotation([0,0,sens], 1)
    elif ori.z > limits["d"] and sens < 0:
        pai.applyRotation([0,0,sens], 1)
    
    # Debug
        
    print("\ns4:",+screen["s4"]," - s4*-1:",+screen["s4"]*-1,"\nx:",+x,"\nsens:",+sens,"\nori:",+ori.z)
        
    
    
        
    
    
