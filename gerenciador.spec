# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Dados da aplicação
app_name = 'Gerenciador'
app_version = '1.0.0'
bundle_identifier = 'com.cucala.gerenciador'

# Configurações de análise
a = Analysis(
    ['gerenciador.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/*', 'assets'),   # Inclui os arquivos de assets
        ('data/*.json', 'data'),  # Inclui os arquivos de dados
    ],
    hiddenimports=[
        'pandas', 'openpyxl', 'customtkinter', 'PIL',
        'tkinter', 'queue', 'json', 'pathlib', 'configparser'
    ],
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

# Configurações do executável
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Desativa o console para aplicativo GUI
    disable_windowed_traceback=False,
    argv_emulation=True,  # Habilita o tratamento de eventos do macOS
    target_arch=None,     # None para arquitetura nativa
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.icns',  # Ícone correto para macOS
)

# Configurações do bundle para macOS
app = BUNDLE(
    exe,
    name=f'{app_name}.app',
    icon='assets/icon.icns',
    bundle_identifier=bundle_identifier,
    version=app_version,
    info_plist={
        'CFBundleName': app_name,
        'CFBundleDisplayName': app_name,
        'CFBundleVersion': app_version,
        'CFBundleShortVersionString': app_version,
        'NSHighResolutionCapable': 'True',
        'NSRequiresAquaSystemAppearance': 'False',
        'LSMinimumSystemVersion': '10.15.0',
    },
)

# Configurações de coleta
coll = COLLECT(
    app,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Gerenciador',
    info_plist='InfoGerenciador.plist',
)

# Configurações adicionais para macOS
app.coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Gerenciador',
)

app.console = False
app.iconfile = 'assets/icon.icns'
