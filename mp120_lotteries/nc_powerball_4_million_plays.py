from random import randint

def get_ticket(ticket_size=5, max_value=69):
    """Get a ticket of ticket_size numbers.
    Numbers are picked from 1 through max_value).
    """
    ticket = []

    while len(ticket) < ticket_size:
        pulled_number = randint(1, max_value)

        # Don't reuse numbers.
        if pulled_number in ticket:
            continue

        ticket.append(pulled_number)

    ticket.sort()
    return ticket

def check_ticket(ticket, winning_draw):
    """Find out how many numbers matched."""
    return len(
        [num for num in ticket if num in winning_draw])


bd_ticket = get_ticket(5, 31)
quick_pick = get_ticket()
print(f"Birthday ticket: {bd_ticket}")
print(f"Quick Pick: {quick_pick}")

# Simulate a number of drawings.
bd_results = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
qp_results = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

num_draws = 1_000_000
for _ in range(num_draws):
    winning_draw = get_ticket()

    matches = check_ticket(bd_ticket, winning_draw)
    bd_results[matches] += 1

    matches = check_ticket(quick_pick, winning_draw)
    qp_results[matches] += 1

# Show results.
print(f"\nResults for {num_draws:,} drawings:")
print("\t\tBirthday\tQuick Pick")
for num in bd_results.keys():
    print(f"Match {num}:\t{bd_results[num]:,}\t\t{qp_results[num]:,}")