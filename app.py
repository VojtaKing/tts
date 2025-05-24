import flet as ft
import pyttsx3

def main(page: ft.Page):
    page.title = "Flet Window Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    entry = ft.TextField(label="Enter something")

    def on_button_click(_):
        engine = pyttsx3.init()
        engine.say(entry.value)
        engine.runAndWait()

    def save():
        engine = pyttsx3.init()
        engine.save_to_file(entry.value, filename.value)
        engine.runAndWait()


    button = ft.Button("Say", on_click=on_button_click)
    save_button = ft.Button("Save", on_click=lambda _: save())
    filename = ft.TextField(label="Filename", value="output.mp3")
    page.add(entry, button, save_button, filename)

ft.app(target=main)