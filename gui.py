import tkinter as tk
import platform

class SystemInfoApp:
    def __init__(self, master):
        self.master = master
        master.title("System Information App")

        self.label = tk.Label(master, text="Click the button to get system information.")
        self.label.pack()

        self.button = tk.Button(master, text="Get System Info", command=self.get_system_info)
        self.button.pack()

    def get_system_info(self):
        system_info = f"System: {platform.system()}\n"
        system_info += f"Node: {platform.node()}\n"
        system_info += f"Release: {platform.release()}\n"
        system_info += f"Version: {platform.version()}\n"
        system_info += f"Machine: {platform.machine()}\n"
        system_info += f"Processor: {platform.processor()}"

        self.label.config(text=system_info)

def main():
    root = tk.Tk()
    app = SystemInfoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
