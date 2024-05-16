import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Microsoft Windows")
root.attributes('-fullscreen', True)

# Create a frame with specified background color
frame = tk.Frame(root, bg="#000088")
frame.pack(fill=tk.BOTH, expand=True)


label_font = ('Lucida Console', 100)
bsod_text = """
):
"""
label = tk.Label(frame, text=bsod_text, font=label_font, bg="#000088", fg="white")
label.pack()



# Create a label for the text
label_font = ('Lucida Console', 14)
label = tk.Label(frame, text="A problem has been detected and Windows has been shut down to prevent damage to your computer.\n\nDRIVER_IRQL_NOT_LESS_OR_EQUAL\n\nIf this is the first time you've seen this stop error screen, restart your computer.\n\n If this screen appears again, follow these steps:\n\nCheck to make sure any new hardware or software is properly installed.\n\n If this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need.\n\nIf problems continue, disable or remove any newly installed hardware or software.\n\n Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.\n\nTechnical information:\n\nSTOP: 0x00D1 (0x00C,0x002,0x00,0xF86B5A89)\n\ngv3.sys - Address F86B5A89 base at F86B5000, DateStamp 3dd9919eb\n\nBeginning dump of physical memory\nPhysical memory dump complete.\n\nContact your system administrator or technical support group for further assistance.", font=label_font, bg="#000088", fg="white")
label.pack()

# Function to prevent right and middle mouse clicks
def no_click(event):
    if event.num == 2 or event.num == 3:
        messagebox.showerror("Error", "00101100x00100100 missing keymgr.dll")

# Bind the function to mouse clicks
root.bind("<Button-2>", no_click)
root.bind("<Button-3>", no_click)

root.mainloop()
