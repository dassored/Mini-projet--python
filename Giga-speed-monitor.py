#speed-monitor
import psutil
import tkinter as tk

# Fonction pour mettre à jour l'affichage des statistiques de bande passante
def update_bandwidth_stats():
    # Récupération des statistiques de bande passante
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    packets_sent = net_io_counters.packets_sent
    packets_recv = net_io_counters.packets_recv

    # Calcul des débits en Mbps
    tx_speed = round(bytes_sent / 1000000 * 8, 2)
    rx_speed = round(bytes_recv / 1000000 * 8, 2)

    # Mise à jour de l'interface graphique avec les statistiques
    tx_label.config(text=f"Upload: {tx_speed} Mbps\nPackets: {packets_sent}")
    rx_label.config(text=f"Download: {rx_speed} Mbps\nPackets: {packets_recv}")

    # Programmation d'une nouvelle mise à jour dans 1 seconde
    root.after(1000, update_bandwidth_stats)

# Initialisation de l'interface graphique
root = tk.Tk()
root.title("Bande passante")

# Création des widgets d'affichage des statistiques
tx_label = tk.Label(root, font=("Helvetica", 16))
rx_label = tk.Label(root, font=("Helvetica", 16))
tx_label.pack(pady=10)
rx_label.pack(pady=10)

# Lancement de la surveillance de la bande passante
update_bandwidth_stats()

# Boucle principale de l'interface graphique
root.mainloop()


