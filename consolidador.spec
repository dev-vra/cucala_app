# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['consolidador.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/*', 'assets'),   # Inclui os arquivos de assets
        ('data/*.json', 'data'),  # Inclui os arquivos de dados
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Consolidador',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon='assets/icon.icns'  # Ícone correto para macOS
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Consolidador'
)
