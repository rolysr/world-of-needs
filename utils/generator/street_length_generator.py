import statistics as st

def generate_street_length(): 
    """Generates a normally street size"""
    a=st.NormalDist(98.2661934338953, 32.848353621982426) 
    length = a.samples(1)
    return length[0]