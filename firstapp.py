import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle

sila = 250/255.0,12/255.0,82/255.0,1

kivy.require('2.0.0')
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

Builder.load_string(""" 
<MyLayout>
    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height

        padding: 20
        spacing: 20

        Label:
            text: "Enter Text: "
            font_size: 50
            size_hint: (None, None)
            width: 40
            height: 20
            pos_hint: {'center_x': 0.362}
            color: (239/255,76/255,207/255,1)

        TextInput:
            id: text_in
            multiline: True
            size_hint: (None, None)
            font_size: 17
            width: 336
            height: 80

        Label:
            text: 'Replacee:'
            size_hint: (None, None)
            font_size: 30
            width: 40
            height: 20
            pos_hint: {'center_x': 0.191}
            color: (239/255,76/255,207/255,1)

        TextInput:
            id: text_replace
            multiline: False
            size_hint: (None, None)
            font_size: 17
            width: 240
            height: 30
#increasing the number makes it go right
#decreasing the number makes it go left
        Label:
            text: 'Replacer:'
            size_hint: (None, None)
            font_size: 30
            width: 40
            height: 20
            pos_hint: {'center_x': 0.185}
            color: (250/255,76/12,207/82,1)

        TextInput:
            id: text_replacer
            multiline: False
            size_hint: (None, None)
            font_size: 17
            width: 240
            height: 30

        Label:
            text: 'Exit Text: '
            font_size: 50
            size_hint: (None, None)
            width: 40
            height: 20
            pos_hint: {'center_x': 0.311}
            color: (250/255,12/255,82/255,1)

        TextInput:
            id: text_out
            multiline: True
            font_size: 17

        Button:
            text: 'Enter'
            font_size: 40
            on_press: root.wp()
            background_normal: ''
            background_color: (33/255.0,5/255.0,255/255.0,1)

        Button:
            text: 'Delete'
            font_size: 40
            on_press: root.d()
            background_normal: ''
            background_color: (250/255.0,12/255.0,82/255.0,1)
""")

class MyLayout(Widget):

    def d(self):
        self.ids.text_out.text = ''
        self.ids.text_in.text = ''
        self.ids.text_replace.text = ''
        self.ids.text_replacer.text = ''

    def wp(self):
        txtin = self.ids.text_in.text
        wtr = self.ids.text_replace.text
        wtrw = self.ids.text_replacer.text
        VG = txtin.replace(wtr, wtrw)

        self.ids.text_out.text = VG


class RandomApp(App):
    def build(self):
        return MyLayout()

    Window.size = (375, 600)
    Window.clearcolor = (29/255.0, 220/255.0, 255/255.0, 1)

if __name__ == '__main__':
    RandomApp().run()

