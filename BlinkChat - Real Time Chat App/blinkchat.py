from kivymd.uix.behaviors.toggle_behavior import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.scrollview import MDScrollView
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivymd.uix.list import TwoLineListItem, ThreeLineListItem
from kivy.properties import StringProperty, NumericProperty
from datetime import datetime, timedelta
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from functions import *
import pandas as pd
import json
from kivymd.toast import toast

KV = """
ScreenManager:
    Home:
    start_screen:
    email:
    verification:
    chat_screen:
    add_friend:
    profile:
    Change_name:
    account_2:
    verification_2:
    Start_Setting:
    verify_email_screen:
    reset_password_screen:
    block_friends_screen:
    Ai_chatbot_screen:
    Theme_setting_screen:
    Settings_Screen:
    New_message_screen:
    Status_screen:

<Home>:                    # =================== Home =========================
    name: "home"
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Blink Chat"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]  # Open drawer

                    MDScrollView:
                        size_hint: (1, 0.9)
                        MDList:
                            id: chat
                            size_hint_y: None
                            height: self.minimum_height

                    BoxLayout:
                        size_hint: (1, 0.1)
                        padding: [10, 10, 10, 10]
                        spacing: 10

    MDNavigationDrawer:
        id: nav_drawer

        BoxLayout:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "10dp"

            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: "150dp"
                padding: "8dp"

                Image:
                    id: home_image
                    source: 'start_pic2.png'  # Replace with your profile picture path
                    size_hint_x: None
                    width: "100dp"
                    height: "100dp"
                    allow_stretch: True

                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "8dp"
                    spacing: "4dp"

                    MDLabel:
                        id: slide_name
                        text: ""  # Replace with actual user name
                        theme_text_color: "Secondary"
                        font_style: "Subtitle1"
                    
                    MDLabel:
                        id: slide_gmail
                        text: ""  # Replace with actual user ID
                        theme_text_color: "Hint"

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Profile'
                        on_release:
                            app.profile_btn()
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'account'
                            on_release:
                                app.profile_btn()
                                nav_drawer.set_state('close')

                    OneLineIconListItem:
                        text: 'Add Friend'
                        on_release:
                            app.add_friend_btn()
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'account-plus'
                            on_release:
                                app.add_friend_btn()
                                nav_drawer.set_state('close')
                                
                                
                    OneLineIconListItem:
                        text: 'Notification'
                        on_release:
                            app.go_to_new_message_screen()
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'message'
                            on_release:
                                app.chatbot_screen()
                                nav_drawer.go_to_new_message_screen('close')
                                
                    OneLineIconListItem:
                        text: 'Status'
                        on_release:
                            app.go_to_status_screen()
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'text-box'
                            on_release:
                                app.chatbot_screen()
                                nav_drawer.go_to_status_screen('close')
                                
                                
                    OneLineIconListItem:
                        text: 'AI'
                        on_release:
                            app.chatbot_screen()
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'brain'
                            on_release:
                                app.chatbot_screen()
                                nav_drawer.set_state('close')
                                
                    OneLineIconListItem:
                        text: 'Settings'
                        on_release:
                            app.go_to_setting_screen()
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'cog'
                            on_release:
                                app.chatbot_screen()
                                nav_drawer.go_to_setting_screen('close')

                    OneLineIconListItem:
                        text: 'About us'
                        on_release:
                            app.about_us()
                            nav_drawer.set_state('close')
                        IconLeftWidget:
                            icon: 'information-outline'
                            on_release:
                                app.about_us()
                                nav_drawer.set_state('close')
                                
<start_screen>:            # =================== start_screen =================
    name: "start_screen"
    MDBoxLayout:
        orientation: "vertical"
        padding: 10
        spacing: '30dp'

        MDIconButton:
            icon: "cog"
            on_release: app.start_setting_btn()
            pos_hint: {'center_x': 0.95}
            halign: "left"

        MDLabel:
            text: "Welcome to Blink Chat"
            font_style: "H4"
            halign: "center"

        Image:
            source: 'start_pic2.png'
            size_hint_x: None
            width: "340dp"
            height: "270dp"
            halign: "center"
            pos_hint: {'center_x': 0.5}


        MDRaisedButton:
            text: "  Get Start  "
            halign: "center"
            pos_hint: {'center_x': 0.5}
            on_release: app.get_start_btn()

        MDFlatButton:
            text: "Already have an account"
            halign: "center"
            pos_hint: {'center_x': 0.5}
            on_release: app.have_account_btn()
 

        MDLabel:
            text: "Version 1.2.54.34"
            halign: "center"
            
        
        

<email>:                   # =================== email ========================
    name: "email"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False
    MDBoxLayout:
        orientation: "vertical"
        spacing: '20dp'
        padding: 50

        MDLabel:
            text: "Account"
            halign: "center"
            font_style: "H2"

        MDTextField:
            id: name_text
            hint_text: "Name"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "account"

        MDTextField:
            id: gmail_text
            hint_text: "E-mail"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "gmail"
            
        MDTextField:
            id: password_text_1
            hint_text: "Password"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "lock"
        
        MDTextField:
            id: password_text_2
            hint_text: "Re-Password"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "lock"

        MDRaisedButton:
            text: "   Next   "
            halign: "center"
            pos_hint: {'center_x': 0.5}
            on_release: app.next_account()
            
        MDLabel:
            text: ""



<verification>:            # =================== verification =================
    name: "verification"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False
    MDBoxLayout:
        orientation: "vertical"
        spacing: '50dp'
        padding: 50

        MDLabel:
            text: "Activation"
            halign: "center"
            font_style: "H2"

        MDLabel:
            id: gmail_label
            text: "We have sent an activation link to {email}. Please check your inbox and verify your account before signing in."
            halign: "center"
            font_style: "H6"
            

        MDRaisedButton:
            text: "   Sign in   "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.sign_in_next_btn()

        MDIconButton:
            id: back_button
            icon: "arrow-left"
            on_release: app.back_account()
            halign: "left"


        MDLabel:
            text: ""
            halign: "center"



    

            

<chat_screen>:             # =================== chat_screen ==================
    name: "chat_screen"
    MDBottomNavigationItem:
        name: 'screen 3'
        text: 'Messages'
        icon: 'facebook-messenger'
        Image:
            id: start_screen
            source: 'start_screen.jpg'
            allow_stretch: True
            keep_ratio: False

        BoxLayout:
            orientation: 'vertical'

            MDTopAppBar:
                id: chat_screen_top_name
                title: "Chats"
                left_action_items: [["arrow-left", lambda x: app.on_menu_click()]]
                right_action_items: [["dots-vertical", lambda x: app.on_dots_click()]]

            ScrollView:
                MDGridLayout:
                    id: messages_box
                    cols: 1
                    adaptive_height: True
                    padding: dp(20)
                    spacing: dp(20)

            BoxLayout:
                size_hint_y: None
                height: dp(56)
                spacing: dp(10)
                padding: dp(10)

                MDTextField:
                    id: message_input
                    hint_text: "Type a message"
                    mode: "fill"

                MDFloatingActionButton:
                    icon: "send"
                    on_release: app.send_message()



<add_friend>:              # =================== add_friend ===================
    name: "add_friend"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False

    MDBoxLayout:
        orientation: "vertical"
        spacing: '50dp'
        padding: 50

        MDLabel:
            text: "Add Friend"
            halign: "center"
            font_style: "H2"

        MDLabel:
            id: gmail_label
            text: "Type your friend E-mail to add in your chats"
            halign: "center"
            

        MDTextField:
            id: friend_gmail_text
            hint_text: "E-mail"
            pos_hint: {'center_x': 0.5}
            mode: "round"
            icon_left: "email"

        MDRaisedButton:
            text: "   Save   "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.add_friend_save_btn()

        MDIconButton:
            icon: "arrow-left"
            on_release: app.back_add_friend()
            halign: "left"


        MDLabel:
            text: ""
            halign: "center"

<profile>:              # =================== profile ===================
    name: "profile"
    BoxLayout:
        orientation: 'vertical'
                    
        MDTopAppBar:
            title: "Your Profile"
            left_action_items: [["arrow-left", lambda x: app.back_profile()]]

        MDBoxLayout:
            orientation: 'vertical'
            padding: "10dp"

            Image:
                id: porfile_image
                source: 'start_pic2.png'
                size_hint_x: None
                width: "340dp"
                height: "270dp"
                halign: "center"
                pos_hint: {'center_x': 0.5}

            OneLineListItem:
                text: ""
                disabled: True

            OneLineIconListItem:
                id: profile_name
                text: ""
                disabled: True
                IconLeftWidget:
                    icon: "account"

            OneLineIconListItem:
                id: porfile_gmail
                text: ""
                disabled: True
                IconLeftWidget:
                    icon: "gmail"

            OneLineListItem:
                text: ""
                disabled: True

            OneLineIconListItem:
                text: "   All Block Friends"
                on_release: app.all_block_friends()
                IconLeftWidget:
                    icon: "block-helper"
                    on_release: app.all_block_friends()


            OneLineIconListItem:
                text: "   Reset Password"
                on_release: app.reset_password_in_profile()
                IconLeftWidget:
                    icon: "lock-reset"
                    on_release: app.reset_password_in_profile()

            OneLineIconListItem:
                text: "   Logout"
                on_release: app.logout_dialog()
                IconLeftWidget:
                    icon: "logout"
                    on_release: app.logout_dialog()

            MDLabel:
                text: ""

            MDLabel:
                text: ""


<Change_name>:              # =================== Change_name ===================
    name: "Change_name"
    BoxLayout:
        orientation: 'vertical'
                    
        MDTopAppBar:
            title: "Frend profile"
            left_action_items: [["arrow-left", lambda x: app.back_friend_profile()]]

        MDBoxLayout:
            orientation: "vertical"
            padding: 30
            spacing: '10dp'

            Image:
                id: friend_image
                source: 'start_pic2.png'
                size_hint_x: None
                width: "340dp"
                height: "270dp"
                halign: "center"
                pos_hint: {'center_x': 0.5}

            OneLineListItem:
                text: ""
                disabled: True

            OneLineIconListItem:
                id: friend_profile_name
                text: ""
                disabled: True
                IconLeftWidget:
                    icon: "account"

            OneLineIconListItem:
                id: friend_porfile_gmail
                text: ""
                disabled: True
                IconLeftWidget:
                    icon: "gmail"
            
            OneLineIconListItem:
                text: ""
                disabled: True

            OneLineIconListItem:
                text: "   Block"
                on_release: app.block_friend_dialog()
                IconLeftWidget:
                    icon: "block-helper"
                    on_release: app.block_friend_dialog()

            OneLineIconListItem:
                text: "   Delete All Chats"
                on_release: app.delete_friend()
                IconLeftWidget:
                    icon: "delete"
                    on_release: app.delete_friend()
                

            MDLabel:
                text: ""


<account_2>:              # =================== account_2 ===================
    name: "account_2"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False

    MDBoxLayout:
        orientation: "vertical"
        spacing: '50dp'
        padding: 50

        MDLabel:
            text: "Sign in"
            halign: "center"
            font_style: "H4"

        MDLabel:
            id: gmail_label
            text: "Enter your E-mail and Password to sign in"
            halign: "center"

        MDTextField:
            id: account_2_gmail_text
            hint_text: "E-mail"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "gmail"
            
        MDTextField:
            id: account_2_password_text
            hint_text: "Password"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "lock"

        MDRaisedButton:
            text: "   Next   "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.account_2_next_btn()

        MDIconButton:
            icon: "arrow-left"
            on_release: app.back_account_2()
            halign: "left"


        MDLabel:
            text: ""
            halign: "center"

<verification_2>:            # =================== verification_2 =================
    name: "verification_2"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False
    MDBoxLayout:
        orientation: "vertical"
        spacing: '50dp'
        padding: 50

        MDLabel:
            text: "verification"
            halign: "center"
            font_style: "H2"

        MDLabel:
            id: gmail_label_222
            text: ""
            halign: "center"

        MDRaisedButton:
            text: "   Sign in   "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.sign_in_next_btn()

        MDIconButton:
            icon: "arrow-left"
            on_release: app.start_setting_btn()
            halign: "left"


        MDLabel:
            text: ""
            halign: "center"


<Start_Setting>:
    name: "Start_Setting"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False

    MDBoxLayout:
        orientation: "vertical"
        spacing: '50dp'
        padding: 50

        MDLabel:
            text: "Settings"
            font_style: "H2"
            halign: "center"

        MDRaisedButton:
            text: "     Verify Email     "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.verify_email()

        MDRaisedButton:
            text: "   Reset Password   "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.reset_password()

        MDIconButton:
            icon: "arrow-left"
            on_release: app.back_account_2()
            halign: "left"


        MDLabel:
            text: ""
            halign: "center"


<reset_password_screen>:
    name: "reset_password_screen"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False

    MDBoxLayout:
        orientation: "vertical"
        spacing: '50dp'
        padding: 50

        MDLabel:
            text: "Reset Password"
            halign: "center"
            font_style: "H2"

        MDLabel:
            text: "Type your E-mail to get Reset Password link"
            halign: "center"
            
        MDTextField:
            id: reset_password_email_text
            hint_text: "E-mail"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "email"

        MDRaisedButton:
            text: "   Send Link   "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.rest_password_btn()

        MDIconButton:
            icon: "arrow-left"
            on_release: app.start_setting_btn()
            halign: "left"

        MDLabel:
            text: ""
            halign: "center"


<verify_email_screen>:
    name: "verify_email_screen"
    Image:
        id: start_screen
        source: 'start_screen.jpg'
        allow_stretch: True
        keep_ratio: False

    MDBoxLayout:
        orientation: "vertical"
        spacing: '50dp'
        padding: 50

        MDLabel:
            text: "Verify Email"
            halign: "center"
            font_style: "H2"

        MDLabel:
            text: "Type your E-mail to get verification link"
            halign: "center"
            

        MDTextField:
            id: verify_email_text
            hint_text: "E-mail"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "email"

        MDTextField:
            id: verify_password_text
            hint_text: "Password"
            pos_hint: {'center_x': 0.5}
            mode: "rectangle"
            icon_left: "lock"

        MDRaisedButton:
            text: "   Send Link   "
            halign: "right"
            pos_hint: {'center_x': 0.5}
            on_release: app.verify_email_btn()

        MDIconButton:
            id: verify_back_btn
            icon: "arrow-left"
            on_release: app.start_setting_btn()
            halign: "left"


        MDLabel:
            text: ""
            halign: "center"

<block_friends_screen>:
    name: "block_friends_screen"
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Block Friends"
            left_action_items: [["arrow-left", lambda x: app.back_to_block_friends()]]

        MDScrollView:
            size_hint: (1, 0.9)
            MDList:
                id: block_friends_id
                size_hint_y: None
                height: self.minimum_height

        BoxLayout:
            size_hint: (1, 0.1)
            padding: [10, 10, 10, 10]
            spacing: 10
            
            
<Ai_chatbot_screen>:
    name: "Ai_chatbot_screen"
    MDBottomNavigationItem:
        name: 'screen 3'
        text: 'Messages'
        icon: 'facebook-messenger'
        Image:
            id: start_screen
            source: 'start_screen.jpg'
            allow_stretch: True
            keep_ratio: False

        BoxLayout:
            orientation: 'vertical'

            MDTopAppBar:
                id: chat_screen_top_name_for_ai
                title: "AI"
                left_action_items: [["arrow-left", lambda x: app.back_to_ai_screen()]]
                right_action_items: [["dots-vertical", lambda x: app.ai_chatbot_profile()]]

            ScrollView:
                MDGridLayout:
                    id: messages_box_for_ai
                    cols: 1
                    adaptive_height: True
                    padding: dp(20)
                    spacing: dp(20)

            BoxLayout:
                size_hint_y: None
                height: dp(56)
                spacing: dp(10)
                padding: dp(10)

                MDTextField:
                    id: message_input_to_ai
                    hint_text: "Ask any thing"
                    mode: "fill"

                MDFloatingActionButton:
                    icon: "send"
                    on_release: app.send_message_to_ai()
                    
                    
<Settings_Screen>:
    name: "Settings_Screen"
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Settings"
            left_action_items: [["arrow-left", lambda x: app.back_to_ai_screen()]]
            
        MDScrollView:
            size_hint: (1, 0.9)
            
            OneLineIconListItem:
                text: "Change Theme"
                on_release: app.go_to_change_theme_screen()
        
        
    
    
<Theme_setting_screen>:
    name: "Theme_setting_screen"
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Change Theme"
            left_action_items: [["arrow-left", lambda x: app.go_to_setting_screen()]]
            
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(20)
            
            MDRaisedButton:
                id: theme_button
                text: "   Choose Theme Style   "
                pos_hint: {"center_x": 0.5}
                on_release: app.open_theme_style_menu(self)

            MDRaisedButton:
                id: palette_button
                text: "Choose Primary Palette"
                pos_hint: {"center_x": 0.5}
                on_release: app.open_primary_palette_menu(self)
                
            MDLabel:
                text: ""
                
                
<New_message_screen>:
    name: "New_message_screen"
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Notification"
            left_action_items: [["arrow-left", lambda x: app.back_to_ai_screen()]]
            
        MDScrollView:
            size_hint: (1, 0.9)
            MDList:
                id: new_chat
                size_hint_y: None
                height: self.minimum_height
                
                
<Status_screen>:
    name: "Status_screen"
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Status"
            left_action_items: [["arrow-left", lambda x: app.back_to_ai_screen()]]
            right_action_items: [["dots-vertical", lambda x: app.open_menu(x)]]
            
        OneLineIconListItem:
            id: user_status_icon
            text: "My Status"
            on_release: app.add_user_status()
            IconLeftWidget:
                id: user_status_icon
                icon: "plus" 
                on_release: app.add_user_status()
            
        MDScrollView:
            size_hint: (1, 0.9)
            
            MDList:
                id: status
                size_hint_y: None
                height: self.minimum_height

"""

