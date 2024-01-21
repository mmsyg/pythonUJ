import tkinter as tk
import random

def narysuj_oczka(canvas, oczka):
    canvas.delete("all")  # Czyści płótno przed narysowaniem nowych oczek
    rozmiar = 200  # Rozmiar kostki
    odstep = rozmiar // 5  # Odległość pomiędzy oczkami

    # Rysowanie ramki kostki
    canvas.create_rectangle(10, 10, rozmiar - 10, rozmiar - 10, outline="black", width=5)

    # Koordynaty środkowych oczek
    srodek_x = rozmiar // 2
    srodek_y = rozmiar // 2

    # Koordynaty rogów
    lewy_gorny = (odstep, odstep)
    prawy_gorny = (rozmiar - odstep, odstep)
    lewy_dolny = (odstep, rozmiar - odstep)
    prawy_dolny = (rozmiar - odstep, rozmiar - odstep)

    # Rysowanie oczek w zależności od wyniku
    if oczka in {1, 3, 5}:
        canvas.create_oval(srodek_x - 15, srodek_y - 15, srodek_x + 15, srodek_y + 15, fill="black")
    if oczka in {2, 3, 4, 5, 6}:
        canvas.create_oval(lewy_gorny[0] - 15, lewy_gorny[1] - 15, lewy_gorny[0] + 15, lewy_gorny[1] + 15, fill="black")
        canvas.create_oval(prawy_dolny[0] - 15, prawy_dolny[1] - 15, prawy_dolny[0] + 15, prawy_dolny[1] + 15, fill="black")
    if oczka in {4, 5, 6}:
        canvas.create_oval(prawy_gorny[0] - 15, prawy_gorny[1] - 15, prawy_gorny[0] + 15, prawy_gorny[1] + 15, fill="black")
        canvas.create_oval(lewy_dolny[0] - 15, lewy_dolny[1] - 15, lewy_dolny[0] + 15, lewy_dolny[1] + 15, fill="black")
    if oczka == 6:
        canvas.create_oval(srodek_x - 15, odstep - 15, srodek_x + 15, odstep + 15, fill="black")
        canvas.create_oval(srodek_x - 15, rozmiar - odstep - 15, srodek_x + 15, rozmiar - odstep + 15, fill="black")

def rzut_kostka():
    wynik = random.randint(1, 6)
    narysuj_oczka(canvas_kostki, wynik)

# Tworzenie okna głównego
okno = tk.Tk()
okno.title("Symulator rzutu kostką")
okno.geometry("800x600")

# Tworzenie płótna dla kostki
canvas_kostki = tk.Canvas(okno, width=200, height=200)
canvas_kostki.pack()

# Tworzenie przycisku
przycisk_rzutu = tk.Button(okno, text="Rzuć kostką", command=rzut_kostka)
przycisk_rzutu.pack()

# Uruchomienie aplikacji
okno.mainloop()
