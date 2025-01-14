import random

def playgame():
    # Inisialisasi nyawa
    player_lives = 3
    bot_lives = 3

    print("Selamat datang di game Batu, Gunting, Kertas!")
    print("Kamu dan bot masing-masing memiliki 3 nyawa. Jika nyawa salah satu habis, permainan selesai.")

    # Loop permainan selama nyawa masih ada
    while player_lives > 0 and bot_lives > 0:
        choices = ["Batu", "Gunting", "Kertas"]
        bot_choice = random.choice(choices)

        player_choice = input("Masukkan pilihan Anda (Batu, Gunting, Kertas): ").capitalize()

        # Validasi input player
        if player_choice not in choices:
            print("Pilihan tidak valid. Silakan pilih antara Batu, Gunting, atau Kertas.")
            continue

        print("Kamu memilih:", player_choice)
        print("Bot memilih:", bot_choice)

        # Logika permainan
        if bot_choice == player_choice:
            print("Hasilnya seri!")
        elif (bot_choice == "Batu" and player_choice == "Gunting") or \
             (bot_choice == "Kertas" and player_choice == "Batu") or \
             (bot_choice == "Gunting" and player_choice == "Kertas"):
            print("Kamu kalah!")
            player_lives -= 1
        else:
            print("Kamu menang!")
            bot_lives -= 1

        # Tampilkan nyawa saat ini
        print(f"Nyawa kamu: {player_lives}, Nyawa bot: {bot_lives}")
        print("------------------------------")

    # Cek siapa pemenangnya
    if player_lives == 0:
        print("Game over! Bot menang.")
    else:
        print("Selamat! Kamu menang melawan bot.")

# Jalankan game
playgame()