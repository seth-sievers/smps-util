# smps-util
A simple GUI utility for quickly and efficiently iterating on SMPS designs. 

**NOT WORKING YET, STILL WIP**

## Directory Structure 
- src/ 
  * Contains Python Source Code 

## Versions: 
- Python 3.13.5

## Temp
```
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
pyinstaller --noconfirm --clean --noconsole --onefile --distpath ../dist --workpath ../build --specpath ../build --name test.exe main.py
```