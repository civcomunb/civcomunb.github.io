# -*- mode: python -*-

block_cipher = None


a = Analysis(['T10_GUI.py'],
             pathex=['C:\\Users\\Mario Raul Freitas\\Dropbox\\Universidade\\CivCom\\Curso-Python-basico\\Apresentação\\Dia 3\\Código'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='T10_GUI',
          debug=False,
          strip=False,
          upx=True,
          console=True )
