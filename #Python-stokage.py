import shutil
total, used, free = shutil.disk_usage("/")
print ("espace disque total %d Go "% (total//(2**30)))
print("Espace disque utilisé: %d Go" % (used // (2**30)))
print("Espace disque disponible: %d Go" % (free // (2**30)))
