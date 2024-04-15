import random

class Game:
    def __init__(self):
        self.nyawa = 5
        self.pertanyaan_jawaban = [
            {
                "pertanyaan": "Ada 10 ikan di dalam akuarium, 2 mati, 4 berenang pergi, dan 3 datang kembali. Berapa jumlah ikan di dalam akuarium?",
                "jawaban": "10"
            },
            {
                "pertanyaan": "Apa yang bisa berdiri tanpa kaki dan duduk tanpa bokong?",
                "jawaban": "topi"
            },
            {
                "pertanyaan": "Apa yang bisa membuat orang menangis saat tertawa?",
                "jawaban": "bawang"
            },
            {
                "pertanyaan": "Apa yang ada di ujung langit?",
                "jawaban": "huruf t"
            },
            {
                "pertanyaan": "Apa yang menjadi semakin kecil saat semakin banyak ditambahkan?",
                "jawaban": "lubang jarum"
            }
        ]

    def perkenalan(self):
        print("Hello, Welcome to the game!\n")
        self.nama = input("What's your name? ")
        self.umur = int(input("Hello, {}, What's your age? ".format(self.nama)))
        if self.umur > 12:
            self.mulai_main()
        else:
            print("Sorry, you are not yet old enough. See you")

    def mulai_main(self):
        playing = input("You are old enough to play! Do you want to start play? Yes/No ")
        if playing.upper() == "YES":
            print("Let's Go!")
            self.main()
        else:
            print("It's okay, See you")

    def main(self):
        print("Anda diberikan 5 nyawa untuk menjawab pertanyaan pada game ini. \nJika Anda salah menjawab maka nyawa Anda berkurang 1. \nPastikan Anda dapat menjawab semua pertanyaan untuk menang.")
        print("----------------------------------------------------------------------------------------")
        pertanyaan_jawaban_acak = random.sample(self.pertanyaan_jawaban, len(self.pertanyaan_jawaban))
        for pertanyaan_jawaban in pertanyaan_jawaban_acak:
            pertanyaan = pertanyaan_jawaban["pertanyaan"]
            jawaban = pertanyaan_jawaban["jawaban"]
            jawaban_pengguna = input(pertanyaan)
            if jawaban_pengguna.lower() == jawaban.lower():
                print("Benar!")
            else:
                print("Salah!")
                self.nyawa -= 1
                print("Nyawa Anda sisa", self.nyawa)
        self.hasil_akhir()

    def hasil_akhir(self):
        if self.nyawa != 0:
            print("Anda menang!")
        else:
            print("Anda kalah! Coba lagi ya")


if __name__ == "__main__":
    game = Game()
    game.perkenalan()