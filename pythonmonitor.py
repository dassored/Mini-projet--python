import psutil
import time

while True :
    # Surveillance de la consommation de CPU et de mémoire
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent


    # Si la consommation est supérieure à un seuil, alerter
    if cpu_percent > 80 or mem_percent> 80 :
        print ("ALERTE : Consommation de CPU ou de mémoire élevée")
        # Ici, on pourrait ajouter des actions supplémentaires, comme envoyer un email ou un message d'alerte
    else :  
        print(f"CPU :{cpu_percent}% / Mémoire : {mem_percent}%")

    # Attendre avant de recommencer la surveillance 
    time.sleep(10)



