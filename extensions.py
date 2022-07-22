"""
* CS50P Problem Set 1
* File Extensions
* by Samu Reinikainen 22.07.2022
"""


fname = input("Enter file name: ").strip().lower()
img_exts = ["gif", "jpg", "jpeg", "png"]
app_exts = ["pdf", "zip"]
app_txts = ["txt"]


if "." in fname:
    ext = fname.split(".")

    if ext[-1] in img_exts:
        print("image/" + ext[1])
    elif ext[-1] in app_exts:
        print("application/" + ext[1])
    elif ext[-1] in app_txts:
        print("text/plain")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
