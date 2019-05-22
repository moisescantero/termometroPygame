"""termometro con pygame"""
import pygame, sys
from pygame.locals import *

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415))#iniciamos pantalla dando tamaño
        pygame.display.set_caption("Termómetro")#nombre para la pantalla
        self.__screen.fill((244,236,203))#doy color al fondo de la pantalla
            
    def __on_close(self):
        pygame.quit()
        sys.exit()          
            
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:#si el tipo de evento es igual a quitar pygame
                    self.__on_close()
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                    
            #Pintamos el fondo de pantalla
            self.__screen.fill((244, 236, 203))
                
            #Pintamos el termómetro en su posición
            self.__screen.blit(self.termometro.custome, (50, 34))
            
            #Pintamos el cuadro de texto
            text = self.entrada.render() # Obtenememos rectánculo blanco y foto de texto y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) #creamos el rectángulo blanco con sus datos (posición y tamaño) text[0]
            self.__screen.blit(text[1], self.entrada.pos()) #Pintamos la foto del texto (text[1])
            '''
            #Pintamos el selector
            self.__screen.blit(self.selector.custome(), (112,153))
            '''
            pygame.display.flip()

            
            pygame.display.flip()
    

            
        
        


if __name__ == "__main__":
    pygame.init()
    app = mainApp
    app.start(None)
        

        