import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from calculadora import Calculadora

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avanzada")
        self.root.geometry("500x650")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        self.calc = Calculadora()
        self.expresion = ""
        self.historial = []
        self.memoria = 0.0

        self._crear_estilo()
        self._crear_pantalla()
        self._crear_botones()
        self._crear_historial()
        self._crear_botones_historial()

        # Atajos de teclado
        self.root.bind("<Return>", lambda e: self.calcular())
        self.root.bind("<BackSpace>", lambda e: self.borrar_ultimo())

    def _crear_estilo(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton",
                        font=("Arial", 14),
                        padding=10,
                        foreground="#ffffff",
                        background="#333333")
        style.map("TButton",
                  background=[("active", "#444444")])

    def _crear_pantalla(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), justify="right", bd=5,
                                bg="#1e1e1e", fg="#ffffff", insertbackground="white")
        self.display.pack(fill="x", padx=10, pady=10)

    def _crear_botones(self):
        frame = tk.Frame(self.root, bg="#121212")
        frame.pack(pady=10)

        botones = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("^", 3, 2), ("+", 3, 3),
            ("sin", 4, 0), ("cos", 4, 1), ("tan", 4, 2), ("√", 4, 3),
            ("log", 5, 0), ("C", 5, 1), ("=", 5, 2), ("Salir", 5, 3),
            ("M+", 6, 0), ("M-", 6, 1), ("MR", 6, 2)
        ]

        for (texto, fila, col) in botones:
            boton = ttk.Button(frame, text=texto,
                               command=lambda t=texto: self._click_boton(t))
            boton.grid(row=fila, column=col, padx=5, pady=5, ipadx=10, ipady=10)

    def _crear_historial(self):
        historial_frame = tk.Frame(self.root, bg="#1e1e1e")
        historial_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(historial_frame, text="Historial", font=("Arial", 14),
                 bg="#1e1e1e", fg="white").pack(anchor="w")

        self.historial_text = tk.Text(historial_frame, height=8, bg="#1e1e1e",
                                      fg="white", font=("Arial", 12), state="disabled")
        self.historial_text.pack(fill="both", expand=True)

    def _crear_botones_historial(self):
        frame = tk.Frame(self.root, bg="#121212")
        frame.pack(pady=5)

        borrar_btn = ttk.Button(frame, text="Borrar Historial",
                                command=self._borrar_historial)
        borrar_btn.grid(row=0, column=0, padx=10, pady=5)

        exportar_btn = ttk.Button(frame, text="Exportar Historial",
                                  command=self._exportar_historial)
        exportar_btn.grid(row=0, column=1, padx=10, pady=5)

    def _click_boton(self, valor):
        if valor == "C":
            self.expresion = ""
            self.display.delete(0, tk.END)
        elif valor == "=":
            self.calcular()
        elif valor == "Salir":
            self.root.quit()
        elif valor == "M+":
            try:
                self.memoria += float(self.display.get())
            except:
                pass
        elif valor == "M-":
            try:
                self.memoria -= float(self.display.get())
            except:
                pass
        elif valor == "MR":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(self.memoria))
            self.expresion = str(self.memoria)
        else:
            self.expresion += valor
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expresion)

    def borrar_ultimo(self):
        self.expresion = self.expresion[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expresion)

    def calcular(self):
        try:
            if "sin" in self.expresion:
                num = float(self.expresion.replace("sin", ""))
                resultado = self.calc.seno(num)
            elif "cos" in self.expresion:
                num = float(self.expresion.replace("cos", ""))
                resultado = self.calc.coseno(num)
            elif "tan" in self.expresion:
                num = float(self.expresion.replace("tan", ""))
                resultado = self.calc.tangente(num)
            elif "√" in self.expresion:
                num = float(self.expresion.replace("√", ""))
                resultado = self.calc.raiz_cuadrada(num)
            elif "log" in self.expresion:
                num = float(self.expresion.replace("log", ""))
                resultado = self.calc.logaritmo(num)
            elif "^" in self.expresion:
                a, b = map(float, self.expresion.split("^"))
                resultado = self.calc.potencia(a, b)
            else:
                resultado = eval(self.expresion)

            self._mostrar_resultado(resultado)

        except Exception:
            messagebox.showerror("Error", "Expresión inválida")
            self.expresion = ""
            self.display.delete(0, tk.END)

    def _mostrar_resultado(self, resultado):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(round(resultado, 6)))
        self.historial.append(f"{self.expresion} = {resultado}")
        self._actualizar_historial()
        self.expresion = str(resultado)

    def _actualizar_historial(self):
        self.historial_text.config(state="normal")
        self.historial_text.delete("1.0", tk.END)
        for linea in self.historial[-10:]:
            self.historial_text.insert(tk.END, linea + "\n")
        self.historial_text.config(state="disabled")

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
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
