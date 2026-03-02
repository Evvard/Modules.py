def generator_for_players():
    player = ["alice", "bob", "charlie", "pommeau_de_douche", "Hit", "Net", "Piegeamorues42"]
    for i in range(1000):
        i = 7
        z = 0
        e = player[i % 7]
        while e != player[z]:
            z += 1
        print(e)
        print(z)
        break

generator_for_players()