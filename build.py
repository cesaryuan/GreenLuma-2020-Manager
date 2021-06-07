import PyInstaller.__main__
import site

sitepath = site.getsitepackages()[1]
PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--noconsole',
    '--name', "GreenLuma2020Manager",
    '--icon', 'icon.ico',
    '--add-data', f'{sitepath}\cloudscraper;cloudscraper'
])
