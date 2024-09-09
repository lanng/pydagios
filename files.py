import os
import shutil


class Files:
    ESTRELA = r"C:\Users\victo\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\ESTRELA"
    TERUO = r"C:\Users\victo\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\TERUO"
    MARANI = r"C:\Users\victo\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\MARANI"
    FORTI = r"C:\Users\victo\OneDrive\Documentos\AUTO SOCORRO\PEDAGIOS\FORTI"
    ERROR = "ERRO AO MOVER O ARQUIVO!"
    PDFS_DIRECTORY = ".\PDFs"

    @staticmethod
    def move_pdf_files():
        # Create the destination directory if it doesn't exist
        os.makedirs(Files.PDFS_DIRECTORY, exist_ok=True)

        print("Moving PDF files...")

        for file in os.listdir():
            if file.lower().endswith(".pdf"):
                source = os.path.join(os.getcwd(), file)
                destination = os.path.join(
                    os.getcwd(), Files.PDFS_DIRECTORY, file)

                try:
                    shutil.move(source, destination)
                    print(f"File moved: {file}")
                except Exception as e:
                    print(f"Error moving file: {file}")
                    print(f"Error: {str(e)}")

    @staticmethod
    def move_files():
        # Call method to move the pdf files to the "/PDFs"
        Files.move_pdf_files()
        path = Files.PDFS_DIRECTORY

        # Verifica se a pasta contem arquivos; se não, sai do script
        if len(os.listdir(path)) == 0:
            print("Nenhum arquivo encontrado")
            return

        print("Gerando PDFs...")

        for files in os.walk(path):
            for file in files[2]:
                source = os.path.join(path, file)
                if file[0].upper() == 'T':
                    try:
                        shutil.move(source, Files.TERUO)
                    except:
                        print(Files.ERROR)
                elif file[0].upper() == 'E':
                    try:
                        shutil.move(source, Files.ESTRELA)
                    except:
                        print(Files.ERROR)
                elif file[0].upper() == 'M':
                    try:
                        shutil.move(source, Files.MARANI)
                    except:
                        print(Files.ERROR)
                elif file[0].upper() == 'F':
                    try:
                        shutil.move(source, Files.FORTI)
                    except:
                        print(Files.ERROR)
                else:
                    print("Arquivo com nome incorreto: ")
                    print(file)

    @staticmethod
    def exclude_png_files():
        print("Excluding PNG files...")

        for file in os.listdir():
            if file.lower().endswith(".png"):
                path = os.path.join(os.getcwd(), file)

                try:
                    os.remove(path)
                    print(f"File deleted: {file}")
                except Exception as e:
                    print(f"Error deleting file: {file}")
                    print(f"Error: {str(e)}")