# ============================== Show uesrs friends on home screen ==============================

def show_friends(self):
    try:
        self.root.get_screen('home').ids.chat.clear_widgets()
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        self.friend_data = get_friends_in_chat(user_email, token)
        self.new_chats = False
        self.block_friends = get_block_friend(user_email, token)

        if self.block_friends is not None:
            self.block_friends_emails = [user["email"] for user in self.block_friends.values()]
        else:
            self.block_friends_emails = ["No Block Friend"]
        

        for user in self.friend_data.values():
            email = user["email"]
            if email not in self.block_friends_emails:
                name = user["name"]
                self.user_friends = self.root.get_screen('home').ids.chat
                self.user_friends.add_widget(TwoLineListItem(text=name, secondary_text=email, on_release=self.on_item_click))
    except:
        pass
def show_block_friends(self):
    try:
        self.user_block_friends = self.root.get_screen('block_friends_screen').ids.block_friends_id
        self.user_block_friends.clear_widgets()  # Clears previous list items

        for user in self.block_friends.values():
            email = user.get("email", "Unknown Email")  # Use .get() to avoid KeyError
            name = user.get("name", "Unknown Name")

            item = TwoLineListItem(
                text=name,
                secondary_text=email,
                on_release=lambda x, n=name, e=email: self.show_block_friend_info(n, e)  # Pass email correctly
            )
            self.user_block_friends.add_widget(item)

    except:
        pass  # Proper error message




