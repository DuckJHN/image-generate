<h1 align="center" id="title"> 📷 Image generator</h1>

Tool generate mutil image from image input

## 🧐 Features

Here're some of the project's best features:

- Resize
- Noise
- Blur
- Rotate
- Flip (horizontal vertical)
- Brightness - contrast
- Modify Exif(inprocess)
- Convert or compress image(inprocess)

## 🚀Environment Variables

To run this project, you will need to add env python in this project use python version
`Python 3.11`

👍 You can use a lower version, but I recommend using version 3.8 or higher

## 🛠️ Installation

Install library necessary
In this project using opencv-python for process image

#### Python 2

```bash
    pip install -r requirements.txt
```

#### Python 3

```bash
    pip3 install -r requirements.txt
```

## ⭐ Run Locally

Clone the project

```bash
    git clone https://github.com/MaxiRadomski/picturegenerator.git
```

Go to the project directory

```bash
    cd picturegenerator
```

Install library

```bash
    pip install -r requirements.txt
```

Run command line interface(CLI) help

#### Python 2

```bash
    py app.py --help
```

#### Python 3

```bash
    python3 app.py --help
```

#### Example

```bash
    py app.py --folder_path images --output_path output --limit 30 --flip-horizontal --noise 10 20 --resize 80 90 --rotation 0 30 --brightness 20 30 --constrast 50 80 --blur gaussian --kn 3 --crop 80 --color
```
