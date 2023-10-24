import os
import json


def updateAutoSave():
    if os.path.exists(
        os.path.expanduser("~")
        + "/.jupyter/lab/user-settings/@jupyterlab/docmanager-extension"
    ):
        with open(
            os.path.expanduser("~")
            + "/.jupyter/lab/user-settings/@jupyterlab/docmanager-extension/plugin.jupyterlab-settings",
            "w+",
        ) as f:
            json.dump({"autosaveInterval": 5}, f)


updateAutoSave()
print("Python Is Set")
