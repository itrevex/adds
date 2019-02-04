REM py -3.7-64 -m pip install py2exe
rem py -3.7-64 -m pip install pyinstaller
REM py -3.7-64 -m pip install --upgrade pip
REM py -3.7-64 setup.py install
REM py -3.7-64 setup.py py2exe
REM py -3.7-64 -m pip install PyInstaller
REM py -3.7-64 -m pip install docopt
REM py -3.7-64 -m pip install dxfwrite
REM py -3.7-64 -m pypi main.spec
REM py -3.7-64 hello.py
REM py -3.7-64 -c "import site; print(site.getsitepackages())"
REM py -3.7-64 -m PyInstaller main.spec
REM py -3.7-64 main.py 
py -3.7-64 main.py "input/input_data.json"

