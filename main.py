from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Create a BoxLayout container
        layout = BoxLayout(orientation='vertical')

        # Add a Label to the layout
        label = Label(text='Hello, Kivy!', font_size='32sp')
        layout.add_widget(label)

        # Add a Button to the layout
        button = Button(text='Press me', size_hint=(1, 0.2))
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # Update the label's text when the button is pressed
        instance.text = 'Button Pressed!'

if __name__ == '__main__':
    MyApp().run()

