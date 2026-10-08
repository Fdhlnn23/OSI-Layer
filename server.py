import socket

def server_program():
    host = '127.0.0.1' # Mendengarkan pada IP lokal (Layer 3)
    port = 5000        # Menyediakan Port khusus (Layer 4)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("[SERVER READY] Menunggu koneksi masuk di port 5000...")

    # Membuka sesi menerima data (Layer 5)
    conn, address = server_socket.accept()
    print(f"[LAYER 5] Sesi terhubung dengan klien dari alamat: {address}")

    while True:
        # 1. MENERIMA ALIRAN BIT/BYTES (Physical & Data Link - Layer 1 & 2)
        # recv(1024) artinya mengambil data mentah sebesar maksimal 1024 bytes dari buffer network card
        data_mentah = conn.recv(1024)
        if not data_mentah:
           break

        print("\n[OSI ALUR] Data fisik diterima! Mengawali proses Dekapsulasi...")
        print(f"[LAYER 1-2] Data biner mentah yang ditangkap: {data_mentah}")

        # 2. MEMBONGKAR TRANSPORT & NETWORK (Layer 3 & 4)
        # Sistem operasi secara otomatis memvalidasi IP (L3) dan nomor port (L4)
        # sehingga data ini berhasil lolos masuk ke program Python kita.
        print(f"[LAYER 3-4] Header IP dan Port diverifikasi, data diteruskan ke aplikasi.")

        # 3. TRANSLASI DATA (Presentation Layer - Layer 6)
        # Mengubah kembali data bytes biner menjadi string teks bahasa manusia
        pesan_diterjemahkan = data_mentah.decode('utf-8')
        print(f"[LAYER 6] Data didekode/diterjemahkan menggunakan UTF-8.")
        
        # 4. MENAMPILKAN DATA (Application Layer - Layer 7)
        print(f"[LAYER 7] Pesan sukses ditampilkan di layar: '{pesan_diterjemahkan}'")

    conn.close()
    print("\n[LAYER 5] Sesi selesai, koneksi diputus.")
if __name__ == '__main__':
    server_program()