class BluetoothApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    #    self.master = master
        self.title("Bluetooth App")
        self.geometry("700x450")

        # self.button = tk.Button(master, text="Connect", command=self.connect)
        # self.button.pack()

    async def discover_devices(self):
        devices = await discover()
        print("Discovered devices:")
        for device in devices:
            print(device)

    def connect(self):
        asyncio.run(self.discover_devices())

root = tk.Tk()
app = BluetoothApp()
root.mainloop()