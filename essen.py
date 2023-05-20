essen_dict = {
            "Obst": "Birne und apfel",
            "sßigkeit": " Pickup,Knoppers",
            "mittagessen" : "Hünchen",
            "Frühstück" : "Rührei mit Käse und sucuk",
            "Abendessen": "Burger",
            "Gemüse":  "Gurke",
            "vitamin": "Tee mit petersillie",
            }

word = input("Ben dün ne yedim???): ")
        
if word in essen_dict.keys():
    print(essen_dict[word])
else:
    print("Bilmiyorum")
