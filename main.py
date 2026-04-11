import cv2
import sys

def buka_kamera():
    """
    Script kamera lintas-platform (Windows & Linux) dengan optimasi performa.
    """
    # Pilih backend terbaik berdasarkan OS
    if sys.platform.startswith('linux'):
        backend = cv2.CAP_V4L2
    elif sys.platform.startswith('win'):
        backend = cv2.CAP_DSHOW
    else:
        backend = None

    # Inisialisasi kamera
    if backend is not None:
        cap = cv2.VideoCapture(0, backend)
    else:
        cap = cv2.VideoCapture(0)

    # Optimasi: Set resolusi dan matikan buffer untuk mengurangi latency
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    if not cap.isOpened():
        # Fallback terakhir jika backend spesifik gagal
        if backend is not None:
            cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Kesalahan: Tidak dapat mengakses kamera.")
            sys.exit(1)

    print("--- Sesi Kamera Dimulai (Optimasi Aktif) ---")
    print("Aksi: Tekan 'q' untuk keluar.")

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Kesalahan: Gagal mengambil gambar.")
                break

            cv2.imshow('Kamera Laptop', frame)

            # Tombol q untuk keluar
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("\nSesi dihentikan.")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("--- Sesi Kamera Berakhir ---")

if __name__ == "__main__":
    buka_kamera()
