def find_max_min(listing):
    listing.sort()
    if listing[0]== listing[-1]:
        return [len(listing)]
    else:
        return [listing[0], listing[-1]]
