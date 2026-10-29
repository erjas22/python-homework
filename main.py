import os
from pathlib import Path

from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.metrics import dp
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup


BG = (0.045, 0.04, 0.065, 1)
PANEL = (0.12, 0.10, 0.16, 1)
PURPLE = (0.52, 0.34, 0.95, 1)
WHITE = (0.96, 0.94, 1, 1)
MUTED = (0.68, 0.65, 0.76, 1)

EXTENSIONS = {".mp3", ".wav", ".ogg", ".flac"}


class NoirMusicApp(App):
    def build(self):
        self.title = "Noir Music"
        self.songs = []
        self.index = -1
        self.sound = None
        self.paused = False
        self.paused_at = 0
        self.seeking = False

        self.root_box = BoxLayout(
            orientation="vertical",
            padding=dp(18),
            spacing=dp(12),
        )
        self.root_box.bind(
            size=self._set_background,
            pos=self._set_background,
        )

        with self.root_box.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(*BG)
            self.bg_rect = Rectangle(
                pos=self.root_box.pos,
                size=self.root_box.size,
            )

        header = BoxLayout(
            size_hint_y=None,
            height=dp(48),
            spacing=dp(8),
        )
        header.add_widget(Label(
            text="[b]NOIR [color=B69AFF]MUSIC[/color][/b]",
            markup=True,
            font_size="22sp",
            halign="left",
        ))
        header.add_widget(self.make_button(
            "+ Add", self.pick_files, width=dp(85)
        ))
        self.root_box.add_widget(header)

        self.search = TextInput(
            hint_text="Search your music...",
            multiline=False,
            size_hint_y=None,
            height=dp(44),
            background_normal="",
            background_active="",
            background_color=PANEL,
            foreground_color=WHITE,
            hint_text_color=MUTED,
            cursor_color=PURPLE,
            padding=[dp(12), dp(11)],
        )
        self.search.bind(text=self.refresh_playlist)
        self.root_box.add_widget(self.search)

        art = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(145),
            padding=dp(12),
        )
        with art.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(*PANEL)
            RoundedRectangle(
                pos=art.pos,
                size=art.size,
                radius=[dp(18)],
            )
        art.bind(pos=self._update_art, size=self._update_art)

        art.add_widget(Label(
            text="[b]♫[/b]",
            markup=True,
            font_size="64sp",
            color=PURPLE,
        ))
        art.add_widget(Label(
            text="YOUR SOUND. YOUR SPACE.",
            font_size="11sp",
            color=MUTED,
        ))
        self.root_box.add_widget(art)
        self.art = art

        self.song_label = Label(
            text="Choose a song",
            font_size="21sp",
            bold=True,
            color=WHITE,
            size_hint_y=None,
            height=dp(32),
            shorten=True,
        )
        self.root_box.add_widget(self.song_label)

        self.status_label = Label(
            text="Add music to get started",
            color=MUTED,
            font_size="12sp",
            size_hint_y=None,
            height=dp(22),
        )
        self.root_box.add_widget(self.status_label)

        self.time_label = Label(
            text="00:00 / 00:00",
            color=MUTED,
            font_size="11sp",
            size_hint_y=None,
            height=dp(18),
        )
        self.root_box.add_widget(self.time_label)

        self.progress = Slider(
            min=0,
            max=100,
            value=0,
            size_hint_y=None,
            height=dp(28),
        )
        self.progress.bind(on_touch_down=self.progress_touch_down)
        self.progress.bind(on_touch_up=self.progress_touch_up)
        self.root_box.add_widget(self.progress)

        controls = BoxLayout(
            size_hint_y=None,
            height=dp(48),
            spacing=dp(10),
        )
        controls.add_widget(self.make_button(
            "|◀", self.previous_song
        ))
        self.play_button = self.make_button(
            "▶ PLAY", self.toggle_play
        )
        controls.add_widget(self.play_button)
        controls.add_widget(self.make_button(
            "▶|", self.next_song
        ))
        self.root_box.add_widget(controls)

        volume_row = BoxLayout(
            size_hint_y=None,
            height=dp(28),
            spacing=dp(10),
        )
        volume_row.add_widget(Label(
            text="VOLUME",
            color=MUTED,
            size_hint_x=None,
            width=dp(65),
            font_size="11sp",
        ))
        self.volume = Slider(min=0, max=1, value=0.8)
        self.volume.bind(value=self.change_volume)
        volume_row.add_widget(self.volume)
        self.root_box.add_widget(volume_row)

        self.root_box.add_widget(Label(
            text="[b]YOUR PLAYLIST[/b]",
            markup=True,
            color=WHITE,
            size_hint_y=None,
            height=dp(28),
            halign="left",
        ))

        self.scroll = ScrollView(do_scroll_x=False)
        self.playlist = BoxLayout(
            orientation="vertical",
            spacing=dp(6),
            size_hint_y=None,
        )
        self.playlist.bind(
            minimum_height=self.playlist.setter("height")
        )
        self.scroll.add_widget(self.playlist)
        self.root_box.add_widget(self.scroll)

        self.music_dir = Path(self.user_data_dir) / "Music"
        self.music_dir.mkdir(parents=True, exist_ok=True)

        Clock.schedule_once(self.load_saved_music, 0.2)
        Clock.schedule_interval(self.update_player, 0.5)
        return self.root_box

    def _set_background(self, *_):
        self.bg_rect.pos = self.root_box.pos
        self.bg_rect.size = self.root_box.size

    def _update_art(self, widget, *_):
        widget.canvas.before.clear()
        from kivy.graphics import Color, RoundedRectangle
        with widget.canvas.before:
            Color(*PANEL)
            RoundedRectangle(
                pos=widget.pos,
                size=widget.size,
                radius=[dp(18)],
            )

    def make_button(self, text, callback, width=None):
        button = Button(
            text=text,
            size_hint_x=None if width else 1,
            width=width or 0,
            size_hint_y=None,
            height=dp(46),
            background_normal="",
            background_down="",
            background_color=PURPLE,
            color=WHITE,
            font_size="14sp",
            bold=True,
        )
        button.bind(on_release=lambda *_: callback())
        return button

    def load_saved_music(self, *_):
        try:
            for path in self.music_dir.iterdir():
                if path.is_file() and path.suffix.lower() in EXTENSIONS:
                    self.add_song(str(path), autoplay=False)
        except OSError:
            pass

        if not self.songs:
            self.status_label.text = "Tap + Add to choose music"

    def pick_files(self):
        if platform == "android":
            try:
                from plyer import filechooser
                filechooser.open_file(
                    on_selection=self.on_files_selected,
                    multiple=True,
                )
            except Exception as exc:
                self.show_message(
                    "File picker error",
                    "Could not open the Android file picker.\n"
                    + str(exc),
                )
            return

        try:
            from tkinter import Tk, filedialog
            window = Tk()
            window.withdraw()
            window.attributes("-topmost", True)
            files = filedialog.askopenfilenames(
                title="Choose music",
                filetypes=[
                    ("Audio files", "*.mp3 *.wav *.ogg *.flac"),
                    ("All files", "*.*"),
                ],
            )
            window.destroy()
            self.on_files_selected(files)
        except Exception as exc:
            self.show_message("File picker error", str(exc))

    def on_files_selected(self, files):
        for path in files or []:
            if path:
                self.add_song(path)

    def add_song(self, path, autoplay=True):
        path = str(path)
        if not os.path.isfile(path):
            return
        if Path(path).suffix.lower() not in EXTENSIONS:
            return
        if path in self.songs:
            return

        self.songs.append(path)
        self.refresh_playlist()

        # Keep a copy in the app's own music directory when possible.
        try:
            import shutil
            destination = self.music_dir / Path(path).name
            if (
                Path(path).resolve() != destination.resolve()
                and not destination.exists()
            ):
                shutil.copy2(path, destination)
        except (OSError, PermissionError):
            pass

        if autoplay:
            self.play_song(len(self.songs) - 1)
        else:
            self.status_label.text = (
                f"{len(self.songs)} song(s) in playlist"
            )

    def refresh_playlist(self, *_):
        if not hasattr(self, "playlist"):
            return

        self.playlist.clear_widgets()
        query = self.search.text.strip().lower()

        found = 0
        for i, path in enumerate(self.songs):
            name = Path(path).stem
            if query not in name.lower():
                continue

            row = BoxLayout(
                size_hint_y=None,
                height=dp(46),
                spacing=dp(8),
            )
            label = Label(
                text=name,
                color=WHITE,
                halign="left",
                shorten=True,
            )
            button = self.make_button(
                "▶", lambda idx=i: self.play_song(idx),
                width=dp(48),
            )
            row.add_widget(label)
            row.add_widget(button)
            self.playlist.add_widget(row)
            found += 1

        if not found:
            self.playlist.add_widget(Label(
                text="No songs found",
                color=MUTED,
                size_hint_y=None,
                height=dp(45),
            ))

    def play_song(self, index):
        if not self.songs:
            self.status_label.text = "Add a song first"
            return

        index %= len(self.songs)
        path = self.songs[index]

        if self.sound:
            self.sound.stop()
            self.sound.unload()
            self.sound = None

        self.index = index
        self.paused = False
        self.paused_at = 0
        self.progress.value = 0
        self.time_label.text = "00:00 / 00:00"
        self.song_label.text = Path(path).stem

        self.sound = SoundLoader.load(path)
        if self.sound is None:
            self.status_label.text = (
                "Audio could not load. Try an MP3 or WAV file."
            )
            self.play_button.text = "▶ PLAY"
            return

        self.sound.volume = self.volume.value
        self.sound.play()
        self.play_button.text = "Ⅱ PAUSE"
        self.status_label.text = "Now playing"

    def toggle_play(self):
        if self.sound is None:
            if self.songs:
                self.play_song(max(self.index, 0))
            else:
                self.pick_files()
            return

        if not self.paused:
            try:
                self.paused_at = self.sound.get_pos() or 0
            except Exception:
                self.paused_at = 0

            self.sound.stop()
            self.paused = True
            self.play_button.text = "▶ PLAY"
            self.status_label.text = "Paused"
        else:
            self.sound.play()
            if self.paused_at > 0:
                try:
                    self.sound.seek(self.paused_at)
                except (NotImplementedError, AttributeError):
                    pass

            self.paused = False
            self.play_button.text = "Ⅱ PAUSE"
            self.status_label.text = "Now playing"

    def next_song(self):
        if self.songs:
            self.play_song((self.index + 1) % len(self.songs))

    def previous_song(self):
        if self.songs:
            self.play_song((self.index - 1) % len(self.songs))

    def change_volume(self, _slider, value):
        if self.sound:
            self.sound.volume = value

    def progress_touch_down(self, slider, touch):
        if slider.collide_point(*touch.pos):
            self.seeking = True

    def progress_touch_up(self, slider, touch):
        if self.seeking and slider.collide_point(*touch.pos):
            self.seeking = False
            if self.sound and self.sound.length:
                try:
                    position = self.sound.length * slider.value / 100
                    self.sound.seek(position)
                    self.paused_at = position
                except (NotImplementedError, AttributeError):
                    self.status_label.text = "Seeking not supported"

    def update_player(self, _dt):
        if not self.sound:
            return

        try:
            length = self.sound.length or 0
            position = self.paused_at if self.paused else (
                self.sound.get_pos() or 0
            )

            self.time_label.text = (
                f"{self.format_time(position)} / "
                f"{self.format_time(length)}"
            )

            if length > 0 and not self.seeking:
                self.progress.value = min(
                    100, max(0, position / length * 100)
                )

            if (
                not self.paused
                and length > 0
                and position >= length - 0.5
            ):
                self.next_song()

        except Exception:
            pass

    @staticmethod
    def format_time(seconds):
        seconds = max(0, int(seconds))
        return f"{seconds // 60:02d}:{seconds % 60:02d}"

    def show_message(self, title, message):
        popup = Popup(
            title=title,
            content=Label(
                text=message,
                color=WHITE,
                halign="center",
            ),
            size_hint=(0.85, 0.4),
        )
        popup.open()

    def on_stop(self):
        if self.sound:
            self.sound.stop()
            self.sound.unload()


if __name__ == "__main__":
    NoirMusicApp().run()