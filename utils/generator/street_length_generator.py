import statistics as st

def generate_street_length(): 
    """Generates a normally street size"""
    a=st.NormalDist(70, 30) 
    length = a.samples(1)
    return length[0]