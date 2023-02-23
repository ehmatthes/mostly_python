import random

def get_flips(num_flips=10):
    """Return a random sequence of coin flips."""
    outcomes = ('H', 'T')
    return random.choices(outcomes, k=num_flips)

def get_best_sequence(flips, threshold):
    """Find the sequence with the highest percentage
    of heads, with a length above the threshold.

    Returns:
    - Sequence with highest heads percentage.
    - Percentage heads for that sequence.
    """
    best_percentage = -1.0

    # Loop over all slices above the threshold size.
    for start_index in range(len(flips)-threshold+1):
        for end_index in range(start_index+threshold, len(flips)+1):
            current_slice = flips[start_index:end_index]
            percent_heads = current_slice.count("H") / len(current_slice)

            # If this is the best sequence, store it.
            if percent_heads > best_percentage:
                best_percentage = percent_heads
                best_sequence = current_slice

    return best_sequence, best_percentage*100

# Generate flips.
all_flips = get_flips(num_flips=3_000)
print(f"Generated {len(all_flips):,} flips.")

# Find best sequence.
print("\nAnalyzing flips...")
best_sequence, percentage = get_best_sequence(all_flips, threshold=100)

print(f"\nThe best sequence has {len(best_sequence):,} flips in it.")
print(f"It consists of {percentage:.1f}% heads.")
