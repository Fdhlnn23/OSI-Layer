import socket

def server_program():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("[SERVER READY] Menunggu koneksi masuk di port 5000...")

    conn, address = server_socket.accept()
    print(f"[LAYER 5] Sesi terhubung dengan klien dari alamat: {address}")

    while True:
        data_mentah = conn.recv(1024)
        if not data_mentah:
           break

        print("\n[OSI ALUR] Data fisik diterima! Mengawali proses Dekapsulasi...")
        print(f"[LAYER 1-2] Data biner mentah yang ditangkap: {data_mentah}")

        print(f"[LAYER 3-4] Header IP dan Port diverifikasi, data diteruskan ke aplikasi.")

        pesan_diterjemahkan = data_mentah.decode('utf-8')
        print(f"[LAYER 6] Data didekode/diterjemahkan menggunakan UTF-8.")
        
        print(f"[LAYER 7] Pesan sukses ditampilkan di layar: '{pesan_diterjemahkan}'")

    conn.close()
    print("\n[LAYER 5] Sesi selesai, koneksi diputus.")
if __name__ == '__main__':
    server_program()