import PySimpleGUI as sg
import os


clear = lambda: os.system('cls')

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Clock singal')],
            [sg.Checkbox('Enable', default=False)], #0
            [sg.Text("Switches")],
            [sg.Checkbox('Enable', default=False)], #1
            [sg.Text("LEDs")],
            [sg.Checkbox('Enable', default=False)], #2
            [sg.Text("7 segment display")],
            [sg.Checkbox('Enable', default=False)], #3
            [sg.Text("Buttons")],
            [sg.Checkbox('Enable', default=False)], #4
            [sg.Button('Ok'), sg.Button('Cancel')] 
         ]

if not os.path.exists("output"):
    os.makedirs("output")

with open("output/constraints.xdc", "w") as file:
    file.close()


# Create the Window
window = sg.Window('Python constrainsfile creator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    clear()

    if values[0]:
        print("Clock signal enabled")
    if values[1]:
        print("Switches enabled")
    if values[2]:
        print("LEDs enabled")
    if values[3]:  
        print("7 segment display enabled")
    if values[4]:
        print("Buttons enabled")
    

window.close()