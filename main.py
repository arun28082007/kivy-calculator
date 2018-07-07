from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calculator(BoxLayout):
    label = ''
    
    def delete(self, instance):
        self.display.text = instance[:0]
    
    def del1(self, instance):
        self.display.text = instance[:-1]
    
    def calc(self, instance):
        self.display.text = str(eval(instance))
        self.result.text = str(eval(instance))
        
class CalculatorApp(App):
    trigger = False
    triggerClear = False
    
    def build(self):
        return Calculator()
        
if __name__ == '__main__':
    CalculatorApp().run()