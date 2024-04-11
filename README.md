# Pydagios

This repository contains a code solution for automating the generation of tolls receipts in the form of PDF documents. The code captures screenshots of a specific area on the screen, extracts the toll values using OCR (Optical Character Recognition), and generates PDF files for each receipt.

The scripts take screenshots of a mobile phone witch have be in your screen, I personly recommend the [`scrcpy`](https://github.com/Genymobile/scrcpy) to controll the smarthphone on computer and take the screenshots.

## Features

- Captures screenshots of a designated area on the screen to extract toll values.
- Utilizes OCR to extract toll values from the captured screenshots.
- Calculates the total sum of toll values.
- Generates a PDF file for each receipt, including the service order number and total value.
- Allows for easy distribution and storage of tolls receipts.

## Prerequisites

Make sure you have the following dependencies installed:

- Python (version 3.10^)
- PyAutoGUI library (for capturing screenshots)
- Pillow library (for image manipulation)
- OpenCV library (for image processing)
- Google Cloud Vision API (for OCR)
- ReportLab library (for PDF generation)
- EasyGUI library (for user interaction)
- shutil module (for file moving)

You can install the required libraries using pip:

```
pip install -r requirements.txt
```

## Usage

1. Clone this repository to your local machine:

```
git clone git@github.com:lanng/pydagios.git
```

2. Install the required dependencies as mentioned above.

3. Navigate to the project directory:

```
cd pydagios
```

4. Create the .env file to suit your requirements of directories

5. Run the `main.py` file:

```
python main.py
```

6. Follow the prompts in the GUI window to enter the service order number and capture toll receipts.

7. Press the `Insert` to capture each file and `End` key to stop capturing screenshots and generate the PDF.

8. The generated PDF files will be saved in the respective directories based on the first character of the file name.

9. After generating the PDFs, move the PDF files for a directory `PDFs` and on GUI click 'yes' to to move the generated files to the appropriate directories you set on .env.

## Configuration

- `main.py`: Modify the `TOP`, `LEFT`, `WIDTH`, and `HEIGHT` variables to adjust the capture area on the screen, if you need.
- `Calculator.py`: Adjust the OCR extraction parameters and customize the extraction logic if required.
- `files.py`: Set the appropriate directory paths for moving the generated PDF files with env file or directly on it.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Disclaimer

Please note that this software is provided as-is, without any warranty. Use it at your own risk.<br> 
Use Google Cloud SDK Shell to configure credentials for Google Cloud Vision. More information can be found at: [`Google Auth Doc`](https://cloud.google.com/vision/docs/authentication).

---

This README provides a brief overview of the Tolls PDF Generator. For detailed instructions and usage examples, refer to the project's documentation or the source code itself.
