import tkinter as tk

class ConsultarDatosRiego(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Consultar datos del riego")
        self.geometry("500x400")

        label = tk.Label(self, text="Consultar datos del riego", font=("Arial", 14))
        label.pack(pady=20)

        button = tk.Button(self, text="Siguiente", command=self.mostrarDatosRiego)
        button.pack()

    def mostrarDatosRiego(self):
        self.withdraw()  # Ocultar esta ventana
        ventanaDatosRiego = VisualizacionDatosRiego(self)
        ventanaDatosRiego.deiconify()  # Mostrar la ventana de datos de riego

class VisualizacionDatosRiego(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Datos del riego")
        self.geometry("500x400")

        # Simulación de datos
        nivel_agua = 90
        humedad_tierra = 70
        hora_ultimo_riego = "10:30:45"
        estado_valvula = "Abierta"

        label = tk.Label(self, text="Consultar datos del riego", font=("Arial", 14))
        label.pack(pady=20)

        label_nivel_agua = tk.Label(self, text=f"Nivel de agua: {nivel_agua}%")
        label_nivel_agua.pack()

        label_humedad_tierra = tk.Label(self, text=f"Humedad de tierra: {humedad_tierra}%")
        label_humedad_tierra.pack()

        label_hora_ultimo_riego = tk.Label(self, text=f"Hora último riego: {hora_ultimo_riego}")
        label_hora_ultimo_riego.pack()

        label_estado_valvula = tk.Label(self, text=f"Estado válvula: {estado_valvula}")
        label_estado_valvula.pack()

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=20)

        button_atras = tk.Button(frame_botones, text="Atrás", command=self.volverAConsultar)
        button_atras.pack(side=tk.LEFT, padx=10)

    def volverAConsultar(self):
        self.withdraw()  # Ocultar esta ventana
        self.master.deiconify()  # Mostrar la ventana de consulta de datos

if __name__ == "__main__":
    app = ConsultarDatosRiego()
    app.mainloop()
