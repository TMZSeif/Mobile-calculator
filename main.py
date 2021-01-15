import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import *
from kivy.lang import *
from kivy.uix.screenmanager import *
global sign
class MyWidgets(GridLayout):
    global sign 
    def __init__(self,**kwargs):
        global sign
        super(MyWidgets,self).__init__(**kwargs)
        self.cols = 1
        self.textinp = TextInput(multiline=False)
        self.add_widget(self.textinp)
        self.inside = GridLayout()
        self.inside.cols = 3
        self.btn1 = (Button(text='1',font_size=25))
        self.btn2 = (Button(text='2',font_size=25))
        self.btn3 = (Button(text='3',font_size=25))
        self.btn4 = (Button(text='4',font_size=25))
        self.btn5 = (Button(text='5',font_size=25))
        self.btn6 = (Button(text='6',font_size=25))
        self.btn7 = (Button(text='7',font_size=25))
        self.btn8 = (Button(text='8',font_size=25))
        self.btn9 = (Button(text='9',font_size=25))
        self.btn0 = (Button(text='0',font_size=25))
        self.btndot = (Button(text='.',font_size=25))
        self.btnclear = (Button(text='C',font_size=25,color=(255/255, 112/255, 0, 1)))
        self.btnadd = (Button(text='+',font_size=25,color=(0,1,0,0.69)))
        self.btnsubtract = (Button(text='-',font_size=25,color=(0,1,0,0.69)))
        self.btnmultiply = (Button(text='x',font_size=25,color=(0,1,0,0.69)))
        self.btndivide = (Button(text='/',font_size=25,color=(0,1,0,0.69)))
        self.btnpercent = (Button(text='%',font_size=25,color=(0,1,0,0.69)))
        self.btnequal = (Button(text='=',font_size=25,background_color=(0,1,0,1)))
        self.btn1.bind(on_release=self.Click1)
        self.btn2.bind(on_release=self.Click2)
        self.btn3.bind(on_release=self.Click3)
        self.btn4.bind(on_release=self.Click4)
        self.btn5.bind(on_release=self.Click5)
        self.btn6.bind(on_release=self.Click6)
        self.btn7.bind(on_release=self.Click7)
        self.btn8.bind(on_release=self.Click8)
        self.btn9.bind(on_release=self.Click9)
        self.btn0.bind(on_release=self.Click0)
        self.btndot.bind(on_release=self.Dot)
        self.btnclear.bind(on_release=self.Clear)
        self.btnadd.bind(on_release=self.Add)
        self.btnsubtract.bind(on_release=self.Subtract)
        self.btnmultiply.bind(on_release=self.Multiply)
        self.btndivide.bind(on_release=self.Divide)
        self.btnpercent.bind(on_release=self.Percent)
        self.btnequal.bind(on_release=self.Equal)
        self.inside.add_widget(self.btn1)
        self.inside.add_widget(self.btn2)
        self.inside.add_widget(self.btn3)
        self.inside.add_widget(self.btn4)
        self.inside.add_widget(self.btn5)
        self.inside.add_widget(self.btn6)
        self.inside.add_widget(self.btn7)
        self.inside.add_widget(self.btn8)
        self.inside.add_widget(self.btn9)
        self.inside.add_widget(self.btn0)
        self.inside.add_widget(self.btndot)
        self.inside.add_widget(self.btnclear)
        self.inside.add_widget(self.btnadd)
        self.inside.add_widget(self.btnsubtract)
        self.inside.add_widget(self.btnmultiply)
        self.inside.add_widget(self.btndivide)
        self.inside.add_widget(self.btnpercent)
        self.inside.add_widget(self.btnequal)
        self.add_widget(self.inside)
        sign = ''
    def Click1(self,instance):
        self.textinp.text += '1' 
    def Click2(self,instance):
        self.textinp.text += '2' 
    def Click3(self,instance):
        self.textinp.text += '3' 
    def Click4(self,instance):
        self.textinp.text += '4' 
    def Click5(self,instance):
        self.textinp.text += '5' 
    def Click6(self,instance):
        self.textinp.text += '6' 
    def Click7(self,instance):
        self.textinp.text += '7' 
    def Click8(self,instance):
        self.textinp.text += '8' 
    def Click9(self,instance):
        self.textinp.text += '9' 
    def Click0(self,instance):
        self.textinp.text += '0' 
    def Clear(self,instance):
        global sign
        self.textinp.text = ''
        sign = None
    def Add(self,instance):
        global sign
        global num
        sign = '+'
        num = self.textinp.text
        self.textinp.text = ''
    def Subtract(self,instance):
        global sign
        global num
        sign = '-'
        num = self.textinp.text
        self.textinp.text = ''
    def Multiply(self,instance):
        global sign
        global num
        sign = 'x'
        num = self.textinp.text
        self.textinp.text = ''
    def Divide(self,instance):
        global sign
        global num
        sign = '/'
        num = self.textinp.text
        self.textinp.text = ''
    def Percent(self,instance):
        global sign
        global num
        sign = '%'
        num = self.textinp.text
        self.textinp.text = ''
    def Equal(self,instance):
        global sign
        global num
        if sign == '+':
            try:
                num = float(self.textinp.text) + float(num)
                self.textinp.text = str(num)
            except:
                self.textinp.text = 'Error please try again'
        elif sign == '-':
            try:
                num = float(self.textinp.text) + float(num)
                self.textinp.text = str(num)
            except:
                self.textinp.text = 'Error please try again'
        elif sign == 'x':
            try:
                num = float(self.textinp.text) + float(num)
                self.textinp.text = str(num)
            except:
                self.textinp.text = 'Error please try again'
        elif sign == '/':
            try:
                num = float(self.textinp.text) + float(num)
                self.textinp.text = str(num)
            except:
                self.textinp.text = 'Error please try again'
        elif sign == '%':
            if self.textinp.text == '':
                num = float(num)/100
                self.textinp.text = str(num)
            else:
                num = float(num)/100*float(self.textinp.text)
                self.textinp.text = str(num)
        else:
            self.textinp.text = self.textinp.text
    def Dot(self,instance):
        self.textinp.text += '.'
class Calculator(App):
    def build(self):
        return MyWidgets()
if __name__ == '__main__':
    Calculator().run()
