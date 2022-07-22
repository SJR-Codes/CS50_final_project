"""
* CS50P Problem Set 1
* File Extensions
* by Samu Reinikainen 22.07.2022
"""


fname = input("Enter file name: ").strip().lower()
img_exts = ["gif", "png"]
jpg_exts = ["jpg", "jpeg"]
app_exts = ["pdf", "zip"]
app_txts = ["txt"]


if "." in fname:
    ext = fname.split(".")
    ext = ext[-1]

    if ext in img_exts:
        print("image/" + ext)
    elif ext in jpg_exts:
        print("image/jpeg")
    elif ext in app_exts:
        print("application/" + ext)
    elif ext in app_txts:
        print("text/plain")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
