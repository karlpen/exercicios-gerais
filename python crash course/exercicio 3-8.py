# exercicio 3-8

locations = ["Tokio", "Bangkok", "Shanghai", "Goa"]
print (f"Lista normal: {locations}")
print (f"Lista em ordem (sem alterar): {sorted(locations)}")
print (f"Lista normal (de novo): {locations}")
print (f"Lista em ordem reversa (sem alterar): {sorted(locations, reverse= True)}")
print (f"Lista normal (de novo): {locations}")
locations.reverse()
print (f"Lista alterada: {locations}")
locations.reverse()
print (f"Lista voltou ao normal: {locations}")
locations.sort()
print (f"Lista em ordem definitiva: {locations}")
locations.sort(reverse= True)
print (f"Lista em ordem reversa definitiva: {locations}")



