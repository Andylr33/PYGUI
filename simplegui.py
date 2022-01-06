import PySimpleGUI as sg

# ----------------

# Step 1: Set the theme for the window application
sg.theme('DarkAmber')

# Step 2: Layout for the window
layout = [

    [sg.Text("Enter your name: ")],
    [sg.InputText()],
    [sg.Button("OK"), sg.Button("Cancel")]  # have two elements in same row
]

# Step 3: Create the Window
window = sg.Window("Form", layout, size=(1400, 600))

# Step 4: Event loop, so window does not close until told to do so.
while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    print(values[0])

# event, values = window.read()  # gets the events and values inputted

# Step 5: Close the window
window.close()
