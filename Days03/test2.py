donnees_clients = [("ID_01", 1500), ("ID_02", 0), ("ID_03", 4200)]
annuaire_ca = {client_id: ca for client_id, ca in donnees_clients if ca > 0}
print(annuaire_ca)