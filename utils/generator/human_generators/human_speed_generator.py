import statistics as st

def generate_human_speed():
    """
        A method for generating human speed. 
        This is given in m/min
        Find more information in https://www.researchgate.net/figure/The-walking-speed-of-pedestrians-is-distributed-normally-with-an-estimated-mean-of-134_fig4_286071735
        Create a Normal Distribution Class instance
        Generate a sample
    """
    a=st.NormalDist(1.34, 0.26) 
    speed = a.samples(1)
    return speed[0]