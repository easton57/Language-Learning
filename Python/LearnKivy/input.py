import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set Columns
        self.cols = 2

        # Add Widgets
        self.add_widget(Label(text="Name: "))
        # Add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # Add Widgets
        self.add_widget(Label(text="Favorite Pizza: "))
        # Add input box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # Add Widgets
        self.add_widget(Label(text="Favorite Color: "))
        # Add input box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        # Create Submit button
        self.submit = Button(text="Submit", font_size=32)
        # Bind a button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}!")
        # Print to screen
        self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}!"))

        # Clear the input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
