<img src="https://i.ibb.co/LzHVNQvw/yt-Download.png" width="300" height="200">
<img alt="YouTube Downloader" src="https://i.ibb.co/qLfQ5pmS/programa.png" style="max-width: 100%;"></a></p>
<p dir="auto">Este script es una aplicación gráfica en Python que permite descargar videos o audios de YouTube. Utiliza la biblioteca <code><code>yt-dlp</code></code> para manejar las descargas y <code><code>tkinter</code></code> para la interfaz gráfica. Los usuarios pueden:</p>
<ol dir="auto">
<li><strong>Ingresar o pegar un enlace de YouTube</strong>.</li>
<li><strong>Seleccionar el formato de descarga</strong>: video o audio (MP3).</li>
<li><strong>Ver el progreso de la descarga</strong> mediante una barra de progreso.</li>
<li><strong>Guardar los archivos descargados en una carpeta seleccionada</strong>.</li>
</ol>
<p dir="auto">Para ejecutar este script en Windows, necesitas las siguientes dependencias:</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">tkinter:</h3><a id="user-content-tkinter" class="anchor" aria-label="Permalink: tkinter:" href="#tkinter"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Biblioteca estándar de Python para crear interfaces gráficas.
No requiere instalación adicional, ya que viene incluida con Python.
yt-dlp:</p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">yt-dlp:</h3><a id="user-content-yt-dlp" class="anchor" aria-label="Permalink: yt-dlp:" href="#yt-dlp"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
Herramienta para descargar videos y audios de YouTube.
Se instala con:
<code>pip install yt-dlp</code>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">ffmpeg:</h3><a id="user-content-ffmpeg" class="anchor" aria-label="Permalink: ffmpeg:" href="#ffmpeg"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Software necesario para procesar y convertir formatos de video y audio.
Descárgalo desde <a href="https://github.com/BtbN/FFmpeg-Builds/releases">FFmpeg</a>, descomprímelo y agrega los ejecutables de FFmpeg en la misma carpeta que este el script.</p>
<p dir="auto">Se utiliza para widgets avanzados como la barra de progreso.
Incluida con tkinter.</p>
<div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto">Resumen de instalación:</h1><a id="user-content-resumen-de-instalación" class="anchor" aria-label="Permalink: Resumen de instalación:" href="#resumen-de-instalación"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
Asegúrate de tener Python instalado (versión 3.6 o superior).
Instala yt-dlp y configura ffmpeg en tu computadora.
Con estas dependencias configuradas, el script funcionará correctamente en Windows. 😊
