from PIL import Image
import os


def main(width, height, plase):
    tree = list(os.walk(plase))
    # запись изменённых файлов
    # recording changed files
    for i in tree:
        if i[1]:
            os.mkdir(f'correktIMG\\{(plase.split("/"))[-1]}')
            for x in i[1]:
                os.mkdir(f'correktIMG\\{(plase.split("/"))[-1]}\\{x}')
        if i[2]:
            for x in i[2]:
                if x != "Thumbs.db":
                    img = Image.open(i[0] + '\\' + x)
                    img = img.resize((int(width), int(height)))
                    if x[-4:] == ".PNG":
                        img.save(f'correktIMG\\{(i[0].split("/"))[-1]}\\{x}')
                    else:
                        img.save(f'correktIMG\\{(i[0].split("/"))[-1]}\\{x[:x.find(".")]}.PNG')
    return True
