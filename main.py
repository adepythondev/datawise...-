from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class DataWiseApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        title = Label(text="DataWise", font_size=32, size_hint=(1, 0.2))
        layout.add_widget(title)

        self.usage_label = Label(
            text="Today's usage: 0 MB",
            font_size=20,
            size_hint=(1, 0.3)
        )
        layout.add_widget(self.usage_label)

        check_button = Button(
            text="Check Usage",
            size_hint=(1, 0.2),
            on_press=self.check_usage
        )
        layout.add_widget(check_button)

        return layout

    def check_usage(self, instance):
        self.usage_label.text = "Today's usage: 245 MB (sample data)"

if __name__ == "__main__":
    DataWiseApp().run()