class MessageBubble4(MDBoxLayout):
    def __init__(self, username, text, timestamp, is_sent_by_user=False, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.padding = dp(10)
        self.is_sent_by_user = is_sent_by_user
        self.spacing = dp(-15)  # Added spacing between username and text

        self.canvas.before.clear()
        with self.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(rgba=(0.94, 0.94, 0.94, 1) if self.is_sent_by_user else (0.85, 0.85, 0.85, 1))
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(15)] * 4)

        self.bind(pos=self.update_rect, size=self.update_rect)

        bubble_content = MDBoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(5))
        
        self.username_label = MDLabel(
            text=f"[b]{username}[/b]",
            theme_text_color='Custom',  # Change from 'Secondary' to 'Custom'
            text_color=(0, 0, 0, 1),    # Set the desired color (Red in this case)
            markup=True,
            size_hint_y=None,
            height=dp(20)
        )


        self.message_label = MDLabel(
            text=text,
            theme_text_color='Custom',
            text_color=(0, 0, 0, 1),
            size_hint_y=None,
            markup=True
        )
        self.message_label.texture_update()
        self.message_label.bind(texture_size=self.update_height)
        
        self.timestamp_label = MDLabel(
            text=timestamp,
            theme_text_color='Custom',
            text_color=(0.5, 0.5, 0.5, 1),
            size_hint_y=None,
            height=dp(20),
            padding=(dp(10), dp(10)),
            font_style='Caption',
            halign='right',
            valign='middle'
        )

        bubble_content.add_widget(self.username_label)
        bubble_content.add_widget(self.message_label)
        self.add_widget(bubble_content)
        self.add_widget(self.timestamp_label)
    
    def update_height(self, instance, size):
        self.height = size[1] + dp(60)
        self.message_label.height = size[1]
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class CustomTextInput(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = "10dp"
        self.size_hint_y = None
        self.height = "180dp"  # Adjusted height

        # ScrollView to allow scrolling inside text input
        self.scroll_view = MDScrollView(
            size_hint=(1, None),
            height="100dp",  # Matches text field height
            bar_width="4dp"  # Thin scrollbar
        )

        self.text_input = MDTextField(
            hint_text="Write your status here...",
            multiline=True,
            size_hint_y=None,
            mode="rectangle",
            height="100dp",  # Fixed height
            font_size="16sp",
        )
        self.text_input.bind(text=self.update_character_count)

        self.char_count_label = MDLabel(
            text="0 / 250",
            theme_text_color="Secondary",
            font_style="Caption",
            halign="right",
            size_hint_y=None,
            height="20dp"
        )

        # Add text field inside scroll view
        self.scroll_view.add_widget(self.text_input)
        self.add_widget(self.scroll_view)
        self.add_widget(self.char_count_label)

    def update_character_count(self, instance, value):
        if len(value) > 250:
            self.text_input.text = value[:250]  # Enforce 250-character limit
        self.char_count_label.text = f"{len(self.text_input.text)} / 250"
        
class Home(Screen):
    pass

class start_screen(Screen):
    pass

class account_2(Screen):
    pass

class email(Screen):
    pass

class profile(Screen):
    pass

class Change_name(Screen):
    pass

class verification(Screen):
    pass

class verification_2(Screen):
    pass

class chat_screen(Screen):
    pass

class add_friend(Screen):
    pass

class Start_Setting(Screen):
    pass

class reset_password_screen(Screen):
    pass

class verify_email_screen(Screen):
    pass

class block_friends_screen(Screen):
    pass

class Ai_chatbot_screen(Screen):
    pass

class Settings_Screen(Screen):
    pass

class Theme_setting_screen(Screen):
    pass

class New_message_screen(Screen):
    pass

class Status_screen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        self.title = "Blink Chat"
        Window.size = (700, 600)
        self.dialog = None
        
        self.last_time = ["0"]
        self.Conversation = [{"role": "system", "content": "You are an AI assistant in a chat application."}]

        return Builder.load_string(KV)
    
    
# ============================== About US ==============================
    
    def about_us(self):
        self.about_us_dilog = MDDialog(
            title = "About US",
            text = "Blink Chat is a cutting-edge messaging app designed for secure, private communication. With end-to-end encryption, your messages are protected from unauthorized access, ensuring complete privacy. The app provides real-time messaging with a sleek, user-friendly interface that’s easy to navigate. Computer, Blink Chat allows seamless cross-platform communication. "+
            "Key features include customizable chat themes, secure file sharing, and group chat options, making it ideal for both personal and professional use. Message history is encrypted and stored safely, so you can access past conversations anytime. Push notifications ensure you never miss a message, even when you’re not actively using the app."+
            "Blink Chat is perfect for anyone looking to maintain privacy without sacrificing convenience. Whether you’re chatting with friends, family, or colleagues, Blink Chat offers a secure and efficient messaging experience that you can trust."
        )
        self.about_us_dilog.open()

# ============================== Status Screen ==============================

    def open_menu(self, button):
        options = ["Delete Status"]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": option,
                "on_release": lambda option=option: self.status_menu_button(option),
            }
            for option in options
        ]
        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=3
        )
        self.menu.open()
        
    def status_menu_button(self, option):
        self.menu.dismiss()
        if option == "Delete Status":
            self.error_dilogbox = MDDialog(
                title = "Status",
                text = "Are you sure to delete your status.",
                buttons = [
                    MDFlatButton(text="Yes", on_release=self.delete_status)
                ])
            self.error_dilogbox.open()
            
    def delete_status(self, obj):
        self.error_dilogbox.dismiss(force=True)
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        status = delete_user_status(user_email, token)
        if status:
            toast("Your status deleted successfully.")
            self.root.get_screen('Status_screen').ids.user_status_icon.icon = "plus"
            self.user_status = False
                
        
        
        
    def go_to_status_screen(self):
        self.root.get_screen('Status_screen').ids.user_status_icon.icon = "plus"
        self.user_status = False
        self.user_friends = self.root.get_screen('Status_screen').ids.status
        self.user_friends.clear_widgets()
        
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        
        user_friends_email_list = [email["email"] for email in self.friend_data.values()]
        user_friends_email_list.append(user_email)
        
        self.status = get_all_status(user_friends_email_list, token)
        
        if self.status:
            now = datetime.now()
            for user in self.status.values():
                email = user["email"]
                status_time_str = user["time"]
                
                # Convert status time string to datetime object
                status_time = datetime.strptime(status_time_str, "%Y-%m-%d %I:%M:%S %p")
                
                # Check if the status is within the last 24 hours
                if status_time >= now - timedelta(hours=24):
                    if email not in self.block_friends_emails and email != user_email:
                        name = user["name"]
                        self.user_friends.add_widget(
                            ThreeLineListItem(
                                text=name, 
                                secondary_text=email, 
                                tertiary_text=status_time_str, 
                                on_release=self.show_status
                            )
                        )
                    elif email == user_email:
                        self.root.get_screen('Status_screen').ids.user_status_icon.icon = "check"
                        self.user_status = True
                        
        self.root.current = "Status_screen"

        
    def show_status(self, instance):
        name = instance.text
        friend_email = instance.secondary_text
        status = self.status[friend_email]["status"]
        self.status_dilog = MDDialog(
            title=f"{name} Status",
            text = status
        )
        self.status_dilog.open()
      
    def add_user_status(self):
        if self.user_status:
            data = pd.read_csv("user_data.csv")
            user_email = data["email"].iloc[0]
            status = self.status[user_email]["status"]
            self.status_dilog = MDDialog(
                title="Your Status",
                text = status
            )
            self.status_dilog.open()
        else:
            self.show_dialog()
    
    def show_dialog(self):
        if not self.dialog:
            self.text_input_component = CustomTextInput()

            self.dialog = MDDialog(
                title="Enter Status",
                type="custom",
                content_cls=self.text_input_component,
                buttons=[
                    MDRaisedButton(text="Submit", on_release=self.submit_text),
                    MDRaisedButton(text="Cancel", on_release=lambda x: self.dialog.dismiss())
                ]
            )
        self.dialog.open()

    def submit_text(self, instance):
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        user_name = data["name"].iloc[0]
        time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        user_status = self.text_input_component.text_input.text
        status_data = {"name": user_name, "email": user_email, "status": user_status, "time": time}
        status = add_status(user_email, user_name, user_status, time, token)
        if status:
            toast("Your status add successfully.")
            self.root.get_screen('Status_screen').ids.user_status_icon.icon = "check"
            self.user_status = True
            self.status[user_email] = status_data
        self.dialog.dismiss()
        
    
        
