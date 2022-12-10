from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button


class SettingsButton(Button, ButtonBehavior, HoverBehavior):
    settings_image = ObjectProperty(None)
    enter_image = Animation(rot_angle=0, duration=0.01) + Animation(rot_angle=-60, duration=0.2)
    leave_image = Animation(rot_angle=-60, duration=0.01) + Animation(rot_angle=0, duration=0.2)

    def __init__(self, **kwargs):
        super(SettingsButton, self).__init__(**kwargs)
        self.image_anim = None
        self.press_anim = None

    def on_press(self):
        self.press_anim = Animation(col=(0, 0, 179 / 255, 1), duration=0.15)
        self.image_anim = Animation(color=(1, 1, 1, 1 / 2), duration=0.15)
        self.press_anim.start(self)
        self.image_anim.start(self.settings_image)

    def on_release(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.image_anim = Animation(color=(1, 1, 1, 1), duration=0.15)
        self.press_anim.start(self)
        self.image_anim.start(self.settings_image)

    def on_enter(self):
        self.press_anim = Animation(col=(0, 0, 230 / 255, 1), duration=0.15)
        self.press_anim.start(self)
        self.enter_image.start(self.settings_image)

    def on_leave(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.press_anim.start(self)
        self.leave_image.start(self.settings_image)

class CloseButton(Button, ButtonBehavior, HoverBehavior):

    close_image = ObjectProperty(None)
    shrink_image = Animation(size_hint=[0.8, 0.8], duration=0.15)
    expand_image = Animation(size_hint=[1, 1], duration=0.15)
    hover_image = Animation(size_hint=[1.1, 1.1], duration=0.15) + Animation(size_hint=[1, 1], duration=0.15)

    def __init__(self, **kwargs):
        super(CloseButton, self).__init__(**kwargs)
        self.image_anim = None
        self.press_anim = None

    def on_press(self):
        self.press_anim = Animation(col=(0, 0, 179 / 255, 1), duration=0.15)
        self.press_anim.start(self)
        self.shrink_image.start(self.close_image)

    def on_release(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.press_anim.start(self)
        self.expand_image.start(self.close_image)

    def on_enter(self):
        self.press_anim = Animation(col=(0, 0, 230 / 255, 1), duration=0.15)
        self.press_anim.start(self)
        self.hover_image.start(self.close_image)

    def on_leave(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.press_anim.start(self)

class UpdateButton(Button, ButtonBehavior, HoverBehavior):
    update_image = ObjectProperty(None)
    enter_image = Animation(rot_angle=0, duration=0.01) + Animation(rot_angle=-60, duration=0.2)
    leave_image = Animation(rot_angle=-60, duration=0.01) + Animation(rot_angle=0, duration=0.2)
    rotating_anim = Animation(rot_angle=360, duration=0.001) + Animation(rot_angle=-360, duration=3)

    def __init__(self, **kwargs):
        super(UpdateButton, self).__init__(**kwargs)
        self.image_anim = None
        self.press_anim = None

    def start_rotation(self):
        self.rotating_anim.repeat = True
        self.rotating_anim.start(self.update_image)

    def stop_rotation(self):
        self.rotating_anim.stop(self.update_image)
        self.update_image.rot_angle = 0

    def on_press(self):
        self.press_anim = Animation(col=(0, 0, 179 / 255, 1), duration=0.15)
        self.image_anim = Animation(color=(1, 1, 1, 1 / 2), duration=0.15)
        self.press_anim.start(self)
        self.image_anim.start(self.update_image)

    def on_release(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.image_anim = Animation(color=(1, 1, 1, 1), duration=0.15)
        self.press_anim.start(self)
        self.image_anim.start(self.update_image)

    def on_enter(self):
        self.press_anim = Animation(col=(0, 0, 230 / 255, 1), duration=0.15)
        self.press_anim.start(self)
        self.enter_image.start(self.update_image)

    def on_leave(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.press_anim.start(self)
        self.leave_image.start(self.update_image)

class StandardTextInput(TextInput):
    pass

class StandardButton(Button, ButtonBehavior, HoverBehavior):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.press_anim = None

    def on_press(self):
        self.press_anim = Animation(col=(0, 0, 179 / 255, 1), duration=0.15)
        self.press_anim.start(self)

    def on_release(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.press_anim.start(self)

    def on_enter(self):
        self.press_anim = Animation(col=(0, 0, 230 / 255, 1), duration=0.15)
        self.press_anim.start(self)

    def on_leave(self):
        self.press_anim = Animation(col=(51 / 255, 51 / 255, 1, 1), duration=0.15)
        self.press_anim.start(self)

class StandardToggle(ToggleButton, ToggleButtonBehavior, HoverBehavior):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.leave_anim = None
        self.hover_anim = None
        self.press_anim = None

    def on_press(self):
        if self.state == "normal":
            self.state = "down"

    def on_state(self, widget, value):
        if value == "down":
            self.press_anim = Animation(col=(77 / 255, 1, 1, 1), duration=0.15)
            self.press_anim.start(self)
        else:
            self.press_anim = Animation(col=(0, 153/255, 153/255, 1), duration=0.15)
            self.press_anim.start(self)

    def on_enter(self):
        self.hover_anim = Animation(col=(0, 163 / 255, 204 / 255, 1), duration=0.15)
        self.hover_anim.start(self)

    def on_leave(self):
        if self.state == "down":
            self.leave_anim = Animation(col=(0, 153 / 255, 153 / 255, 1), duration=0.15)
            self.leave_anim.start(self)
        else:
            self.leave_anim = Animation(col=(77 / 255, 1, 1, 1), duration=0.15)
            self.leave_anim.start(self)

class PairLabel(Label):
    pass

class PriceLabel(Label):
    pass

class TimeLabel(Label):
    pass