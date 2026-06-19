import tkinter as tk
from tkinter import ttk
import psutil


def obtener_datos():
    medir_cpu = psutil.cpu_percent(interval=1)

    medir_ram = psutil.virtual_memory()
    porcentaje_ram = medir_ram.percent
    ram_usado_gb = medir_ram.used / (1024 ** 3)
    ram_total_gb = medir_ram.total / (1024 ** 3)

    medir_disco = psutil.disk_usage("/")
    porcentaje_disco = medir_disco.percent
    disco_usado = medir_disco.used / (1024 ** 3)
    disco_total = medir_disco.total / (1024 ** 3)

    sensores = psutil.sensors_temperatures()
    temp_cpu = sensores["k10temp"][0].current

    datos = {
        "cpu": medir_cpu,
        "ram": {
            "porcentaje": porcentaje_ram,
            "usado_gb":   ram_usado_gb,
            "total_gb":   ram_total_gb
        },
        "disco": {
            "porcentaje": porcentaje_disco,
            "usado_gb":   disco_usado,
            "total_gb":   disco_total
        },
        "temperatura": temp_cpu
    }
    return datos


class MonitorApp:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Monitor de Sistema")
        self.crear_widgets()
        self.ventana.after(1000, self.actualizar)
        self.ventana.attributes("-topmost", True)

    def crear_widgets(self):
        tk.Label(self.ventana, text="CPU").pack()
        self.var_cpu = tk.IntVar()
        self.barra_cpu = ttk.Progressbar(self.ventana, variable=self.var_cpu, maximum=100, length=300)
        self.barra_cpu.pack()
        self.label_cpu = tk.Label(self.ventana, text="0%")
        self.label_cpu.pack()

        tk.Label(self.ventana, text="RAM").pack()
        self.var_ram = tk.IntVar()
        self.barra_ram = ttk.Progressbar(self.ventana, variable=self.var_ram, maximum=100, length=300)
        self.barra_ram.pack()
        self.label_ram = tk.Label(self.ventana, text="0%")
        self.label_ram.pack()

        tk.Label(self.ventana, text="Disco").pack()
        self.var_disk = tk.IntVar()
        self.barra_disk = ttk.Progressbar(self.ventana, variable=self.var_disk, maximum=100, length=300)
        self.barra_disk.pack()
        self.label_disk = tk.Label(self.ventana, text="0%")
        self.label_disk.pack()

        tk.Label(self.ventana, text="Temperatura CPU").pack()
        self.label_temp = tk.Label(self.ventana, text="0°C")
        self.label_temp.pack()

    def elegir_color(self, porcentaje):
        if porcentaje < 60:
            return "green"
        elif porcentaje < 85:
            return "orange"
        else:
            return "red"

    def actualizar(self):
        datos = obtener_datos()

        self.var_cpu.set(datos["cpu"])
        self.label_cpu.config(
            text=f"{datos['cpu']}%",
            fg=self.elegir_color(datos["cpu"])
        )

        self.var_ram.set(datos["ram"]["porcentaje"])
        self.label_ram.config(
            text=f"{datos['ram']['porcentaje']}% — {round(datos['ram']['usado_gb'], 1)} GB",
            fg=self.elegir_color(datos["ram"]["porcentaje"])
        )

        self.var_disk.set(datos["disco"]["porcentaje"])
        self.label_disk.config(
            text=f"{datos['disco']['porcentaje']}% — {round(datos['disco']['usado_gb'], 1)} GB",
            fg=self.elegir_color(datos["disco"]["porcentaje"])
        )

        temp = datos["temperatura"]
        self.label_temp.config(
            text=f"{temp}°C",
            fg=self.elegir_color(temp)
        )

        self.ventana.after(1000, self.actualizar)


root = tk.Tk()
app = MonitorApp(root)
root.mainloop()
