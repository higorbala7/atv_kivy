from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right', loop=True)


        imagens = ["senaipe.jpeg", "sesi.lpg", "iel.jpg"]
        for imagem in imagens:
            imagem_widget = AsyncImage(source=imagem)
            carousel.add_widget(imagem_widget)

            return carousel
        

if __name__ == "__main__":
    CarouselApp().run()