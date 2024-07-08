from PIL import Image
import os

def main(width,height,plase):
    tree = list(os.walk(plase))
    per1=width
    per2=height
    # запись изменённых файлов
    # recording changed files
    if len(tree) != 1:
        os.mkdir(f'correktIMG\\{(plase.split("/"))[-1]}')
        for i in range(len(tree) - 1):
            os.mkdir(f'correktIMG\\{(plase.split("/"))[-1]}\\{(tree[i + 1][0]).split("\\")[1]}')
        for i in range(len(tree)):
            for x in range(len(tree[i][2])):
                if len(tree[i][2]) != 0 and i != 0 and tree[i][2][x] == 'Thumbs.db':
                    if x != 0:
                        tree[i][2].pop(x)
                    else:
                        tree[i][2].pop(x)
                        break
            for x in tree[i][2]:
                print(tree[i][0] + '/' + x)
                img = Image.open(tree[i][0] + '/' + x)
                print(img)
                # ширина,  высота
                # width,   height
                img = img.resize((int(per1), int(per2)))
                if x[-4:] == ".PNG":
                    img.save(f'correktIMG\\{(plase.split("/"))[-1]}\\{(tree[i][0]).split("\\")[1]}\\{x}')

                else:
                    img.save(f'correktIMG\\{(plase.split("/"))[-1]}\\{(tree[i][0]).split("\\")[1]}\\{x[:x.find(".")]}.PNG')
    return True