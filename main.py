import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
import requests
from bs4 import BeautifulSoup
from kivy.lang.builder import Builder

kv = Builder.load_string("""
<MyWidget>:
    cityI:cityI
    cityO:cityO
    tempO:tempO
    skyO:skyO
    GridLayout:
        cols:1
        size:root.width,root.height
        GridLayout:
            size_hint_y:None
            height:60
            cols:2
            TextInput:
                font_size:40
                id:cityI
                multiline:False
            Button:
                size_hint:0.3,1
                text:"Search"
                on_press:root.search()
        Label:
            id:cityO
            text:"City Name"
            size_hint:1,0.5 
            font_size:40
        Label:
            id:tempO
            text:"temperature"
            font_size:80
        Label:
            id:skyO
            text:"Sky status"
            font_size:50
""")

class MyWidget(Widget):
    cityI = ObjectProperty(None)
    
    def search(self):
        city = self.cityI.text

        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+city
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str.split('\n')
        time = data[0]
        sky = data[1]

        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text

        # getting other required data
        pos = strd.find('Wind')
        other_data = strd[pos:]
        self.ids.cityO.text = city
        self.ids.tempO.text = temp
        self.ids.skyO.text = sky



class mainApp(App):
    def build(self):
        return MyWidget()
    
if __name__ =="__main__":
    mainApp().run()