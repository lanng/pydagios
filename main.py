import keyboard
import os
import pyautogui as auto
import easygui as eg
import shutil
from PIL import Image
from Calculator import Calculator
from Files import Files

# Dimesões da area do print
TOP = 765
LEFT = 300
WIDTH = 390
HEIGHT = 600
reply = ""
value_text = ""
values = []

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

    values.clear()
    for i in range(1, counter + 1):
        im = Image.open(f'ped{i}.png')
        im = im.convert('L')
        imageList.append(im)
        values.append(Calculator.extract_value(f'ped{i}.png'))

    value_text = Calculator.sum_values(values)

    # colocando as imagens armazenadas no pdf, retirando o prieiro elemento para não se repetir
    imageList[0].save(f'{service_order} - R$ {value_text}.pdf', save_all=True,
                      resolution=140, append_images=imageList[1:])
    auto.alert('PDF gerado com sucesso - R$ ' + str(value_text))
    reply = eg.buttonbox(msg='Deseja gerar outro PDF?', choices=('Sim', 'Nao'))


auto.alert('Gerador de PDF finalizado - Movendo arquivos...')
Files.move_files()
# exclude png files for clean directory at the end.
Files.exclude_png_files()
