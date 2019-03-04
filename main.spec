# -*- mode: python -*-

block_cipher = None

allFiles = [
    ('./assests/', 'assests'),
    ('./input/', 'input'),
    ( './read_me.pdf/', '.' ),
    ( './release_update.pdf/', '.' ),
    ( './run.bat/', '.' ),
    ( 'C:\\Users\\treve\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\ezdxf\\templates', 'ezdxf/templates' ),
    ]

a = Analysis(['main.py'],
             pathex=['E:\\Projects\\ESAI\\PROGRAMMING\\PYTHON\\adds'],
             binaries=[],
             datas=allFiles,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='setup/icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
