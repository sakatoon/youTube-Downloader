import yt_dlp
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import threading

class YouTubeMusicDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Descargador de Música y Video de YouTube")
        self.root.resizable(False, False)

        # Variables
        self.url_var = tk.StringVar()
        self.output_var = tk.StringVar(value=os.getcwd())
        self.quality_var = tk.StringVar(value="medium")
        self.progress_var = tk.StringVar(value="Listo para descargar")
        self.download_type = tk.StringVar(value="mp3")  # mp3 o video

        # Centrar la ventana con tamaño aumentado
        self.center_window(600, 450)

        # Interfaz
        self.create_widgets()

    def center_window(self, width, height):
        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular coordenadas para centrar
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Establecer geometría
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Etiqueta y entrada para URL
        tk.Label(self.root, text="URL de YouTube (video o lista):").pack(pady=10)
        url_frame = tk.Frame(self.root)
        url_frame.pack(pady=5)
        tk.Entry(url_frame, textvariable=self.url_var, width=50).pack(side=tk.LEFT, padx=5)
        tk.Button(url_frame, text="Pegar", command=self.paste_link).pack(side=tk.LEFT)

        # Carpeta de salida
        tk.Label(self.root, text="Carpeta de salida:").pack(pady=10)
        output_frame = tk.Frame(self.root)
        output_frame.pack()
        tk.Entry(output_frame, textvariable=self.output_var, width=50).pack(side=tk.LEFT)
        tk.Button(output_frame, text="Seleccionar", command=self.select_output_folder).pack(side=tk.LEFT, padx=5)

        # Calidad de audio
        tk.Label(self.root, text="Calidad de audio (para MP3):").pack(pady=10)
        quality_options = ["best (320kbps)", "medium (192kbps)", "low (128kbps)"]
        ttk.Combobox(self.root, textvariable=self.quality_var, values=quality_options, state="readonly").pack()

        # Tipo de descarga (MP3 o Video)
        tk.Label(self.root, text="Tipo de descarga:").pack(pady=10)
        type_frame = tk.Frame(self.root)
        type_frame.pack()
        tk.Radiobutton(type_frame, text="Audio (MP3)", variable=self.download_type, value="mp3").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(type_frame, text="Video (MP4)", variable=self.download_type, value="video").pack(side=tk.LEFT, padx=10)

        # Botón de descarga
        tk.Button(self.root, text="Descargar", command=self.start_download_thread).pack(pady=20)

        # Barra de progreso
        self.progress_bar = ttk.Progressbar(self.root, length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

        # Etiqueta de estado
        tk.Label(self.root, textvariable=self.progress_var, wraplength=500).pack(pady=10)

        # Leyenda Desarrollado por
        tk.Label(self.root, text="Desarrollado por: SakaToOn", font=("Arial", 10, "italic")).pack(side=tk.BOTTOM, pady=5)

    def paste_link(self):
        # Pegar el enlace desde el portapapeles
        self.url_var.set(self.root.clipboard_get())

    def select_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_var.set(folder)

    def start_download_thread(self):
        # Iniciar la descarga en un hilo separado para no congelar la GUI
        thread = threading.Thread(target=self.download_music)
        thread.daemon = True
        thread.start()

    def download_music(self):
        url = self.url_var.get().strip()
        output_path = self.output_var.get().strip()
        quality = self.quality_var.get().split()[0].lower()
        download_type = self.download_type.get()

        if not url:
            self.progress_var.set("Error: Ingresa una URL válida")
            messagebox.showerror("Error", "Por favor, ingresa una URL de YouTube")
            return

        if not os.path.exists(output_path):
            try:
                os.makedirs(output_path)
            except Exception as e:
                self.progress_var.set(f"Error al crear carpeta: {str(e)}")
                messagebox.showerror("Error", f"No se pudo crear la carpeta: {str(e)}")
                return

        try:
            ydl_opts = {
                'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),  # Incluir índice para listas
                'noplaylist': False,  # Permitir listas de reproducción
                'quiet': False,
                'progress_hooks': [self.progress_hook],
            }

            if download_type == "mp3":
                quality_settings = {
                    'best': '320',
                    'medium': '192',
                    'low': '128'
                }
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': quality_settings.get(quality, '192'),
                    }],
                })
            else:  # video
                ydl_opts.update({
                    'format': 'bestvideo+bestaudio/best',
                    'merge_output_format': 'mp4',
                })

            self.progress_var.set("Iniciando descarga...")
            self.progress_bar["value"] = 0
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.progress_var.set("¡Descarga completada!")
            messagebox.showinfo("Éxito", "Descarga completada correctamente")

        except Exception as e:
            self.progress_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error durante la descarga: {str(e)}")

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%').strip().replace('%', '')
            try:
                percent_float = float(percent)
                self.progress_bar["value"] = percent_float
                speed = d.get('_speed_str', 'N/A').strip()
                eta = d.get('_eta_str', 'N/A').strip()
                title = d.get('info_dict', {}).get('title', 'N/A')
                playlist_index = d.get('info_dict', {}).get('playlist_index', '')
                if playlist_index:
                    self.progress_var.set(f"Canción {playlist_index}: {title} | Progreso: {percent}% | Velocidad: {speed} | ETA: {eta}")
                else:
                    self.progress_var.set(f"Progreso: {percent}% | Velocidad: {speed} | ETA: {eta}")
            except ValueError:
                pass
        elif d['status'] == 'finished':
            self.progress_bar["value"] = 100
            self.progress_var.set("Procesando archivo...")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeMusicDownloader(root)
    root.mainloop()