# ============================== Notification Screen ==============================
        
    def go_to_new_message_screen(self):
        self.user_friends = self.root.get_screen('New_message_screen').ids.new_chat
        self.user_friends.clear_widgets()
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        
        self.new_chats = get_new_chats(user_email, token)
        
        if self.new_chats:
            for user in self.new_chats.values():
                email = user["email"]
                if email not in self.block_friends_emails:
                    name = user["name"]
                    time = user["time"]
                    self.user_friends.add_widget(ThreeLineListItem(text=name, secondary_text=email, tertiary_text=time, on_release=self.on_item_click))
                    
        self.root.current = "New_message_screen"
        
        
# ============================== Settings Screen ==============================

    def go_to_setting_screen(self):
        self.root.current = "Settings_Screen"
        
    def go_to_change_theme_screen(self):
        self.root.current = "Theme_setting_screen"
        
    def open_theme_style_menu(self, button):
        themes = ["Light", "Dark"]
        menu_items = [
            {"viewclass": "OneLineListItem", "text": theme, "on_release": lambda theme=theme: self.set_theme_style(theme)}
            for theme in themes
        ]
        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=3
        )
        self.menu.open()
        
        
    def open_primary_palette_menu(self, button):
        palettes = ["Red", "Pink", "Purple", "DeepPurple", "Indigo", "Blue", "LightBlue", "Cyan", "Teal", "Green", "LightGreen", "Lime", "Yellow", "Amber", "Orange", "DeepOrange", "Brown", "Gray", "BlueGray"]
        menu_items = [
            {"viewclass": "OneLineListItem", "text": palette, "on_release": lambda palette=palette: self.set_primary_palette(palette)}
            for palette in palettes
        ]
        self.palette_menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=3
        )
        self.palette_menu.open()
    
    def set_theme_style(self, theme_style):
        self.theme_cls.theme_style = theme_style
        self.save_theme(theme_style, self.theme_cls.primary_palette)
        self.menu.dismiss()
    
    def set_primary_palette(self, palette):
        self.theme_cls.primary_palette = palette
        self.save_theme(self.theme_cls.theme_style, palette)
        self.palette_menu.dismiss()
        
    def save_theme(self, theme_style, palette):
        data = {"Theme Style": [theme_style], "Primary Palette": [palette]}
        df = pd.DataFrame(data)
        df.to_csv("theme_settings.csv", index=False)
        
    
        
