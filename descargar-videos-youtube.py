import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from yt_dlp import YoutubeDL

# Detectar si se ejecuta como .exe
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

# Ruta a ffmpeg
ffmpeg_path = os.path.join(base_path, 'ffmpeg.exe')
os.environ['PATH'] = os.path.dirname(ffmpeg_path) + os.pathsep + os.environ['PATH']

# Ruta al icono
icono_path = os.path.join(base_path, 'youtube.ico')

# Inicializar ventana
ventana = tk.Tk()
ventana.title("Descargar vídeo de YouTube")
ventana.geometry("550x250")
ventana.resizable(False, False)

# Aplicar icono si existe
if os.path.exists(icono_path):
    try:
        ventana.iconbitmap(icono_path)
    except Exception as e:
        print(f"⚠️ No se pudo aplicar el icono: {e}")

# Ruta seleccionada por el usuario
directorio_salida = None

# Selector de carpeta
def seleccionar_carpeta():
    global directorio_salida
    carpeta = filedialog.askdirectory()
    if carpeta:
        directorio_salida = carpeta
        etiqueta_carpeta.config(text=f"📁 Carpeta seleccionada:\n{directorio_salida}")

# Hook de progreso
def progreso_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            porcentaje = int(downloaded * 100 / total)
            barra_progreso['value'] = porcentaje
            ventana.update_idletasks()
    elif d['status'] == 'finished':
        barra_progreso['value'] = 100
        ventana.update_idletasks()

# Función principal de descarga
def descargar_video():
    url = entrada_url.get().strip()
    if not url:
        messagebox.showwarning("Falta el enlace", "Introduce un enlace de YouTube.")
        return
    if not directorio_salida:
        messagebox.showwarning("Falta carpeta", "Selecciona dónde guardar el vídeo.")
        return

    barra_progreso['value'] = 0
    ventana.update_idletasks()

    ydl_opts = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]',
        'outtmpl': os.path.join(directorio_salida, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [progreso_hook],
        'quiet': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("✅ Descarga completada", "El vídeo se ha descargado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")

# Interfaz gráfica
tk.Label(ventana, text="🔗 Enlace de YouTube:").pack(pady=10)
entrada_url = tk.Entry(ventana, width=70)
entrada_url.pack()

tk.Button(ventana, text="📁 Seleccionar carpeta de descarga", command=seleccionar_carpeta).pack(pady=5)
etiqueta_carpeta = tk.Label(ventana, text="📁 Aún no se ha seleccionado ninguna carpeta", fg="gray")
etiqueta_carpeta.pack()

tk.Button(ventana, text="⬇️ Descargar vídeo", command=descargar_video).pack(pady=10)

barra_progreso = ttk.Progressbar(ventana, length=400, mode='determinate')
barra_progreso.pack(pady=10)

ventana.mainloop()
