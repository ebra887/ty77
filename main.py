from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

class CalculatorApp(App):

    def build(self):
        self.title = "Flat Calculator"

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # 🧮 العنوان
        title = Label(text="آلة حاسبة", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(title)

        # 🔢 الإدخال الأول
        self.entry_a = TextInput(hint_text="الرقم الأول", multiline=False)
        layout.add_widget(self.entry_a)

        # 🔢 الإدخال الثاني
        self.entry_b = TextInput(hint_text="الرقم الثاني", multiline=False)
        layout.add_widget(self.entry_b)

        # ➗ العمليات
        self.operation = Spinner(
            text="+",
            values=["+", "-", "*", "/"],
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.operation)

        # 🔘 زر الحساب
        btn = Button(
            text="احسب",
            background_color=(0.1, 0.1, 0.1, 1),
            size_hint=(1, 0.3)
        )
        btn.bind(on_press=self.calc)
        layout.add_widget(btn)

        # 📦 النتيجة
        self.result = Label(text="النتيجة: ", font_size=18)
        layout.add_widget(self.result)

        return layout

    # 🧠 دالة الحساب
    def calc(self, instance):
        try:
            a = float(self.entry_a.text)
            b = float(self.entry_b.text)
            op = self.operation.text

            if op == "+":
                res = a + b
            elif op == "-":
                res = a - b
            elif op == "*":
                res = a * b
            elif op == "/":
                res = a / b

            self.result.text = f"النتيجة: {res}"

        except:
            self.result.text = "خطأ في الإدخال"


if __name__ == "__main__":
    CalculatorApp().run()