# ============================== AI Chatbot Screen ==============================
    def chatbot_screen(self):
        chat_screen = self.root.get_screen('Ai_chatbot_screen')
        messages_box = chat_screen.ids.messages_box_for_ai
        messages_box.clear_widgets()
        
        for i in self.Conversation:
            if i["role"] == "user":
                sender_name = "You"
                is_sent_by_user = True
            elif i["role"] == "assistant":
                sender_name = "AI"
                is_sent_by_user = False
                
            else:
                sender_name = None
                    
            if sender_name:
                new_message = MessageBubble4(
                    username=sender_name,
                    text=i["content"],
                    timestamp="",
                    is_sent_by_user=is_sent_by_user
                )
                messages_box.add_widget(new_message)
                    
        chat_screen.ids.messages_box_for_ai.scroll_y = 1
        self.root.current = "Ai_chatbot_screen"  
        
    def back_to_ai_screen(self):
        self.root.current = "home"
        
    def send_message_to_ai(self):
        chat_screen = self.root.get_screen('Ai_chatbot_screen')
        messages_box = chat_screen.ids.messages_box_for_ai
        message = chat_screen.ids.message_input_to_ai.text
        if message:
            self.Conversation.append({"role": "user", "content": message})
            answer = get_ai_answer(self.Conversation)
            self.Conversation.append({"role": "assistant", "content": answer})
            if answer:
                messages_box.clear_widgets()
                with open("AI_User_chats.json", "w") as file:
                    json.dump(self.Conversation, file, indent=4)
                    
                for i in self.Conversation:
                    if i["role"] == "user":
                        sender_name = "You"
                        is_sent_by_user = True
                    elif i["role"] == "assistant":
                        sender_name = "AI"
                        is_sent_by_user = False
                        
                    else:
                        sender_name = None
                        
                    if sender_name:
                        new_message = MessageBubble4(
                            username=sender_name,
                            text=i["content"],
                            timestamp="",
                            is_sent_by_user=is_sent_by_user
                        )
                        messages_box.add_widget(new_message)

                chat_screen.ids.message_input_to_ai.text = ""

    def ai_chatbot_profile(self):
        self.error_dilogbox = MDDialog(
                title = "AI",
                text = "Do you want to clean all Conversation with AI.",
                buttons = [
                    MDFlatButton(text="No", on_release=self.dilog_close),
                    MDFlatButton(text="Yes", on_release=self.clean_all_conversation)
                ])
        self.error_dilogbox.open()
        
    def clean_all_conversation(self, obj):
        self.error_dilogbox.dismiss(Force=True)
        with open("AI_User_chats.json", "w") as file:
            self.root.get_screen('Ai_chatbot_screen').ids.messages_box_for_ai.clear_widgets()
            self.Conversation = [{"role": "system", "content": "You are an AI assistant in a chat application."}]
            json.dump(self.Conversation, file, indent=4)
            
            
        self.error_dilogbox = MDDialog(
                title = "AI",
                text = "Your Conversation with AI is Clean.",
                buttons = [
                    MDFlatButton(text="OK", on_release=self.dilog_close)
                ])
        self.error_dilogbox.open()
        
        
        
        
# ============================== Block Friends ==============================

    def all_block_friends(self):
        self.root.current = "block_friends_screen"

    def back_to_block_friends(self):
        self.root.current = "profile"

    def show_block_friend_info(self, name, email):
        self.block_friend_name = name
        self.block_friend_email = email
        self.confirm_logout_dialog = MDDialog(
            title="UnBlock Friend",
            text=f"Are you show to unblock {name}.",
            buttons=[
                MDFlatButton(text="No", on_release=self.reset_password_dilog_close),
                MDRaisedButton(text="Yes", on_release=self.unblock_friend)
            ]
        )
        self.confirm_logout_dialog.open()

    def unblock_friend(self, obj):
        self.confirm_logout_dialog.dismiss(force=True)
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]

        friends_id = [user for user in self.block_friends]
        friends_email = [user["email"] for user in self.block_friends.values()]

        if friends_email and friends_id:
            for i, m in enumerate(friends_email):
                if m == self.block_friend_email:
                    friend_id = friends_id[i]
                    unblock = unblock_user_friend(user_email, friend_id, token)
                    if unblock:
                        show_friends(self)
                        show_block_friends(self)
                        self.error_dilogbox = MDDialog(
                            title="UnBlock Friend",
                            text=f"{self.block_friend_name} is unblock.",
                            buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
                        )
                        self.error_dilogbox.open()
                    else:
                        self.error_dilogbox = MDDialog(
                            title="UnBlock Friend",
                            text=f"{self.block_friend_name} is not unblock.",
                            buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
                        )
                        self.error_dilogbox.open()
                    break




