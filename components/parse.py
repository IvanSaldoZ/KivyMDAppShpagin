import time

from bs4 import BeautifulSoup
import requests
import os

components_list_file_name = "components_list.html"
components_folder = 'parsed_components'
imgs_folder = 'parsed_imgs'

if not os.path.isfile(components_list_file_name):
    page = requests.get('https://kivymd.readthedocs.io/en/latest/components/')
    with open(components_list_file_name, "w", encoding="UTF-8") as f:
        f.writelines(page.text)
else:
    with open(components_list_file_name, "r") as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'html.parser')
        class_name = 'toctree-l1'
        a_class = 'reference internal'
        # ans = soup.find_all('div', attrs={'class'='toctree-wrapper compound'})
        ans = soup.find_all('a', attrs={"class": "reference internal"})
        i = 1
        for a in ans:
            link_url = a["href"]
            link_text = a.text
            if not '..' in link_url:
                print(f'{link_text}')
                # Теперь заходим в каждый компонент и ищем там картинки
                component_file_name = link_text + '.html'
                goto = f'https://kivymd.readthedocs.io/en/latest/components/{link_url}'
                print(goto)
                if not os.path.isfile(os.path.join(components_folder, component_file_name)):
                    page = requests.get(goto)
                    with open(os.path.join(components_folder, component_file_name), "w", encoding="UTF-8") as f_c:
                        contents = page.text
                        f_c.writelines(contents)
                else:
                    with open(os.path.join(components_folder, component_file_name), "r", encoding="UTF-8") as f:
                        contents = f.read()
                soup = BeautifulSoup(contents, 'html.parser')
                main_content = soup.select('img', attrs={'class': 'align-center'})
                if len(main_content) > 1:
                    imgs = main_content[1:]
                    for img in imgs:
                        src = img['src']
                        i += 1
                        print(i, src)
                        if str(src).endswith('.gif'):
                            folder_name_to_save = 'gif'
                        else:
                            folder_name_to_save = 'png'
                        full_folder_path = os.path.join(imgs_folder, folder_name_to_save, link_text)
                        if not os.path.isdir(full_folder_path):
                            os.mkdir(full_folder_path)
                        # Имя файла из URL-а
                        img_file_name = src.split('/')[-1]
                        img_full_file_path = os.path.join(full_folder_path, img_file_name)
                        # Если ещё не загружен файл:
                        if not os.path.isfile(img_full_file_path):
                            # Сохраняем картинку в нужную папку
                            image = requests.get(src)
                            image_content = image.content
                            with open(img_full_file_path, 'wb') as img_f:
                                img_f.write(image_content)
                            time.sleep(5)




        # ans = soup.select('div')
        # print(ans)
        # print(soup.head)
        # print(soup.li)
