import psutil
import tkinter as tk

# Fonction pour récupérer les informations sur les connexions des programmes
def get_process_connections():
    connections = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            conns = psutil.Process(pid).connections()
            for conn in conns:
                connections.append({'pid': pid, 'name': name, 'status': conn.status,
                                     'local_address': conn.laddr, 'remote_address': conn.raddr})
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return connections

# Fonction pour mettre à jour l'affichage des connexions
def update_connections():
    connections = get_process_connections()
    # Effacement des anciennes données
    conn_listbox.delete(0, tk.END)
    # Ajout des nouvelles données
    for conn in connections:
        conn_listbox.insert(tk.END, f"{conn['pid']} - {conn['name']}: {conn['status']} - {conn['local_address']} <-> {conn['remote_address']}")
    # Programmation d'une nouvelle mise à jour dans 1 seconde
    root.after(1000, update_connections)

# Initialisation de l'interface graphique
root = tk.Tk()
root.title("Monitoring des connexions")

# Création de la liste des connexions
conn_listbox = tk.Listbox(root, font=("Helvetica", 10), width=100, height=40)
conn_listbox.pack(pady=10)

# Lancement de la surveillance des connexions
update_connections()

# Boucle principale de l'interface graphique
root.mainloop()

    
    

    

    





        
    

