import os
import shutil
import logging
from dotenv import load_dotenv


class Files:
    load_dotenv()
    DESTINATIONS = {
        "E": os.getenv("ESTRELA_DIR", r"./PDFs"),
        "M": os.getenv("MARANI_DIR", r"./PDFs"),
        "T": os.getenv("TERUO_DIR", r"./PDFs"),
        "F": os.getenv("FORTI_DIR", r"./PDFs"),
    }

    PDFS_DIRECTORY = os.getenv("PDFS_DIR", ".\PDFs") 
    ERROR_MESSAGE = "ERRO AO MOVER O ARQUIVO: {file}"

    @staticmethod
    def setup_logger():
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    @staticmethod
    def move_pdf_files():
        # Create the destination directory if it doesn't exist
        os.makedirs(Files.PDFS_DIRECTORY, exist_ok=True)
        logging.info("moving PDF files to %s", Files.PDFS_DIRECTORY)

        for file in os.listdir():
            if file.lower().endswith(".pdf"):
                source = os.path.join(os.getcwd(), file)
                destination = os.path.join(
                    os.getcwd(), Files.PDFS_DIRECTORY, file)

                try:
                    shutil.move(source, destination)
                    logging.info("File moved %s", file)
                except Exception as e:
                    logging.error(Files.ERROR_MESSAGE.format(file=file))
                    logging.error("Errors details: %s", str(e))

    @staticmethod
    def move_files():
        # Call method to move the pdf files to the "/PDFs"
        Files.move_pdf_files()
        pdf_path = Files.PDFS_DIRECTORY

        # Verifica se a pasta contem arquivos; se não, sai do script
        if not os.listdir(pdf_path):
            logging.info("No files found in %s", pdf_path)
            return

        logging.info("Processing files in %s", pdf_path)

        for root, _, files in os.walk(pdf_path):
            for file in files:
                source = os.path.join(root, file)
                prefix = file[0].upper()
                
                #debug .env errors
                logging.info("estrela: %s", Files.DESTINATIONS.get("E"))


                destination_dir = Files.DESTINATIONS.get(prefix)
                if destination_dir:
                    try:
                        os.makedirs(destination_dir, exist_ok=True)
                        shutil.move(source, destination_dir)
                        logging.info("Moved %s to %s", file, destination_dir)
                    except Exception as e:
                        logging.error(Files.ERROR_MESSAGE.format(file=file))
                        logging.error("Error details: %s", str(e))
                else:
                    logging.warning("File has an incorrect name or no matching directory: %s", file)

    @staticmethod
    def exclude_png_files():
        logging.info("Deleting PNG files...")

        for file in os.listdir():
            if file.lower().endswith(".png"):
                path = os.path.join(os.getcwd(), file)

                try:
                    os.remove(path)
                    logging.info("File deleted: %s", file)
                except Exception as e:
                    logging.error("Error deleting file: %s", file)
                    logging.error("Error details: %s", file)


Files.setup_logger()