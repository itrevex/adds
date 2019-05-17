REM py -3.7-64 -m pip install py2exe 
rem py -3.7-64 -m pip install pyinstaller
REM py -3.7-64 -m pip install --upgrade pip
REM py -3.7-64 setup.py install
REM py -3.7-64 setup.py py2exe
REM py -3.7-64 -m pip install PyInstaller
REM py -3.7-64 -m pip install docopt
REM py -3.7-64 -m pip install dxfwrite
REM py -3.7-64 -m pip install -U pytest
REM py -3.7-64 -m pip install coverage
REM py -3.7-64 -m pip install pytest-cov
REM py -3.7-64 -m pip install pylint --upgrade
REM py -3.7-64 -m pypi main.spec
REM py -3.7-64 hello.py
REM py -3.7-64 -c "import site; print(site.getsitepackages())"
REM py -3.7-64 -m PyInstaller src/main.py
REM py -3.7-64 -m PyInstaller main.spec
REM py -3.7-64 main.py 
REM git rm --cached *.dxf
REM "dist/main/main" input/philip.trad
REM iscc "setup/adds.iss"
REM "setup/setups/adds_setup-1.0.3"
py -3.7-64 src/main.py "../input/philip.trad"
REM py -3.7-64 todo.py

