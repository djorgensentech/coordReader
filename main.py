import tkinter as tk
from coord_reader_app import CoordReaderApp


def main():
    # Create the Tkinter root window
    root = tk.Tk()

    # Create an instance of the CoordReaderApp class
    app = CoordReaderApp(root)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
