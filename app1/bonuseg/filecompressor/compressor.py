import PySimpleGUI as sg 
from zipcreator import make_Archive

label1 = sg.Text("Select file to compress")
input1 = sg.Input()
button1 = sg.FileBrowse("choose", key="files")

label2 = sg.Text("Select destination to store")
input2 = sg.Input()
button2 = sg.FolderBrowse("choose", key="folder")

compress_btn = sg.Button("compress")

window = sg.Window("Files Compressor", layout=[[label1,input1,button1],
                                               [label2,input2,button2],
                                               [compress_btn]])

while True:
    events, values = window.read()
    print(events, values)

    filepaths = values["files"].split(";")
    folder = values["folder"]

    make_Archive(filepaths, folder)

    break

window.close()
