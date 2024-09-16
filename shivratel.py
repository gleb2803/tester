import base64
import json
from idlelib.browser import file_open
from shutil import which


def shifr(in_file,out_file):

    with open(file=in_file,mode="r",encoding="UTF-8") as f:

        data = json.load(f)



    data = base64.b64encode(str(data).encode("utf-8"))

    with open(file=out_file,mode="w") as f:
        f.write(str(data))


if __name__ == "__main__":
    shifr("time.json","test.dat")