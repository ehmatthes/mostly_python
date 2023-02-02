winners = ["elizabeth", "ryan", "kayla"]

print("The winners are:")
for index, winner in enumerate(winners):
    place = index + 1
    print(f"{place}. {winner.title()}")