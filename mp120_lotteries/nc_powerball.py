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

breakpoint()