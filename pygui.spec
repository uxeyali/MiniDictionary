# -*- mode: python -*-

block_cipher = None


a = Analysis(['pygui.py'],
             pathex=['/Users/wi5483pi/Dropbox/WSU/Software Engineering/PycharmProjects/MiniDictionary'],
             binaries=[],
             datas=[('Dictionary.csv', '.')],
             hiddenimports=['pandas._libs.tslibs.np_datetime'],
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
          name='pygui',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
