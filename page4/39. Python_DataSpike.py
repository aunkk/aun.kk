"""DataSpike"""
def main_loop(i, data_spare=None):
    """loop input for 8 times and checking which one is maximum"""
    if i <= 3:
        data = int(input())
        if i == 1:
            data_spare = data
        data_spare = compare(data_spare, data)
        
    else:
        print(data_spare)

def compare(data_1, data_2):
    """comparing to find maximum number"""
    if data_1 < data_2:
        return data_2
    return data_1

main_loop(1)
