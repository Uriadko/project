import random
import time
import tkinter as tk
from tkinter import messagebox

class Mafia:
    def __init__(self, name):
        self.name = name

    def choose_target(self, players, root):
        self.selected_target = None

        def select_target():
            nonlocal self
            selected_index = listbox.curselection()
            if selected_index:
                self.selected_target = players[selected_index[0]]
                root.destroy()  
                root.quit()     

        root.title("Мафія обирає ціль")
        label = tk.Label(root, text="Оберіть гравця для вбивства!:")
        label.pack()

        listbox = tk.Listbox(root)
        for player in players:
            listbox.insert(tk.END, player)
        listbox.pack()

        button = tk.Button(root, text="Оберіть ціль", command=select_target)
        button.pack()

        root.mainloop()

        return self.selected_target

class Sheriff:
    def __init__(self, name):
        self.name = name

    def inspect(self, players, root):
        self.selected_player = None

        def select_player():
            nonlocal self
            selected_index = listbox.curselection()
            if selected_index:
                self.selected_player = players[selected_index[0]]
                root.destroy() 
                root.quit()     

        root.title("Шериф обирає гравця")
        label = tk.Label(root, text="Оберіть гравця для перевірки!:")
        label.pack()

        listbox = tk.Listbox(root)
        for player in players:
            listbox.insert(tk.END, player)
        listbox.pack()

        button = tk.Button(root, text="Перевірка", command=select_player)
        button.pack()

        root.mainloop()

        return self.selected_player

class Citizen:
    def __init__(self, name):
        self.name = name

    def treat(self, players, root):
        self.selected_doctor = None

        def select_doctor():
            nonlocal self
            selected_index = listbox.curselection()
            if selected_index:
                self.selected_doctor = players[selected_index[0]]
                root.destroy()  
                root.quit()     

        root.title("Мирний житель обирає лікаря")
        label = tk.Label(root, text="Оберіть гравця для лікування!:")
        label.pack()

        listbox = tk.Listbox(root)
        for player in players:
            listbox.insert(tk.END, player)
        listbox.pack()

        button = tk.Button(root, text="Оберіть лікаря", command=select_doctor)
        button.pack()

        root.mainloop()

        return self.selected_doctor

def main():
    players = ["Розалін", "Маркус", "Дафна", "Ерез", "Ноа"]
    sheriff = Sheriff("Sheriff")
    mafia = Mafia("Mafia")
    citizen = Citizen("Мирний житель")
    
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Гра почалась!")

    while len(players) > 2:
        time.sleep(1)
        messagebox.showinfo("Ніч:", "Настала ніч!")
        if isinstance(mafia, Mafia):
            target_window = tk.Toplevel()
            target = mafia.choose_target(players, target_window)
            target_window.destroy() 
            if target:
                messagebox.showinfo("Ніч:", f"{mafia.name} вбиває {target}.")
                if isinstance(target, Sheriff):
                    messagebox.showinfo("Результат:", f"{sheriff.name} був вбитий мафією!")
                    players.remove(sheriff)
                    break
                else:
                    players.remove(target)

        time.sleep(1)
        if isinstance(citizen, Citizen):
            doctor_window = tk.Toplevel()
            doctor = citizen.treat(players, doctor_window)
            doctor_window.destroy()
            if doctor:
                messagebox.showinfo("День:", f"{citizen.name} лікує {doctor}.")

        time.sleep(1)
        messagebox.showinfo("День:", "Настав день!")
        suspect_window = tk.Toplevel()
        suspect = sheriff.inspect(players, suspect_window)
        suspect_window.destroy() 
        messagebox.showinfo("Перевірка:", f"{sheriff.name} перевіряє {suspect}.")
        messagebox.showinfo("Результат:", f"{suspect} - {mafia.name}" if suspect == players[-1] else f"{suspect} - звичайний гравець.")

    if len(players) > 2:
        messagebox.showinfo("Кінець гри:", "Місто виграло!")

if __name__ == "__main__":
    main() 
