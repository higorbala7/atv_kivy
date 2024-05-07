from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label


class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)

        Slider.bind(value=self.atualizar_label)
        Slider.label = Label(text="Valor do Slider: {}".format(int(Slider.value)))


        layout.add_widget(Slider)
        layout.add_widget(self.label)

        return layout
    def atualizar_label(self, instance, valor):
        self.label.text = "Valor do Slider: {}".format(int(valor))

if __name__ == "__main__":
    MinhaApp().run()