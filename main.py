import kivy
kivy.require('1.11.0')

from kivy.config import Config
Config.set('kivy','default_font',['msgothic','font/SourceHanSansCN-Bold.otf'])
#Config.setdefault('kivy','default_font',None)
#Config.write()

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color,Rectangle
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.tabbedpanel import TabbedPanelException
from kivy.uix.tabbedpanel import TabbedPanelContent
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder


'''kivy.resources.resource_add_path("/font")
fong_heiti = kivy.resources.resource_find('SourceHanSansCN-Bold.otf')'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen

class Top(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        Window.fullscreen = 1
        Window.size = (1920,1080)
        return Top()

if __name__ == '__main__':
    MainApp().run()