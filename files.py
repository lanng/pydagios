import os
import shutil

# Declarando o caminho da pasta para o script enviar os PDFs gerados.
ESTRELA = r"C:\Users\Victor\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\ESTRELA"
TERUO = r"C:\Users\Victor\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\TERUO"
MARANI = r"C:\Users\Victor\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\MARANI"
FORTI = r"C:\Users\Victor\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\FORTI"
ERROR = "ERRO AO MOVER O ARQUIVO!"

pasta = ".\PDFs"

# Verifica se a pasta contem arquvios, se não, sai do script
if len(os.listdir(pasta)) == 0:
    print("Nenhum arquivo encontrado")
    exit()

print("Gerando PDFs...")

for files in os.walk(pasta):
    for file in files[2]:
        source = os.path.join(pasta, file)
        if file[0] == 'T':
            try:
                shutil.move(source, TERUO)
            except:
                print(ERROR)
        elif file[0] == 'E':
            try:
                shutil.move(source, ESTRELA)
            except:
                print(ERROR)
        elif file[0] == 'M':
            try:
                shutil.move(source, MARANI)
            except:
                print(shutil.Error.message)
                print(ERROR)
        elif file[0] == 'F':
            try:
                shutil.move(source, FORTI)
            except:
                print(ERROR)
        else:
            print("Arquivo com nome incorreto: ")
            print(file)
