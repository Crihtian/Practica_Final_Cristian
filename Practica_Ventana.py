import psutil
import tkinter as tk

class SystemMonitor:
    """Clase para monitorizar el uso de recursos del sistema."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Monitorización de Recursos del Sistema")
        self.root.geometry("400x300")  # Tamaño de la ventana

        # Crear etiquetas para mostrar la información
        self.cpu_label = tk.Label(self.root, text="Uso de CPU: 0%", font=("Arial", 14))
        self.cpu_label.pack(pady=10)

        self.ram_label = tk.Label(self.root, text="Uso de RAM: 0%", font=("Arial", 14))
        self.ram_label.pack(pady=10)

        self.disk_label = tk.Label(self.root, text="Uso de Disco: 0%", font=("Arial", 14))
        self.disk_label.pack(pady=10)

        # Iniciar la actualización de los datos
        self.update_data()

        # Ejecutar la interfaz gráfica
        self.root.mainloop()

    def update_data(self):
        """Actualizar los datos de uso de recursos del sistema."""
        cpu_usage = psutil.cpu_percent(interval=0.5)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        # Actualizar las etiquetas con los nuevos valores
        self.cpu_label.config(text=f"Uso de CPU: {cpu_usage}%")
        self.ram_label.config(text=f"Uso de RAM: {memory_usage}%")
        self.disk_label.config(text=f"Uso de Disco: {disk_usage}%")

        # Llamar a la función cada medio segundo
        self.root.after(500, self.update_data)

if __name__ == "__main__":
    SystemMonitor()
