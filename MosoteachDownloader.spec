# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['MosoteachDownloader.py'],
             pathex=['/Users/hlf/Documents/Language/Python/MosoteachDownloader'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MosoteachDownloader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='104-2101151J3550-L.icns')
app = BUNDLE(exe,
             name='MosoteachDownloader.app',
             icon='104-2101151J3550-L.icns',
             bundle_identifier=None)
