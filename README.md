# 📥 **Descargador de vídeos de YouTube (con interfaz gráfica)**

He creado esta aplicación para mi madre, que necesitaba una forma **fácil, segura y sin complicaciones técnicas** para poder descargar vídeos de YouTube para sus clases de religión.  
La idea es que **cualquier persona —sin conocimientos de informática— pueda usarla cómodamente** para guardar vídeos educativos, musicales o personales en su ordenador.

---

## ✅ **¿Qué hace esta aplicación?**

- Descarga vídeos de YouTube en calidad **hasta 1080p**.  
- Fusiona automáticamente vídeo y audio en un solo archivo **.mp4**.  
- Permite **elegir la carpeta de destino** para cada vídeo.  
- Muestra una **barra de progreso** durante la descarga.  
- Tiene una interfaz **clara y sencilla**, desarrollada con **Tkinter**.  
- Funciona en **Windows** y **no requiere instalación de Python ni ffmpeg** en el equipo final.

---

## 🛠️ **¿Qué contiene este repositorio?**

- `descargar-youtube-gui.py` → El script principal en Python.  
- `youtube.ico` → Icono personalizado estilo YouTube.  
- `ffmpeg.exe` → Ejecutable necesario para unir vídeo y audio.  
- `requirements.txt` → Archivo con las dependencias necesarias.  
- Este `README.md` con todas las instrucciones paso a paso.

---

## 🚀 **Cómo generar el `.exe` final paso a paso**

### 📦 **1. Prepara tu carpeta**

Crea una carpeta de trabajo y coloca en ella los siguientes archivos:

```
descargar-youtube/
├── descargar-youtube-gui.py
├── ffmpeg.exe
├── youtube.ico
├── requirements.txt
```

🔹 Puedes descargar `ffmpeg.exe` desde: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)  
Solo necesitas el archivo `ffmpeg.exe` que se encuentra dentro de la carpeta `/bin` del ZIP descargado.

---

### 🐍 **2. Crea un entorno virtual** (opcional pero recomendable)

**En Windows (CMD o PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 **3. Instala las dependencias desde `requirements.txt`**

```bash
pip install -r requirements.txt
```

Este archivo incluye:

- `yt-dlp`  
- `pyinstaller`

---

### 🧱 **4. Compila el `.exe` con icono y `ffmpeg` integrados**

```bash
pyinstaller --onefile --windowed --icon=youtube.ico --add-data "youtube.ico;." --add-binary "ffmpeg.exe;." descargar-youtube-gui.py
```

---

### 📁 **5. Ejecuta tu aplicación**

El ejecutable generado estará en la carpeta `dist/` con el nombre:

```
dist/descargar-youtube-gui.exe
```

✅ Este archivo puede ejecutarse en **cualquier equipo Windows** sin necesidad de instalar Python, ffmpeg, ni nada adicional.

---

## 🖼️ **¿Qué ve el usuario?**

- Una ventana sencilla para **pegar el enlace de YouTube**.  
- Un botón para **elegir la carpeta de guardado**.  
- Una **barra de progreso** durante la descarga.  
- Un **aviso** cuando la descarga ha finalizado correctamente.

---

## 🔧 **Tecnologías utilizadas**

- **yt-dlp**: herramienta moderna y potente para descargar vídeos de YouTube.  
- **tkinter**: interfaz gráfica integrada en Python.  
- **ffmpeg**: combina vídeo y audio en un solo archivo con calidad óptima.

---

## 📜 **Licencia**

Este proyecto está publicado bajo la licencia **MIT**.

Hazlo tuyo, compártelo, ¡y si puede ayudar a más madres, padres o profesores... aún mejor! ❤️
