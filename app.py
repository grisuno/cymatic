#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""
app.py

Autor: Gris Iscomeback
Correo electrónico: grisiscomeback[at]gmail[dot]com
Fecha de creación: xx/xx/xxxx
Licencia: GPL v3

Descripción:  
"""
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

class CymaticsVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Cimáticas por Frecuencia")
        
        self.label = tk.Label(root, text="Visualizador de Cimáticas", font=("Arial", 24), fg="white", bg="#1a1a1a")
        self.label.pack(pady=20)
        
        self.frame = tk.Frame(root, bg="#1a1a1a")
        self.frame.pack(pady=20)
        
        self.frequency_input = tk.Entry(self.frame, font=("Arial", 16), width=10)
        self.frequency_input.pack(side=tk.LEFT, padx=10)
        
        self.visualize_button = tk.Button(self.frame, text="Visualizar", font=("Arial", 16), bg="#4CAF50", fg="white", command=self.visualize)
        self.visualize_button.pack(side=tk.LEFT, padx=10)
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white", bd=2, relief=tk.SOLID)
        self.canvas.pack(pady=20)
        
        self.draw_cymatic(440)

    def draw_cymatic(self, frequency):
        width, height = 400, 400
        centerX, centerY = width // 2, height // 2
        radius = min(width, height) // 2 - 10

        image = np.zeros((height, width))

        for x in range(width):
            for y in range(height):
                dx = x - centerX
                dy = y - centerY
                distance = np.sqrt(dx**2 + dy**2)

                if distance <= radius:
                    angle = np.arctan2(dy, dx)
                    value = np.sin(distance / 5 * np.log(frequency)) * np.cos(angle * frequency / 10)
                    intensity = int((value + 1) * 127.5)
                    image[y, x] = intensity

        plt.imshow(image, cmap='gray', extent=(0, width, 0, height))
        plt.axis('off')
        plt.savefig("cymatic_pattern.png", bbox_inches='tight', pad_inches=0)
        plt.close()

        self.cymatic_image = tk.PhotoImage(file="cymatic_pattern.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.cymatic_image)

    def visualize(self):
        try:
            frequency = float(self.frequency_input.get())
            if 20 <= frequency <= 20000:
                self.draw_cymatic(frequency)
            else:
                messagebox.showerror("Error", "Por favor, ingrese una frecuencia entre 20 Hz y 20,000 Hz.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#1a1a1a")
    app = CymaticsVisualizer(root)
    root.mainloop()