# ============================== Start Settings ==============================
    def reset_password_in_profile(self):
        self.confirm_logout_dialog = MDDialog(
            title="Reset Password",
            text="You need to log out before resetting your password. Do you want to continue?",
            buttons=[
                MDFlatButton(text="Cancel", on_release=self.reset_password_dilog_close),
                MDRaisedButton(text="Logout", on_release=self.logout_and_reset_password)
            ]
        )
        self.confirm_logout_dialog.open()

    def logout_and_reset_password(self, obj):
        self.confirm_logout_dialog.dismiss(force=True)
        with open("password.txt", "w") as file:
            file.write("")
            pd.DataFrame().to_csv("user_data.csv", index=False)
            self.root.current = "reset_password_screen"

    def logout_dialog(self):
        self.confirm_logout_dialog = MDDialog(
            title="Logout",
            text="Are you sure for logout.",
            buttons=[
                MDFlatButton(text="Cancel", on_release=self.reset_password_dilog_close),
                MDRaisedButton(text="Logout", on_release=self.logout)
            ]
        )
        self.confirm_logout_dialog.open()

    def logout(self, obj):
        self.confirm_logout_dialog.dismiss(force=True)
        with open("password.txt", "w") as file:
            file.write("")
            pd.DataFrame().to_csv("user_data.csv", index=False)
            self.root.current = "start_screen"

    def reset_password_dilog_close(self, obj):
        self.confirm_logout_dialog.dismiss(force=True)



    def start_setting_btn(self):
        self.root.current = "Start_Setting"

    def verify_email(self):
        self.root.current = "verify_email_screen"

    def reset_password(self):
        self.root.current = "reset_password_screen"

    def verify_email_btn(self):
        email = self.root.get_screen('verify_email_screen').ids.verify_email_text.text
        password = self.root.get_screen('verify_email_screen').ids.verify_password_text.text

        if email == "" and password == "":
            self.error_dilogbox = MDDialog(
                title="Verify Email",
                text=f"Please Enter your Email or Pasword.",
                buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()

        elif email.lower() != email:
            self.error_dilogbox = MDDialog(
                title="Verify Email",
                text=f"You email is InCorrect. Please Check!",
                buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()

        else:
            link = send_verification_email(email, password)
            if link:
                self.root.get_screen('verification_2').ids.gmail_label_222.text = f"We have sent an activation link to {email}. Please check your inbox and verify your account before signing in."
                self.root.current = "verification_2"
            else:
                self.error_dilogbox = MDDialog(
                    title = "Verify Email",
                    text = "Your Email and Password is InCorrect. Please Check!",
                    buttons = [
                        MDFlatButton(text="OK", on_release=self.dilog_close)
                    ])
                self.error_dilogbox.open()


    def rest_password_btn(self):
        email = self.root.get_screen('reset_password_screen').ids.reset_password_email_text.text

        if email == "":
            self.error_dilogbox = MDDialog(
                title="Reset Password",
                text=f"Please Enter your Email.",
                buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()

        elif email.lower() != email:
            self.error_dilogbox = MDDialog(
                title="Reset Password",
                text=f"You email is InCorrect. Please Check!",
                buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()

        else:
            link = reset_password(email)
            if link:
                self.root.get_screen('verification_2').ids.gmail_label_222.text = f"We have sent an activation link to {email}. Please check your inbox and reset your account password before signing in."
                self.root.current = "verification_2"
            else:
                self.error_dilogbox = MDDialog(
                    title = "Verify Email",
                    text = "Your Email is InCorrect. Please Check!",
                    buttons = [
                        MDFlatButton(text="OK", on_release=self.dilog_close)
                    ])
                self.error_dilogbox.open()

        
# ============================== Create Account ==============================

    def on_start(self):
        try:
            data = pd.read_csv("user_data.csv")
    
            if data.empty:
                self.root.current = "start_screen"
            else:
                with open("password.txt", "r") as file:
                    user_password = file.read()
                    user_email = data["email"].iloc[0]

                if user_email and user_password:
                    user = sign_in(user_email, user_password)
                    user_verifi = user_is_verifiaction(user["idToken"])
                else:
                    self.root.current = "start_screen"
                
                if user_verifi:
                    self.root.current = "home"
                else:
                    self.root.current = "start_screen"

                if user is not None:
                    data.loc[0, "idToken"] = user["idToken"]
                    data.to_csv("user_data.csv", index=False)
                    
                    chatbot_config = get_chatbot_config_data(user["idToken"])
                    df = pd.DataFrame(chatbot_config.values()) 
                    df.to_csv("chatbot_config.csv", index=False)

        except:
            self.root.current = "start_screen"
        try:
            with open("AI_User_chats.json", "r") as file:
                self.Conversation = json.load(file)
        except:
            pass
           
        show_friends(self)
        show_block_friends(self)
        try:
            data = pd.read_csv("theme_settings.csv")
            self.theme_cls.theme_style = data["Theme Style"][0]
            self.theme_cls.primary_palette = data["Primary Palette"][0]
            if data["Theme Style"][0] == "Light":
                img_source = "start_screen_light.jpg"
                self.root.get_screen('email').ids.start_screen.source = img_source
                self.root.get_screen('verification').ids.start_screen.source = img_source
                self.root.get_screen('chat_screen').ids.start_screen.source = img_source
                self.root.get_screen('add_friend').ids.start_screen.source = img_source
                self.root.get_screen('account_2').ids.start_screen.source = img_source
                self.root.get_screen('verification_2').ids.start_screen.source = img_source
                self.root.get_screen('Start_Setting').ids.start_screen.source = img_source
                self.root.get_screen('reset_password_screen').ids.start_screen.source = img_source
                self.root.get_screen('verify_email_screen').ids.start_screen.source = img_source
                self.root.get_screen('Ai_chatbot_screen').ids.start_screen.source = img_source

        except:
            img_source = "start_screen_light.jpg"
            self.root.get_screen('email').ids.start_screen.source = img_source
            self.root.get_screen('verification').ids.start_screen.source = img_source
            self.root.get_screen('chat_screen').ids.start_screen.source = img_source
            self.root.get_screen('add_friend').ids.start_screen.source = img_source
            self.root.get_screen('account_2').ids.start_screen.source = img_source
            self.root.get_screen('verification_2').ids.start_screen.source = img_source
            self.root.get_screen('Start_Setting').ids.start_screen.source = img_source
            self.root.get_screen('reset_password_screen').ids.start_screen.source = img_source
            self.root.get_screen('verify_email_screen').ids.start_screen.source = img_source
            self.root.get_screen('Ai_chatbot_screen').ids.start_screen.source = img_source
    
# ============================== Message Screen ==============================
    def on_item_click(self, instance):
        self.friend_name = instance.text
        self.friend_email = instance.secondary_text
        if self.new_chats:
            print(self.new_chats)
            data = pd.read_csv("user_data.csv")
            user_email = data["email"].iloc[0]
            token = data["idToken"].iloc[0]
            ids = [id for id in self.new_chats]
            print(ids)
            emails = [email["email"] for email in self.new_chats.values()]  
            print(ids, emails)

            if self.friend_email in emails:
                id = ids[emails.index(self.friend_email)]
                remove_new_chat(user_email, id, token)
            
        self.event = Clock.schedule_interval(self.load_messages, 2)
        self.root.get_screen('chat_screen').ids.chat_screen_top_name.title = self.friend_name
        self.root.current = "chat_screen"
        
    def on_menu_click(self):
        self.root.current = "home"
        if self.event:
            self.event.cancel()  # Stop the Clock event
        self.root.get_screen('chat_screen').ids.messages_box.clear_widgets()
        self.last_time[0] = "0"
        
    def on_dots_click(self):
        self.root.current = "Change_name"
        self.root.get_screen('Change_name').ids.friend_porfile_gmail.text = self.friend_email
        self.root.get_screen('Change_name').ids.friend_profile_name.text = self.friend_name
        
# ============================== Friend Profile ============================== 

    def delete_friend(self):
        self.error_dilogbox_delete_chats = MDDialog(
                title="Delete All chats",
                text=f"Are you sure you want to delete all chats with {self.friend_name}?",
                buttons=[MDFlatButton(text="Yes", on_release=self.delete_friend_chats_yes)]
            )
        self.error_dilogbox_delete_chats.open()
        
    def delete_friend_chats_yes(self, obj):
        self.error_dilogbox_delete_chats.dismiss(force=True)
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        delete = delete_friend_chats_yes_do(user_email, self.friend_email, token)
        self.last_time[0] = "0"
        self.root.get_screen('chat_screen').ids.messages_box.clear_widgets()
        if delete:
            self.error_dilogbox = MDDialog(
                title="Delete All chats",
                text=f"Your chat with {self.friend_name} has been successfully deleted.",
                buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()
        
        
    def back_friend_profile(self):
        self.root.current = "chat_screen"

# ============================== Start Settings ==============================

    def block_friend_dialog(self):
        self.error_dilogbox = MDDialog(
                title="Block Friend",
                text=f"Are you sure to block {self.friend_name}",
                buttons=[MDFlatButton(text="Yes", on_release=self.block_friend)]
            )
        self.error_dilogbox.open()

    def block_friend(self, obj):
        self.error_dilogbox.dismiss(Force=True)
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        block = block_user_friend(user_email, self.friend_email, self.friend_name, token)
        if block:
            show_friends(self)
            show_block_friends(self)

            self.root.current = "home"
            if self.event:
                self.event.cancel()  # Stop the Clock event
                self.root.get_screen('chat_screen').ids.messages_box.clear_widgets()
                self.last_time[0] = "0"
            self.error_dilogbox = MDDialog(
                title="Block Friend",
                text=f"{self.friend_name} is block in your chat list.",
                buttons=[MDFlatButton(text="ok", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()

        else:
            self.error_dilogbox = MDDialog(
                title="Block Friend",
                text=f"{self.friend_name} is not block in your chat list.",
                buttons=[MDFlatButton(text="ok", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()

        
            
# ============================= Profile Screen ============================

    def profile_btn(self):
        self.root.current = "profile"
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        name = data["name"].iloc[0]
        
        self.root.get_screen('profile').ids.profile_name.text = name
        self.root.get_screen('profile').ids.porfile_gmail.text = user_email
        
    def back_profile(self):
        self.root.current = "home"
        
        
        
        
# ============================== Load Message ==============================  
        
    def load_messages(self, obj):
        chat_screen = self.root.get_screen('chat_screen')
        messages_box = chat_screen.ids.messages_box

        # Load user email and token from CSV
        try:
            data = pd.read_csv("user_data.csv")
            self.user_email = data["email"].iloc[0]
            self.token = data["idToken"].iloc[0]
        except Exception as e:
            return

        # Fetch messages from Firebase
        try:
            messages = load_user_message(self.user_email, self.friend_email, self.token)
            for msg in messages.values():
                timestamp2 = msg.get("time", "Unknown Time")
        except Exception as e:
            return

        if not messages:
            return  # Exit function if there are no messages

        
        if self.last_time[0] != timestamp2 or self.last_time[0] == "0":
            messages_box.clear_widgets()
            # Loop through messages and add them to the UI
            for msg in messages.values():  # Iterate directly over dictionary values
                sender_email = msg.get("sender", "")
                message_text = msg.get("message", "")
                timestamp = msg.get("time", "Unknown Time")

            # Avoid adding duplicate messages
                is_sent_by_user = sender_email == self.user_email  # Check if the user sent the message
                sender_name = "You" if is_sent_by_user else self.friend_name  # Adjust sender name

                new_message = MessageBubble4(username=sender_name, text=message_text, timestamp=timestamp, is_sent_by_user=is_sent_by_user)
                messages_box.add_widget(new_message)
                
            self.last_time[0] = timestamp2

# ============================== Send Message ==============================

    def send_message(self):
        self.message = self.root.get_screen('chat_screen').ids.message_input.text
        try:
            data = pd.read_csv("user_data.csv")
            user_email = data["email"].iloc[0]
            token = data["idToken"].iloc[0]
            name = data["name"].iloc[0]

            # Create a single message object
            time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            message = {
                "message": self.message,
                "time": time,
                "sender": user_email  # Add sender information
            }

            # Send the message to the recipient
            send_user_message(user_email, self.friend_email, message, token)
            send_user_message(self.friend_email, user_email, message, token)
            add_new_chat(self.friend_email, user_email, name, self.message, token)
            SoundLoader.load("message_send_sound.mp3").play()

            # Clear the input field
            self.root.get_screen('chat_screen').ids.message_input.text = ""
        except Exception as e:
            self.error_dilogbox = MDDialog(
                title="Error",
                text=f"Failed to send message.",
                buttons=[MDFlatButton(text="OK", on_release=self.dilog_close)]
            )
            self.error_dilogbox.open()
    
    def get_start_btn(self):
        self.root.current = "email"
        
    def back_account(self):
        self.root.current = "email"
        
    def dilog_close(self, obj):
        self.error_dilogbox.dismiss(force=True)
        
    def next_account(self):
        self.user_name = self.root.get_screen('email').ids.name_text.text
        self.user_gmail = self.root.get_screen('email').ids.gmail_text.text
        self.user_change_gmail = self.user_gmail.replace(".", "-")
        self.user_password_1 = self.root.get_screen('email').ids.password_text_1.text
        self.user_password_2 = self.root.get_screen('email').ids.password_text_2.text
    
    
        if self.user_name == "" or self.user_gmail == "":
            self.error_dilogbox = MDDialog(
                title = "Error",
                text = "Please enter your name",
                buttons = [
                    MDFlatButton(text="OK", on_release=self.dilog_close)
                ])
            self.error_dilogbox.open()

        elif self.user_gmail == "" or self.user_gmail[-10:] != "@gmail.com" or self.user_gmail != self.user_gmail.lower():
            self.error_dilogbox = MDDialog(
                title = "Error",
                text = "Your E-mail is not Correct, please Check",
                buttons = [
                    MDFlatButton(text="OK", on_release=self.dilog_close)
                ])
            self.error_dilogbox.open()
            
        elif self.user_password_1 == "" or self.user_password_2 == "" or self.user_password_1 != self.user_password_2:
            self.error_dilogbox = MDDialog(
                title = "Error",
                text = "Your Password is not Correct, please Check",
                buttons = [
                    MDFlatButton(text="OK", on_release=self.dilog_close)
                ])
            self.error_dilogbox.open()
            
        else:
            user = sign_up(self.user_gmail, self.user_password_1, self.user_name)
            if user:
                self.root.get_screen('verification').ids.gmail_label.text = f"We have sent an activation link to {self.user_gmail}. Please check your inbox and verify your account before signing in."
                self.root.current = "verification"
            else:
                self.error_dilogbox = MDDialog(
                    title = "Error",
                    text = "This E-mail is already in use",
                    buttons = [
                        MDFlatButton(text="OK", on_release=self.dilog_close)
                    ])
                self.error_dilogbox.open()
                
# ============================== Activation account screen ==============================
    
    def have_account_btn(self):
        self.root.current = "account_2"
        
    def sign_in_next_btn(self):
        self.root.current = "account_2"
        
    def back_verification_2(self):
        self.root.current = "start_screen"

    def back_account_2(self):
        self.root.current = "start_screen"
    
    def account_2_next_btn(self):
        self.user_gmail = self.root.get_screen('account_2').ids.account_2_gmail_text.text
        self.user_password = self.root.get_screen('account_2').ids.account_2_password_text.text
        
        if self.user_gmail == "" or self.user_gmail[-10:] != "@gmail.com" or self.user_gmail != self.user_gmail.lower():
            self.error_dilogbox = MDDialog(
                title = "Error",
                text = "Your E-mail is not Correct, please Check",
                buttons = [
                    MDFlatButton(text="OK", on_release=self.dilog_close)
                ])
            self.error_dilogbox.open()
            
        elif self.user_password == "":
            self.error_dilogbox = MDDialog(
                title = "Error",
                text = "Your Password is not Correct, please Check",
                buttons = [
                    MDFlatButton(text="OK", on_release=self.dilog_close)
                ])
            self.error_dilogbox.open()
            
        else:
            try:
                user = sign_in(self.user_gmail, self.user_password)
                if user:
                    user_verif = user_is_verifiaction(user["idToken"])
                    if user_verif:
                        user_data = get_user_data(user["localId"], user["idToken"])
                        name = user_data["name"]
                        email = user_data["email"]
                        user_data = {
                            "name": [name],
                            "email": [email],
                            "localId": [user["localId"]],
                            "idToken": [user["idToken"]]
                        }
                        df = pd.DataFrame(user_data)
                        df.to_csv("user_data.csv", index=False)
                        
                        with open("password.txt", "w") as file:
                            file.write(self.user_password)
                        
                        show_friends(self)
                        show_block_friends(self)

                        self.root.current = "home"
                    else:
                        self.error_dilogbox = MDDialog(
                        title = "Error",
                        text = "Your E-mail is not verify. Please Verify your email.",
                        buttons = [
                            MDFlatButton(text="OK", on_release=self.dilog_close)
                        ])
                        self.error_dilogbox.open()
                else:
                    self.error_dilogbox = MDDialog(
                        title = "Error",
                        text = "Your E-mail or Password is not Correct, please Check",
                        buttons = [
                            MDFlatButton(text="OK", on_release=self.dilog_close)
                        ])
                    self.error_dilogbox.open()
            except:
                self.error_dilogbox = MDDialog(
                    title = "Error",
                    text = "Your E-mail or Password is not Correct, please Check",
                    buttons = [
                        MDFlatButton(text="OK", on_release=self.dilog_close)
                    ])
                
# ============================== Add Friend Screen ==============================

    def add_friend_btn(self):
        self.root.current = "add_friend"
        
    def back_add_friend(self):
        self.root.current = "home"
        
    def add_friend_save_btn(self):
        data = pd.read_csv("user_data.csv")
        user_email = data["email"].iloc[0]
        token = data["idToken"].iloc[0]
        user_name = data["name"].iloc[0]
        self.user_friend_email = self.root.get_screen('add_friend').ids.friend_gmail_text.text
        
        if self.user_friend_email == "" or self.user_friend_email != self.user_friend_email.lower():
            self.error_dilogbox = MDDialog(
                title = "Error",
                text = "Your Friend E-mail is not Correct, please Check",
                buttons = [
                    MDFlatButton(text="OK", on_release=self.dilog_close)
                ])
            self.error_dilogbox.open()
        else:
            try:
                friends = get_friends_in_chat(user_email, token)
                all_user = get_all_users(token)
                users_ids = [item for item in all_user]
                users_emails = [all_user[id]["email"] for id in users_ids]
                users_name = [all_user[id]["name"] for id in users_ids]
                for index, e in enumerate(users_emails):
                    if e == self.user_friend_email:
                        user_friend_name = users_name[index]
                        break
                else:
                    user_friend_name = "unKnow person"
            except:
                pass
            
            if friends:
                friends = [user["email"] for user in friends.values()]
            else:
                friends = ["No friends"]
                
            if all_user:
                all_user = [user["email"] for user in all_user.values()]
            else:
                all_user = ["No friends"]
                
            if self.user_friend_email in friends:
                self.error_dilogbox = MDDialog(
                    title = "Error",
                    text = "This friend is already in your chat",
                    buttons = [
                        MDFlatButton(text="OK", on_release=self.dilog_close)
                    ])
                self.error_dilogbox.open()
            elif self.user_friend_email not in all_user:
                self.error_dilogbox = MDDialog(
                    title = "Error",
                    text = "This friend is not in Blink Chat",
                    buttons = [
                        MDFlatButton(text="OK", on_release=self.dilog_close)
                    ])
                self.error_dilogbox.open()
            elif self.user_friend_email == user_email:
                self.error_dilogbox = MDDialog(
                    title = "Error",
                    text = "You can't add your self",
                    buttons = [
                        MDFlatButton(text="OK", on_release=self.dilog_close)
                    ])
                self.error_dilogbox.open()
            else:
                user_1 = add_friend_in_chat(user_friend_name, user_email, self.user_friend_email, token)
                user_2 = add_friend_in_chat(user_name, self.user_friend_email, user_email, token)
                if user_1 and user_2:
                    self.root.current = "home"
                    show_friends(self)
                    show_block_friends(self)


if __name__ == "__main__":
    MyApp().run()
