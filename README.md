# 📷 Webcam Viewer (Cross-Platform)

Script Python sederhana, teroptimasi, dan mandiri (_standalone_) untuk menampilkan feed kamera laptop Anda. Dibuat untuk memastikan performa maksimal baik di Linux maupun Windows.

## ✨ Fitur Utama

- **Mandiri (Standalone)**: Hanya butuh satu file `main.py`—tidak perlu folder virtual environment yang berat.
- **Deteksi OS Otomatis**: Mengenali sistem operasi Anda dan secara otomatis memilih backend kamera terbaik.
- **Optimasi Performa**:
  - **Linux**: Menggunakan backend `V4L2` untuk menghilangkan delay/patah-patah.
  - **Windows**: Menggunakan `DirectShow (DSHOW)` untuk stabilitas.
- **Anti-Lag**: Mengatur ukuran buffer secara eksplisit untuk memastikan video tetap _real-time_.

## 🛠️ Prasyarat

- Python 3.x
- Library OpenCV

## 🚀 Instalasi & Penggunaan

### 🐧 Linux (Pop!\_OS / Ubuntu / Debian)

Karena distro Linux modern mengelola environment Python dengan ketat (PEP 668), ikuti langkah ini untuk instalasi global yang bersih:

1. **Instalasi Dependencies**:
   ```bash
   sudo apt update && sudo apt install python3-opencv python-is-python3 -y
   ```
2. **Jalankan Script**:
   ```bash
   python main.py
   ```
   _Catatan: Jika jendela tidak muncul di sistem Wayland, gunakan command:_ `export QT_QPA_PLATFORM=xcb && python main.py`

### 🪟 Windows

1. **Instalasi OpenCV**:
   ```cmd
   pip install opencv-python
   ```
2. **Jalankan Script**:
   ```cmd
   python main.py
   ```

## ⌨️ Kontrol

- **Tekan 'q'**: Untuk menutup jendela kamera dan keluar dari program dengan aman.
- **Ctrl + C**: Untuk menghentikan paksa melalui terminal.

## Tanda

Bebas digunakan dan dimodifikasi untuk keperluan apapun.

Terimakasih Enjoy Coding! ☕🚬
