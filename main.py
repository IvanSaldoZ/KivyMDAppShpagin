from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.icon_definitions import md_icons

from kivymd.uix.menu import MDDropdownMenu

from kivymd.font_definitions import fonts

KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1
                        
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)      
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1       
                        
                        
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Input"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"   
                                
                                BoxLayout:
                                    orientation: 'horizontal'                               
                                    
                                    MDIconButton:
                                        icon: "calendar-month"
                                        
                                    MDTextField:
                                        id: start_date
                                        hint_text: "Start date"
                                        on_focus: if self.focus: app.date_dialog.open()
                                
                                BoxLayout:
                                    orientation: 'horizontal'                         
                                    
                                    MDIconButton:
                                        icon: "cash"
                                        
                                    MDTextField:
                                        id: loan
                                        hint_text: "Loan"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                
                                    
                                    MDIconButton:
                                        icon: "clock-time-five-outline"
                                            
                                    MDTextField:
                                        id: months
                                        hint_text: "Months"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                 
                                    
                                    MDIconButton:
                                        icon: "bank"
                                            
                                    MDTextField:
                                        id: interest
                                        hint_text: "Interest, %"
                                    
                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        on_focus: if self.focus: app.menu.open()
                                
                                MDSeparator:
                                    height: "1dp"
                                    
                                
                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'
                                
                                        MDRectangleFlatIconButton:
                                            icon: "android"
                                            text: "BUTTON1"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0, 0, 0, 1
                                            icon_color: 1, 0, 0, 1
                                            md_bg_color: 0.1, 0.1, 0.1, 1
                                            adaptive_width: True
                                            on_release: app.calc_table(*args)
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'
                                    
                                        MDRectangleFlatIconButton:
                                            icon: "android"
                                            text: "BUTTON2"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0, 0, 0, 1
                                            icon_color: 1, 0, 0, 1
                                            md_bg_color: 0.1, 0.1, 0.1, 1
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'
                                        
                                        Button:
                                            text: "Test Ok"
                                            size_hint_y: .5
                                            background_color: (0.1, 0.1, 0.1, 1.0)
                                                                           
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"
                            

                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"
                        
                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"
                        
                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class MortgageCalculatorApp(MDApp):
    """
    Основной класс приложения
    """

    # Переменные, которые можно использовать в KV через вызов "app."
    # (например, app.title, app.by_who и т.д.
    title = "Mortgage Calculator"
    by_who = 'by Ivan Saldikov'

    def build(self):
        """
        Метод при билде приложения
        :return:
        """
        return Builder.load_string(KV)

    def on_start(self):
        """
        Метод при создании приложения
        :return:
        """
        # Иконки слева
        icons_item_menu_lines = {
            "account-cowboy-hat": "About author",
            "youtube": "My YouTube",
            "coffee": "Donate author",
            "github": "Source code",
            "share-variant": "Share app",  #air-horn
            "shield-sun": "Dark/Light",
        }
        # Иконки закладок
        icons_item_menu_tabs = {
            "calculator-variant": "Input",  #ab-testing
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",  # chart-arc
            "book-open-variant": "Sum",
        }
        # Левое меню
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # Закладки в центре можно формировать программным образом, а не через KV-файла
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #     self.root.ids.tabs.add_widget(
        #         Tab(text=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref] {name_tab}")
        #     )

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print('Tab clicked!!!', tab_text)

    def on_star_click(self):
        """
        При нажатии на звёздочку сверху справа
        :return:
        """
        print("star clicked!")


class Tab(MDFloatLayout, MDTabsBase):
    """
    Список закладок (tabs)
    https://kivymd.readthedocs.io/en/latest/components/tabs/
    """
    pass


MortgageCalculatorApp().run()