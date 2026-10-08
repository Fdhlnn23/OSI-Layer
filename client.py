import socket

def client_program():
    host = '127.0.0.1' 
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(True, f"[LAYER 5] Sesi terkoneksi ke Server {host}:{port}")

    pesan_mentah = "Halo Pak CEO Adan, ini ada pesan rahasia dari Pak Anaz!"
    print(True, f"[LAYER 5] Data dibuat: '{pesan_mentah}'")


    data_terenkapsulasi = pesan_mentah.encode('utf-8')
    print(f"[LAYER 6] Data diubah ke format Bytes/Biner untuk siap kirim.")

    print("[OSI ALUR] Mengirimkan data (Proses Enkapsulasi berlangsung...)\n")
    client_socket.send(data_terenkapsulasi)

    client_socket.close()
    print("[LAYER 5] Sesi komunikasi ditutup.")

if __name__ == '__main__':
    client_program()
