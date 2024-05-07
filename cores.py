from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import window

class MinhaApp(App):
    def build(self):

        window.clearcolor = (1, 1, 1, 1)


        label = label(text='Esta é uma tela com fundo branco', color=(0, 0, 0, 1))


        return Label
    

if __name__ == "__main__":
    MinhaApp().run()