def chronological_split(rows, train_fraction=.7, validation_fraction=.15):
    """Split ordered records without shuffling future observations backward."""
    if not 0 < train_fraction < 1 or not 0 <= validation_fraction < 1 or train_fraction+validation_fraction >= 1: raise ValueError("invalid fractions")
    n=len(rows); a=int(n*train_fraction); b=a+int(n*validation_fraction)
    return rows[:a], rows[a:b], rows[b:]
