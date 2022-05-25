from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:

            OneLineListItem:
                text: "О лицее"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Фотографии предприятия"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                    
            OneLineListItem:
                text: "Адрес"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Ликино-Дулевский лицей"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: f"Муниципальное автономное общеобразовательное учреждение «Ликино-Дулевский лицей» имеет свою богатую историю. Оно ведет свое начало от церковно-приходской школы.Это было единственное образовательное учреждение в г. Ликино-Дулево.17 сентября 1931 года впервые открыла свои двери Дулевская школа №1, расположившаяся в новом четырехэтажном здании, пока еще школа-семилетка. Через пять лет школа получает новый статус среднего учебного заведения. И на протяжении 70-ти лет «Дулевская средняя школа №1» обучала детей фарфористов, машиностроителей и текстильщиков, давала им прочные знания, которые позволяли многим выпускникам поступать в вузы нашей страны.Первый выпуск 1939 года насчитывал 19 человек, большинство из них в тяжелом военном 1941 году ушло на фронт, многие из них не вернулись. А в светлом и просторном здании школы был развернут эвакогоспиталь № 2933, который просуществовал до 1949 года. Ученики были переведены в Дулевскую школу №4.В январе 1949 года здание школы освобождается от госпиталя и ученики возвращаются в родные стены."
                    halign: "center"

            MDScreen:
                name: "scr 2"

                MDGridLayout:
                    cols: 3
                    row_default_height: ((self.width - 0) - self.cols*self.spacing[0]) / self.cols
                    row_force_default: True
                    adaptive_height: True
                    padding: dp(4), dp(4)
                    spacing: dp(4)

                    SmartTileWithStar:
                        source: "https://ozzebra.ru/wp-content/uploads/Snimok-115.jpg"
                    SmartTileWithStar:
                        source: "http://ozmo.ru/files/image/35/24/63/lg!6ha.jpg"
                    SmartTileWithStar:
                        source: "https://static.360tv.ru/get_resized/HVX28uOAwce7XREnDrFWj9vYaXYWObsObR0fyX2yktQ/resizing_type:fill/size:640:360/gravity:fp:0.5:0.5/enlarge:1/aHR0cHM6Ly9zdGF0aWMuMzYwdHYucnUvbWVkaWEvaW1hZ2VzL2FydGljbGVzL2Nyb3BzLzQxYjdmYmQ2LTMzYzItNDBhYS1iYjliLWVjMjY1MjFlNDM5ZS9jcm9wXzkyMV81MTguanBn.webp"
                    SmartTileWithStar:
                        source: "https://sun9-34.userapi.com/s/v1/if2/pH4y2zLfm1qQ9X2gjhszZPxHVD_fad0ofdjJe6i15Sm1VNLrtgax1lk1-A2Dl4ph4VAwy72B34P8IV448zX8kn-E.jpg?size=1024x766&quality=96&type=album"
                    SmartTileWithStar:
                        source: "https://sun9-48.userapi.com/s/v1/if2/5So6Fj3CibzYl0Sj-lYqajsnCzaS0leJwDT6w2PnzeFEb4GunWf08RRItrIqx8R_yzoa1SKE2v2aVEwZ01xrPYR7.jpg?size=1024x576&quality=96&type=album"
                    SmartTileWithStar:
                        source: "https://sun9-83.userapi.com/s/v1/if2/O0xgrpHOGPssMmUNoj43RB2FFimeYFaOnkRqwly8pmolMRhL_A4VPTXNsRaGiLzZR0e0NoNy7shF5p7nAfYBI02s.jpg?size=1024x574&quality=96&type=album"
                    
            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: f"Адрес: 142670, Московская область, город Ликино - Дулёво, улица Кирова, 73"

                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)

class Cifra(MDApp):
    def build(self):
        return Builder.load_string(KV)


Cifra().run()