# -*- mode: python ; coding: utf-8 -*-
import os
import subprocess

block_cipher = None

a = Analysis(
    ['lanzador.py'],
    pathex=[],
    binaries=[],
    datas=[],
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
    name='Gestion mantenimiento golosinas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['iconom.ico'],
)

# ==============================================================================
# PROCESO DE FIRMA AUTOMÁTICA POST-COMPILACIÓN (.PFX)
# ==============================================================================

# Obtener rutas absolutas sin depender exclusivamente de constantes globales
spec_dir = os.path.dirname(os.path.abspath('lanzador.py')) if not 'SPECPATH' in locals() else SPECPATH
dist_dir = os.path.join(spec_dir, 'dist') if not 'DISTPATH' in locals() else DISTPATH

exe_generado = os.path.join(dist_dir, f'{exe.name}.exe')

NOMBRE_CERTIFICADO = 'Palmesano.pfx'
CERT_PATH = os.path.join(spec_dir, NOMBRE_CERTIFICADO)
CERT_PASS = 'TuClave123'  # Cambia por la contraseña real de tu archivo .pfx
TIMESTAMP_URL = 'http://timestamp.digicert.com'

signtool_cmd = [
    'signtool',
    'sign',
    '/f', CERT_PATH,
    '/p', CERT_PASS,
    '/tr', TIMESTAMP_URL,
    '/td', 'sha256',
    '/fd', 'sha256',
    exe_generado,
]

if os.path.exists(exe_generado):
    print('\n===================================================================')
    print(f'[+] Firmando ejecutable: {exe_generado}')
    if os.path.exists(CERT_PATH):
        try:
            # Capturamos la salida para ver exactamente lo que dice signtool si hay algún fallo
            res = subprocess.run(signtool_cmd, check=True, capture_output=True, text=True)
            print('[✔] Aplicación firmada exitosamente.')
            print(res.stdout)
        except subprocess.CalledProcessError as e:
            print(f'[✘] Error al firmar con signtool:\n{e.stderr}')
        except FileNotFoundError:
            print('[✘] Error: No se encontró "signtool.exe" en el PATH de Windows.')
    else:
        print(f'[✘] Error: No se encontró el archivo de certificado en: {CERT_PATH}')
    print('===================================================================\n')