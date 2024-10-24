import tkinter as tk
import keyboard
import mouse
import pyautogui


class CoordReaderApp:
    def __init__(self, master):
        # Initialize the Tkinter window
        self.master = master
        self.master.title("Coord-Reader")  # Set window title
        self.master.geometry("300x250")  # Set default window size

        # Set window icon
        self.master.iconbitmap("coords.ico")

        # Label to display "Mouse Position"
        self.label = tk.Label(master, text="Mouse Position", font=("Arial", 12))
        self.label.pack()

        # Label to display the current mouse coordinates
        self.coord_label = tk.Label(master, text="Win + Alt", font=("Arial", 36))
        self.coord_label.pack()

        # Label to display "Color:"
        self.color_label = tk.Label(master, text="Color:", font=("Arial", 12))
        self.color_label.pack()

        # Label to display the color as a small colored box
        self.color_box = tk.Label(master, bg="white", width=10, height=2)
        self.color_box.pack()

        # Start monitoring mouse position and updating the GUI
        self.update_mouse_position()

    def update_mouse_position(self):
        # Check if the 'esc' key is pressed to exit the program
        if keyboard.is_pressed('esc'):
            self.master.destroy()
            return

        # Check if 'Win + Alt' is pressed to update mouse position and color
        if keyboard.is_pressed('alt') and keyboard.is_pressed('win'):
            # Get the current mouse position
            position = mouse.get_position()
            position_str = f"{position[0]} {position[1]}"

            # Update the coordinate label with the current mouse position
            self.coord_label.config(text=position_str)

            # Get the color of the pixel at the current mouse position
            color = pyautogui.pixel(position[0], position[1])

            # Update the color box with the color of the pixel
            self.color_box.config(bg=f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}")

            # Update the color label with the color value
            self.color_label.config(text=f"Color: #{color[0]:02X}{color[1]:02X}{color[2]:02X}")

        # Schedule the next update after 100 milliseconds
        self.master.after(100, self.update_mouse_position)


def main():
    # Create the Tkinter root window
    root = tk.Tk()

    # Create an instance of the CoordReaderApp class
    app = CoordReaderApp(root)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
