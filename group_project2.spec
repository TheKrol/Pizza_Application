added_files = [
	('C:/Users/krol5/Downloads/School/CSC_4110/group_project2/assests/*.png', 'assests' ),
	('C:/Users/krol5/Downloads/School/CSC_4110/group_project2/logs/Inventory.json', 'logs'),
	('C:/Users/krol5/Downloads/School/CSC_4110/group_project2/logs/employees.txt', 'logs')
    ]
block_cipher = None
a = Analysis(['group_project2.py'],
         pathex=['C:/Users/krol5/Downloads/School/CSC_4110/group_project2'],
         binaries=None,
         datas=added_files,
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None,
         excludes=None,
         cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      [],
      name='Group_Project2',
      debug=True,
      bootloader_ignore_signals=False,
      strip=False,
      upx=True,
      upx_exclude=[],
      runtime_tmpdir=None,
      console=True )
coll = COLLECT(exe)