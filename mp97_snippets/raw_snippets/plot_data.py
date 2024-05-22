for reading_set in reading_sets:
    ph.plot_data_static(
        reading_set,
        known_slides=known_slides,
        critical_points=critical_points
    )

a_utils.summarize_results()