import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):#inicializo objeto termometro
        self.custome = pygame.image.load("images/termo1.png")#cargo imagen
        
    def convertir(self,grados,toUnidad):#método convertir del objeto termometro
        resultado = 0
        if toUnidad == "F":
            resultado = grados * 9/5 + 32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        return "{:10.2f}".format(resultado)
        
        
    
class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad="C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad
        
    def custome(self):#getter u obtenedor de selector
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    def unidad(self):#getter de unidad
        return self.__tipoUnidad
    
    
    def change(self):#método cambio de selector de grados
       if self.__tipoUnidad == "F":
            self.__tipoUnidad = "C"
       else:
            self.__tipoUnidad = "F"
    
    
    

class NumberInput():
    __value = 0
    __strValue = ""
    __position = [0,0]
    __size = [0,0]
    __pointsCount = 0
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial",24)
        self.value(value)
    
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0):
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode ==".":
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE:
                self.__strValue = self.__strValue[:-1]
                self.value(self.__strValue)
                
    
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74,74,74))#creo rectángulo blanco para introducir Tª
        rect = textBlock.get_rect()#guardo en variable solo el rectángulo de textBlock
        rect.left = self.__position[0]#guardo en variable posición izquierda del rectángulo
        rect.top = self.__position[1]#guardo en variable posición arriba del rectángulo
        rect.size = self.__size#guardo en variable tamaño del rectángulo
        """
        return {
                "fondo": rect
                "texto": textBlock
            }
        """
        return (rect, textBlock)
    
    def value(self, val=None):
        if val==None:
            return self.__value
        else:
            val = str(val)
            print(val, "Grados")
            try:
                self.__value = float(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass    
    
    
    
    
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass            

    
    def posX(self, val=None):#getter de width para size
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass#si el valor no es adecuado pasa de él

    def posY(self, val=None):#getter de width para size
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass#si el valor no es adecuado pasa de él
    
    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass#si el valor no es adecuado pasa de él
   




class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))#creo una pantalla de tamaño dado
        pygame.display.set_caption("Termómetro")#doy nombre a la pantalla
        
        self.termometro = Termometro()#guardo en variable llamada a función termómetro
        self.entrada = NumberInput("")#guardo en variable llamada a función entrada de Tª
        self.entrada.pos((106, 58))#doy posición para rectángulo de entrada de datos
        self.entrada.size((133, 28))#doy tamaño al rectángulo para entrada de datos
        
        self.selector = Selector()#llamo a objeto selector de grados

    def __on_close(self):
        pygame.quit()
        sys.exit()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                
                self.entrada.on_event(event)#me pasas los eventos a método on_event de class numberInput
                if event.type == pygame.MOUSEBUTTONDOWN:#si pulso botón ratón
                    self.selector.change()#llamo a change de selector
                    grados = self.entrada.value()#llamo a getter de grados
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados,nuevaUnidad)
                    self.entrada.value(temperatura)
                    
            #pinto el fondo de pantalla
            self.__screen.fill((244,236,203))#pinto fondo de la pantalla
                
            #pinto termómetro en su posición
            self.__screen.blit(self.termometro.custome,(50,34))
            #pinto el cuadro de texto
            text = self.entrada.render()#obtengo rectangulo y texto
            pygame.draw.rect(self.__screen, (255,255,255), text[0])#creo el rectangulo
            self.__screen.blit(text[1], self.entrada.pos()) #Pintamos la foto del texto (text[1])
            
            #pintamos el selector de grados
            self.__screen.blit(self.selector.custome(), (112,153))
            
            pygame.display.flip()

if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()        