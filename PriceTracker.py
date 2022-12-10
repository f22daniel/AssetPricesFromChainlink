import sys

import requests.exceptions
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from PriceTrackerWidgets import *
from PriceTrackerVariables import *
from web3 import Web3
import ast
from datetime import datetime
from datetime import datetime as d
import time as t
import threading

Builder.load_file('PriceTracker.kv')
Window.size = (500, 650)

w3 = ""

class PriceTracking(Widget):

    def __init__(self, **kwargs):
        super(PriceTracking, self).__init__(**kwargs)
        global w3
        try:
            print(f"Infura API: {settings_price_tracker.infura_api}")
            w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{settings_price_tracker.infura_api}"))  # Web 3 API
            variables_tracker.contract_address = Web3.toChecksumAddress(variables_tracker.contract_address)
            variables_tracker.contract = w3.eth.contract(address=variables_tracker.contract_address, abi=variables_tracker.abi)  # Contract connection
            variables_tracker.abi = ast.literal_eval(variables_tracker.abi)  # Conversion of abi from string to dictionary
            self.ids.error_label.text = "No errors"
            self.super = []  # Keeping track of the hot keys
            # this part of the code requests the keyboard to perform key bindings, it can be put in a method and called at need
            keyboard = Window.request_keyboard(self.keyboard_released, self)
            keyboard.bind(on_key_down=self.keyboard_on_key_down, on_key_up=self.keyboard_released)
            self.update_prices()
            self.update_widgets()
            self.run_update_time()

        except requests.exceptions.HTTPError as e:
            print(e)
        except KeyError as e:
            print(e)

    def update_time(self):

        while variables_tracker.run_time is True:

            # timestamp to time format (delay time)
            def calculate_time_delta(time):
                time = int(time)
                day = time // (24 * 3600)
                time = time % (24 * 3600)
                hour = time // 3600
                time %= 3600
                minutes = time // 60
                time %= 60
                if day != 0:
                    return "%d day %d hour %d min ago" % (day, hour, minutes)
                elif day == 0 and hour != 0:
                    return "%d hour %d min ago" % (hour, minutes)
                elif day == 0 and hour == 0 and minutes != 0:
                    return "%d min ago" % minutes
                else:
                    return "now"

            present_time = d.now()
            present_time = present_time.strftime('%H:%M  %d-%m-%Y')  # Present time formatting
            timestamp = datetime.now().timestamp()  # Current timestamp
            timestamp = int(timestamp)
            update_delta = timestamp - int(variables_tracker.updated_timestamp)  # Calculating time latency
            update_delta = calculate_time_delta(update_delta)  # Time latency conversion
            self.ids.time_label.text = present_time
            self.ids.status_label.text = f"Last updated: {update_delta}"
            t.sleep(1/2)

    @staticmethod
    def exit_app():
        variables_tracker.run_time = False  # Threaded loop kill
        sys.exit()  # Program termination

    def run_update_time(self):
        t1 = threading.Thread(target=self.update_time)  # Set a thread for time label
        t1.start()

    def run_update_prices(self):
        t2 = threading.Thread(target=self.repeat_update_prices)  # Set a thread for prices update
        t2.start()

    def repeat_update_prices(self):
        self.ids.update_button.start_rotation()
        self.update_prices()

        for i, p in enumerate(variables_tracker.keys):
            price_list = ast.literal_eval(variables_tracker.data_prices[p])

            if "Eth" not in p or "EthUsd" in p:
                self.ids[f"price_{i}"].text = f"{round(float(price_list[0])/10**8, 3)}"
            else:
                self.ids[f"price_{i}"].text = f"{round(float(price_list[0])/10**18, 6)}"

            self.ids[f"time_{i}"].text = price_list[1]

        self.ids.update_button.stop_rotation()

    @staticmethod
    def update_prices():
        variables_tracker.data_prices = {}
        threads = []
        variables_tracker.keys = []
        variables_tracker.widget_keys = []

        def calculate_time_delta(time):
            time = int(time)
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            if day != 0:
                return "%dd %dh %dm ago" % (day, hour, minutes)
            elif day == 0 and hour != 0:
                return "%dh %dm ago" % (hour, minutes)
            elif day == 0 and hour == 0 and minutes != 0:
                return "%dm ago" % minutes

        def thread_operation(i):
            try:
                price_time = eval(f'variables_tracker.contract.functions.{variables_tracker.abi[i]["name"]}().call()')

                time_delta = int(datetime.now().timestamp()) - price_time[1]  # Calculating price update latency
                price_time[1] = str(calculate_time_delta(time_delta))  # Timestamp conversion into time format

                # print({f'{variables_tracker.abi[i]["name"]}': f"{price_time}"})
                variables_tracker.data_prices.update({f'{variables_tracker.abi[i]["name"]}': f"{price_time}"})
            except requests.exceptions.HTTPError as e:
                print(e)
                variables_tracker.data_prices.update({f'{variables_tracker.abi[i]["name"]}': f"data error"})

        # API call threads setup
        for n in range(1, 58):
            price_thread = threading.Thread(target=thread_operation, args=(n,))
            threads.append(price_thread)
            variables_tracker.keys.append(f'{variables_tracker.abi[n]["name"]}')  # Key list creation
            price_thread.start()

        for x in threads:
            x.join()

        variables_tracker.keys.sort()

        # Label description key creation
        for x, y in enumerate(variables_tracker.keys):
            slashed_fixed_key = ""
            if x != 0:
                fixed_key = y[9:]
                for i, l in enumerate(reversed(fixed_key)):
                    if i == 2:
                        slashed_fixed_key = "/" + l + slashed_fixed_key
                    else:
                        slashed_fixed_key = l + slashed_fixed_key
            else:
                slashed_fixed_key = y

            variables_tracker.widget_keys.append(slashed_fixed_key)

        variables_tracker.updated_timestamp = datetime.now().timestamp()  # Current timestamp update

        print(variables_tracker.data_prices)
        print(variables_tracker.keys)
        print(variables_tracker.widget_keys)

    def update_widgets(self):

        # Label creation
        for i, p in enumerate(variables_tracker.keys):  # i = Iterator, p = Pairing
            # print(i, p)
            try:
                # Pair extraction
                if p == "TotalMarketCapUsd":
                    pair_label = PairLabel(text="CryptoCap/Usd")
                else:
                    pair_label = PairLabel(text=f"{variables_tracker.widget_keys[i]}")

                price_list = ast.literal_eval(variables_tracker.data_prices[p])  # Conversion from string to list

                # Price extraction
                if "Eth" not in p or "EthUsd" in p:
                    price_label = PriceLabel(text=f"{round(float(price_list[0])/10**8, 3)}")
                    self.ids[f"price_{i}"] = price_label
                else:
                    price_label = PriceLabel(text=f"{round(float(price_list[0])/10**18, 6)}")
                    self.ids[f"price_{i}"] = price_label

                time_label = TimeLabel(text=f"{price_list[1]}")  # Time extraction
                self.ids[f"time_{i}"] = time_label

                # Widget creation
                self.ids.price_widgets.add_widget(pair_label)
                self.ids.price_widgets.add_widget(price_label)
                self.ids.price_widgets.add_widget(time_label)

            except SyntaxError:
                if p == "TotalMarketCapUsd":
                    pair_label = PairLabel(text="CryptoCap/Usd")
                else:
                    pair_label = PairLabel(text=f"{variables_tracker.widget_keys[i]}")

                if "Eth" not in p or "EthUsd" in p:
                    price_label = PriceLabel(text="data error")
                    self.ids[f"price_{i}"] = price_label
                else:
                    price_label = PriceLabel(text="data error")
                    self.ids[f"price_{i}"] = price_label

                time_label = TimeLabel(text=f"data error")

                self.ids.price_widgets.add_widget(pair_label)
                self.ids.price_widgets.add_widget(price_label)
                self.ids.price_widgets.add_widget(time_label)

                self.ids.error_label.text = "Error occured, check API and restart the app"
                # self.ids.error_label.color = (1, 0, 0, 0)

    # Keyboard control code
    def keyboard_released(self, window, keycode):
        self.super = []

    def keyboard_on_key_down(self, window, keycode, text, super):

        if 'lctrl' in self.super and keycode[1] == 'u':
            self.run_update_prices()
        elif 'lctrl' in self.super and keycode[1] == 'q':
            self.exit_app()
        elif 'lctrl' not in self.super and keycode[1] in ['lctrl']:
            self.super.append(keycode[1])

# Popup window for settings
class SettingsPopup(Popup):

    def __init__(self, **kwargs):
        super(SettingsPopup, self).__init__(**kwargs)
        self.ids.infura_api.text = settings_price_tracker.infura_api

    def update_infura_api(self, value, input):
        global w3
        if not value:
            self.ids.infura_api.text = input
            settings_price_tracker.infura_api = input
            settings_price_tracker.infura_link = f"https://mainnet.infura.io/v3/{input}"
            w3 = Web3(Web3.HTTPProvider(settings_price_tracker.infura_link))
            Settings.update_json(settings_price_tracker)
            print(f"Updated infura: {settings_price_tracker.infura_api}")


class PriceTrackingApp(App):
    price_tracker = PriceTracking()

    def build(self):
        Window.clearcolor = (102/255, 163/255, 1, 1)
        return self.price_tracker

if __name__ == '__main__':
    PriceTrackingApp().run()