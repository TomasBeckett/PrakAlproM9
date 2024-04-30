def angkaMaxdanMin():
    angka = []

    while True:
        input_angka = input("Masukan data Angka menggunakan (,) atau Ketik 'done' untuk selesai : ")
    
        if input_angka.lower() == 'done':
            break

        angka.extend(input_angka.split(','))

    angka = [float(x) for x in angka]

    if angka:
        print("Nilai maks:", max(angka))
        print("Nilai min:", min(angka))
    else:
        print("None")

angkaMaxdanMin()



