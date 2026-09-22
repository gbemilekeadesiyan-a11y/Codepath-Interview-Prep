"""def lineup(artists, set_times):
    result = {} 
    for i in range(len(artists)):
        result[artist[i]] = set_times[i]
    return result"""  


"""def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {"message": "Artist not found"}"""
    
"""def total_sales(ticket_sales):
    total = 0
    for value in ticket_sales.values():
        total += value
    return total"""

"""def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}  
    
    for artist in venue1_schedule:
        if artist in venue2_schedule:  
            if venue1_schedule[artist] == venue2_schedule[artist]:  
                conflicts[artist] = venue1_schedule[artist]
    
    return conflicts
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))"""  



"""def best_set(votes):
    vote_counts = {}
    
    for artist in votes.values():  
        if artist in vote_counts:
            vote_counts[artist] += 1
        else:
            vote_counts[artist] = 1
    
    return max(vote_counts, key = vote_counts.get)  
    
    """





