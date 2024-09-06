# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\kevin\\OneDrive\\Área de Trabalho\\Programas\\Cad_Diaristas_Django\\cad_diaristas1.1\\cad_diaristas\\cad_diaristas\\static', 'static'), ('C:\\Users\\kevin\\OneDrive\\Área de Trabalho\\Programas\\Cad_Diaristas_Django\\cad_diaristas1.1\\cad_diaristas\\cad_diaristas\\app_cad_diarista\\templates', 'templates')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='manage',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
