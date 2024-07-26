import zipfile
import os
import urllib.request
import shutil
from time import sleep

print("Five nuker is being updated please wait...")
os.system("title Five nuker is being updated please wait...")

print("Closing the nuker process...")
os.system('taskkill /f /im Five-nuker.exe')

sleep(2)

print("Deleting the old version...")
try:
    os.remove("Five-nuker.exe")
    shutil.rmtree("_five-nuker-contents-dir")
except Exception as joker_eshkere_medniy_bik_42_BRATYXAAAAAAAAA_52_sank_piter_pyk_xixi_pyk:   # с таким эщкере кодом пойду работать в гугл - G1itch
    print(f"FAIL! {joker_eshkere_medniy_bik_42_BRATYXAAAAAAAAA_52_sank_piter_pyk_xixi_pyk}")
    pass

print("Downloading release.zip...")
urllib.request.urlretrieve("https://github.com/glitch65/Five-nuker/raw/Rework/release.zip", "release.zip")


try:
    with zipfile.ZipFile("release.zip", "r") as release:
        release.extractall()
except Exception as e:
    print(f"FAIL! {e}")
    pass

print("Deleting release.zip...")
try:
    os.remove("release.zip")
except Exception as e:
    print(f"FAIL! {e}")
    pass
print("Deleting updater.zip")
try:
    os.remove("updater.zip")
except Exception as e:
    print(f"FAIL! {e}")
    pass

print("Starting Five nuker...")
os.system("Five-nuker.exe")