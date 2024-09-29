import PySimpleGUI as sg

label1 = sg.Text("Select file to compress")
input1 = sg.Input()
button1 = sg.FileBrowse("choose")

label2 = sg.Text("Select destination to store")
input2 = sg.Input()
button2 = sg.FileBrowse("choose")

compress_btn = sg.Button("compress")

window = sg.Window("Files Compressor", layout=[[label1,input1,button1],
                                               [label2,input2,button2],
                                               [compress_btn]])

window.read()
window.close()
