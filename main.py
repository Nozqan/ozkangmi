from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle, RoundedRectangle, Ellipse
import os
import shutil

# 🔥 TELEFON HAFIZASI (DÜZELTİLDİ)
BASE_PATH = "/storage/emulated/0/Ozkan_Kasa"

for f in ["Fotos", "Videos", "Music"]:
    os.makedirs(os.path.join(BASE_PATH, f), exist_ok=True)

# --- RENKLER ---
VIBRANT_PURPLE = (0.5, 0, 1, 1)
NEON_CYAN = (0, 1, 1, 1)
HOT_PINK = (1, 0, 0.5, 1)
DARK_BG = (0.02, 0.01, 0.08, 1)

class DynamicBackground(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*DARK_BG)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            Color(0.4, 0, 0.8, 0.2)
            self.glow = Ellipse(size=(800, 800))
        self.bind(size=self.update_bg)

    def update_bg(self, *args):
        self.rect.size = self.size
        self.glow.pos = (self.width*0.3, self.height*0.5)

class GlassCard(Button):
    def __init__(self, text_val, sub_text="", main_color=(1, 1, 1, 0.1), **kwargs):
        super().__init__(**kwargs)
        self.value = text_val  # 🔥 yeni (hata fix)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.markup = True
        self.text = f"[size=22sp][b]{text_val}[/b][/size]\n[size=12sp]{sub_text}[/size]"
        self.halign = 'center'

        with self.canvas.before:
            Color(*main_color)
            self.rrect = RoundedRectangle(pos=self.pos, size=self.size, radius=[30,])

    def on_size(self, *args):
        self.rrect.pos = self.pos
        self.rrect.size = self.size

# --- ŞİFRE EKRANI ---
class PasswordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = DynamicBackground()
        self.pin = ""

        self.layout.add_widget(Label(
            text="[b][color=FF00FF]Özkan[/color][color=00FFFF]GMİ[/color][/b]",
            markup=True, font_size='55sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.88}))

        self.display = Label(
            text="SİSTEM KİLİTLİ",
            markup=True,
            font_size='22sp',
            color=NEON_CYAN,
            pos_hint={'center_x': 0.5, 'center_y': 0.75})
        self.layout.add_widget(self.display)

        grid = GridLayout(cols=3, spacing=15,
                          size_hint=(0.8, 0.45),
                          pos_hint={'center_x': 0.5, 'center_y': 0.38})

        for i in ['1','2','3','4','5','6','7','8','9','C','0','OK']:
            btn = GlassCard(i, main_color=(1, 1, 1, 0.05))
            btn.bind(on_press=self.press)
            grid.add_widget(btn)

        self.layout.add_widget(grid)
        self.add_widget(self.layout)

    def press(self, instance):
        val = instance.value  # 🔥 FIX

        if val == 'C':
            self.pin = ""
        elif val == 'OK':
            if self.pin == "8044":  # 🔐 ŞİFRE DEĞİŞTİ
                self.manager.current = 'main'
            else:
                self.pin = ""
                self.display.text = "[color=FF3355]HATALI ŞİFRE[/color]"
        else:
            if len(self.pin) < 6:
                self.pin += val

        if self.pin:
            self.display.text = f"[b][color=00FFFF]{'*' * len(self.pin)}[/color][/b]"
        else:
            self.display.text = "SİSTEM KİLİTLİ"

# --- ANA MENÜ ---
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        l = DynamicBackground()

        l.add_widget(Label(
            text="KASA KONTROL",
            font_size='28sp',
            bold=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.92}))

        menu = GridLayout(cols=1, spacing=20,
                          size_hint=(0.85, 0.5),
                          pos_hint={'center_x': 0.5, 'center_y': 0.48})

        items = [
            ("FOTOĞRAFLAR", HOT_PINK, 'photo'),
            ("VİDEOLAR", VIBRANT_PURPLE, 'video'),
            ("MÜZİKLER", NEON_CYAN, 'music')
        ]

        for t, c, target in items:
            btn = GlassCard(t, main_color=(c[0], c[1], c[2], 0.2))
            btn.bind(on_press=lambda x, n=target: setattr(self.manager, 'current', n))
            menu.add_widget(btn)

        l.add_widget(menu)
        self.add_widget(l)

# --- DOSYA EKRANI ---
class FolderScreen(Screen):
    def __init__(self, folder_type, **kwargs):
        super().__init__(**kwargs)
        self.folder_type = folder_type
        self.layout = DynamicBackground()

        self.layout.add_widget(Label(
            text=f"{folder_type.upper()} DEPOSU",
            pos_hint={'center_y': 0.95}))

        back = Button(text="< GERİ",
                      size_hint=(0.2, 0.05),
                      pos_hint={'x':0.05, 'top':0.98})
        back.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))

        self.scroll = ScrollView(size_hint=(0.95, 0.7),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.grid = GridLayout(cols=3, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)

        add_btn = Button(text="+ YENİ DOSYA EKLE",
                         size_hint=(0.8, 0.08),
                         pos_hint={'center_x':0.5, 'center_y':0.1},
                         background_color=HOT_PINK)
        add_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'upload'))

        self.layout.add_widget(back)
        self.layout.add_widget(self.scroll)
        self.layout.add_widget(add_btn)

        self.add_widget(self.layout)

    def on_enter(self):
        self.grid.clear_widgets()
        path = os.path.join(BASE_PATH, self.folder_type)

        for f in os.listdir(path):
            btn = GlassCard(f[:8]+"...", main_color=(1,1,1,0.05),
                            size_hint_y=None, height=200)
            self.grid.add_widget(btn)

# --- YÜKLEME ---
class UploadScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        l = DynamicBackground()

        self.chooser = FileChooserIconView(path="/sdcard",
                                           size_hint=(1, 0.75),
                                           pos_hint={'top': 1})

        self.bar = ProgressBar(max=100,
                               size_hint=(0.8, 0.05),
                               pos_hint={'center_x':0.5, 'center_y':0.18},
                               opacity=0)

        btn = GlassCard("DOSYAYI HAPSET",
                        main_color=(0,1,0.5,0.2),
                        size_hint=(0.8, 0.1),
                        pos_hint={'center_x':0.5, 'center_y':0.07})

        btn.bind(on_press=self.process)

        l.add_widget(self.chooser)
        l.add_widget(self.bar)
        l.add_widget(btn)

        self.add_widget(l)

    def process(self, inst):
        if self.chooser.selection:
            src = self.chooser.selection[0]
            ext = os.path.splitext(src)[1].lower()

            if ext in ['.jpg', '.jpeg', '.png']:
                folder = "Fotos"
            elif ext in ['.mp4', '.mkv', '.avi']:
                folder = "Videos"
            elif ext in ['.mp3', '.wav']:
                folder = "Music"
            else:
                folder = "Fotos"

            dest = os.path.join(BASE_PATH, folder, os.path.basename(src))

            self.bar.opacity = 1
            anim = Animation(value=100, duration=1.2)
            anim.bind(on_complete=lambda *x: self.save(src, dest))
            anim.start(self.bar)

    def save(self, src, dest):
        shutil.copy2(src, dest)
        self.bar.value = 0
        self.bar.opacity = 0
        self.manager.current = 'main'

# --- APP ---
class OzkanGMIApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(PasswordScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FolderScreen(folder_type="Fotos", name='photo'))
        sm.add_widget(FolderScreen(folder_type="Videos", name='video'))
        sm.add_widget(FolderScreen(folder_type="Music", name='music'))
        sm.add_widget(UploadScreen(name='upload'))
        return sm

if __name__ == '__main__':
    OzkanGMIApp().run()
