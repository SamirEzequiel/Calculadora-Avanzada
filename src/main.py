import customtkinter as ctk
from calculadora import Calculadora
from tkinter import messagebox, filedialog

ctk.set_appearance_mode("dark")  # modo oscuro inicial
ctk.set_default_color_theme("blue")  # tema azul

class CalculadoraProfesional:
    def __init__(self):
        self.calc = Calculadora()
        self.expresion = ""
        self.historial = []
        self.memoria = 0.0

        # Ventana principal
        self.root = ctk.CTk()
        self.root.title("Calculadora Avanzada Profesional")
        self.root.geometry("450x650")
        self.root.resizable(False, False)

        self._crear_pantalla()
        self._crear_botones()
        self._crear_historial()
        self._crear_botones_historial()
        self._crear_modo_oscuro()

        self.root.mainloop()

    # Pantalla principal
    def _crear_pantalla(self):
        self.display = ctk.CTkEntry(self.root, font=("Arial", 24), justify="right")
        self.display.pack(fill="x", padx=10, pady=10)

    # Botones de la calculadora
    def _crear_botones(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(padx=10, pady=5, fill="both", expand=True)

        # Números
        numeros = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
            ("0", 3, 0), (".", 3, 1)
        ]
        for (num, r, c) in numeros:
            ctk.CTkButton(frame, text=num, command=lambda n=num: self._click(n),
                          height=50, width=50).grid(row=r, column=c, padx=5, pady=5)

        # Operaciones básicas
        operaciones = [
            ("+", 0, 3, "#4CAF50"), ("-", 1, 3, "#F44336"),
            ("*", 2, 3, "#2196F3"), ("/", 3, 3, "#FF9800"),
            ("=", 3, 2, "#9C27B0"), ("C", 3, 4, "#607D8B")
        ]
        for (op, r, c, color) in operaciones:
            ctk.CTkButton(frame, text=op, fg_color=color,
                          command=lambda o=op: self._click(o),
                          height=50, width=50).grid(row=r, column=c, padx=5, pady=5)

        # Funciones avanzadas
        funciones = [("sin", 4, 0), ("cos", 4, 1), ("tan", 4, 2), ("√", 4, 3), ("log", 5, 0)]
        for (f, r, c) in funciones:
            ctk.CTkButton(frame, text=f, command=lambda func=f: self._click(func),
                          height=50, width=50).grid(row=r, column=c, padx=5, pady=5)

        # Botones de memoria
        memoria = [("M+", 5, 1), ("M-", 5, 2), ("MR", 5, 3)]
        for (m, r, c) in memoria:
            ctk.CTkButton(frame, text=m, command=lambda mem=m: self._click(mem),
                          height=50, width=50).grid(row=r, column=c, padx=5, pady=5)

    # Historial con scroll
    def _crear_historial(self):
        self.historial_text = ctk.CTkTextbox(self.root, height=100)
        self.historial_text.pack(fill="both", padx=10, pady=5)

    # Botones de historial
    def _crear_botones_historial(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=5)

        ctk.CTkButton(frame, text="Borrar Historial", command=self._borrar_historial,
                      width=150).grid(row=0, column=0, padx=10)
        ctk.CTkButton(frame, text="Exportar Historial", command=self._exportar_historial,
                      width=150).grid(row=0, column=1, padx=10)

    # Botón para alternar modo oscuro/claro
    def _crear_modo_oscuro(self):
        ctk.CTkButton(self.root, text="Modo Claro/Oscuro",
                      command=self._toggle_modo, width=200).pack(pady=5)

    # Alternar modo
    def _toggle_modo(self):
        current = ctk.get_appearance_mode()
        ctk.set_appearance_mode("light" if current=="dark" else "dark")

    # Lógica de botones
    def _click(self, valor):
        if valor == "C":
            self.expresion = ""
            self.display.delete(0, "end")
        elif valor == "=":
            self._calcular()
        elif valor in ["M+", "M-", "MR"]:
            self._gestionar_memoria(valor)
        else:
            self.expresion += valor
            self.display.delete(0, "end")
            self.display.insert(0, self.expresion)

    # Memoria
    def _gestionar_memoria(self, valor):
        try:
            if valor == "M+":
                self.memoria += float(self.display.get())
            elif valor == "M-":
                self.memoria -= float(self.display.get())
            elif valor == "MR":
                self.display.delete(0, "end")
                self.display.insert(0, str(self.memoria))
                self.expresion = str(self.memoria)
        except:
            pass

    # Calcular
    def _calcular(self):
        try:
            if "sin" in self.expresion:
                num = float(self.expresion.replace("sin", ""))
                res = self.calc.seno(num)
            elif "cos" in self.expresion:
                num = float(self.expresion.replace("cos", ""))
                res = self.calc.coseno(num)
            elif "tan" in self.expresion:
                num = float(self.expresion.replace("tan", ""))
                res = self.calc.tangente(num)
            elif "√" in self.expresion:
                num = float(self.expresion.replace("√", ""))
                res = self.calc.raiz_cuadrada(num)
            elif "log" in self.expresion:
                num = float(self.expresion.replace("log", ""))
                res = self.calc.logaritmo(num)
            else:
                res = eval(self.expresion)

            self.display.delete(0, "end")
            self.display.insert(0, str(round(res, 6)))
            self.historial.append(f"{self.expresion} = {res}")
            self._actualizar_historial()
            self.expresion = str(res)
        except:
            messagebox.showerror("Error", "Expresión inválida")
            self.expresion = ""
            self.display.delete(0, "end")

    def _actualizar_historial(self):
        self.historial_text.delete("1.0", "end")
        for linea in self.historial[-10:]:
            self.historial_text.insert("end", linea + "\n")

    def _borrar_historial(self):
        if messagebox.askyesno("Confirmar", "¿Deseas borrar el historial?"):
            self.historial.clear()
            self._actualizar_historial()

    def _exportar_historial(self):
        if not self.historial:
            messagebox.showinfo("Información", "No hay historial para exportar.")
            return
        archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Archivo de texto", "*.txt")])
        if archivo:
            try:
                with open(archivo, "w", encoding="utf-8") as f:
                    for linea in self.historial:
                        f.write(linea + "\n")
                messagebox.showinfo("Éxito", f"Historial exportado a {archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo exportar: {e}")


if __name__ == "__main__":
    CalculadoraProfesional()
