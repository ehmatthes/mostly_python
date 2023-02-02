winners = ["elizabeth", "ryan", "kayla"]

print("The winners are:")
for i, winner in [(i, winner) for i, winner in enumerate(winners)]:
    place = i + 1
    print(f"{place}. {winner.title()}")