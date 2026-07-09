from kivy.app import App
from kivy.uix.label import Label

class DataWiseApp(App):
    def build(self):
        return Label(text="Hello, DataWise is working!")

if __name__ == "__main__":
    DataWiseApp().run()
