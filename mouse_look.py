# Mouse Look simples - Por Sam Mahonri
# Testado no Blender 2.79, UPBGE 0.2.5 e UPBGE 0.3.0.

#own = Cabeça do personagem, pode ser um "Empty"
#body = Pai da cabeça do personagem, Parente do "Empty"
#Na cabeça, adicione a propriedade "sens" (Sensibilidade) Ex: 0.002
#A Camera pode ser filha da cabeça

from bge import logic as G, render as R

def main(cont):
    
    own = cont.owner
    body = own.parent
    sens = (own["sens"])*-1
    mouse = own.sensors["mov"]
    
    sWidth = R.getWindowWidth()//2
    sHeight = R.getWindowHeight()//2
    
    x = (mouse.position[0] - sWidth)* sens
    y = (mouse.position[1] - sHeight)* sens
    
    ori = own.orientation
    
    if y < 0 and ori[2][1] < -0.88:
        y = 0
    if y > 0 and ori[2][1] > 0.88:
        y = 0
        
    body.applyRotation([0,0,x], 1)
    own.applyRotation([y,0,0], 1)
    
    R.setMousePosition(sWidth, sHeight)
