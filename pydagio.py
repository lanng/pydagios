import keyboard
import os
import pyautogui as auto
import easygui as eg
from PIL import Image

# Dimesões da area do print
TOP = 765
LEFT = 300
WIDTH = 390
HEIGHT = 600
reply = ""

while reply != "Nao":
    imageList = []
    auto.PAUSE = 2
    service_order = eg.enterbox(
        'Informe o número do serviço e o identificador:')

    counter = 0
    while keyboard.is_pressed('end') == False:
        if keyboard.is_pressed('insert'):
            im = auto.screenshot(region=(TOP, LEFT, WIDTH, HEIGHT))
            counter = counter + 1
            im.save(f'ped{counter}.png')
            auto.alert(f'IMAGEM SALVA - {counter}')

    auto.alert(f'Preparando os Docs - Quantidade de pedagios: {counter}')

    for i in range(1, counter + 1):
        im = Image.open(f'ped{i}.png')
        im = im.convert('L')
        imageList.append(im)

    # colocando as imagens armazenadas no pdf, retirando o prieiro elemento para não se repetir
    imageList[0].save(f'{service_order}.pdf', save_all=True,
                      resolution=140, append_images=imageList[1:])
    auto.alert('PDF gerado com sucesso')
    reply = eg.buttonbox(msg='Deseja gerar outro PDF?', choices=('Sim', 'Nao'))

auto.alert('Gerador de PDF finalizado - Movendo arquivos...')
os.system('python files.py')
