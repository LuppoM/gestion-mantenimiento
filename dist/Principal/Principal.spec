# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

datas_pptx = collect_data_files('pptx')
datas_matplotlib = collect_data_files('matplotlib')
datas_babel = collect_data_files('babel')  # <--- Agregamos los datos de babel

datas_totales = [
    ('fondo.jpg', '.'),
    ('iconom.ico', '.'),
] + datas_pptx + datas_matplotlib + datas_babel

hidden_pptx = collect_submodules('pptx')

a = Analysis(
    ['Principal.py'],
    pathex=['.'],
    binaries=[],
    datas=datas_totales,
    hiddenimports=[
        'tkcalendar',
        'babel.numbers',  # <--- Asegura la importación de babel
        'win32timezone',
        'reportlab',
        'reportlab.pdfgen.canvas',
        'reportlab.lib.pagesizes',
        'reportlab.lib.colors',
        'matplotlib',
        'matplotlib.backends.backend_tkagg',
    ] + hidden_pptx,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['notebook', 'scipy', 'IPython'],  # <--- Sin excluir babel.locale-data
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Principal',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='iconom.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='Principal'
)