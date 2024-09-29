import functon
import PySimpleGUI as sg

label = sg.Text("Type in a To DO")
input_box = sg.InputText(tooltip="Enter todo")

add_btn = sg.Button("Add")

windows = sg.Window("My To Do App", layout=[[label],[input_box, add_btn]])
windows.read()
windows.close()