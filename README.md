# KivyMD Application Shpagin

Это мобильное приложение на основе фреймворка KivyMD и видео-уроков Шпагина:
https://www.youtube.com/watch?v=IJSdFYcm8EA

### Начало работы с фреймворком:
https://kivymd.readthedocs.io/en/latest/getting-started/#

Установка фреймворка:
`pip install kivymd`

### Автокомпиляция APK:
https://www.youtube.com/watch?v=fmkX_3ynHsc&t=51s
Добавляем buildozer.spec, buildozer-32bit.spec 
и buildozer-64bit.spec 


### Дизайн приложения:
https://www.youtube.com/watch?v=M9zDe7--VJE

Навигационное меню слева:
https://kivymd.readthedocs.io/en/latest/components/navigation-drawer/

Там есть ошибка, поэтому нужно использовать код здесь, заменив 
https://github.com/kivymd/KivyMD/issues/796


```
NavigationLayout
```
на
```
MDNavigationLayout
```
и
```
left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
```
на
```
left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
```

Сам KV - это описание как раз элементов на макете приложения:
https://kivy.org/doc/stable/guide/lang.html


Преобразование цветов в HEX в KV-файле:
https://stackoverflow.com/questions/22932242/convert-rgba-color-codes-255-255-255-255-to-kivy-color-codes-in-1-1-1-1


Хорошие иконки есть тут:
https://fonts.google.com/icons?selected=Material+Icons

Парсер картинок всех компонентов:
Папка /components

### Считывание переменных из приложения
https://www.youtube.com/watch?v=KLcHMJETg4A
В KV-файле пишем "app.", + в основном классе приложения можно писать переменные,
например "app.title", class MainApp(MDApp): ... title = 'Something'


### Kivy Designer Pattern

Тот паттерн, который я использовал для дизайна на сайте KivyDesigner, хранится 
в файле `kivy_designer_pattern.py`
                
