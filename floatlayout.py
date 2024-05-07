from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        layout_float =FloatLayout()

        botao1 = Button (text='Botão 1', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.1, 'y':0.8})
        botao2 = Button (text='Botão 1', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        botao3= Button (text='Botão 1', size_hint=(None, None), size=(100, 50), pos_hint={'righ': 0.9, 'y': 0.1})


        layout_float.add_widget(botao1)
        layout_float.add_widget(botao2)
        layout_float.add_widget(botao3)

        return layout_float
    

if __name__ == "__main__":
    MinhaApp().run()


