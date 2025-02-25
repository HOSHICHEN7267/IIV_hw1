def find_Bi(pi, msg_list):
    max = 0
    for msg in msg_list:
        if msg.p < pi and msg.c > max:
            max = msg.c
    return max

def sum_wtime(i):
    return i

def cal_Qi(msg_list, tau):
    return find_Bi(msg_list) + sum_wtime(msg_list, tau)

class message:
    def __init__(self, p, c, t):
        self.p = p
        self.c = c
        self.t = t

if __name__ == "__main__":

    try:
        with open("input.dat", "r") as file:
            data = file.readlines()
            msg_len = int(data[0].strip())
            tau = int(data[1].strip())

            msg_list = list()

            for line in data[2:]:
                values = line.strip().split()
                msg_list.append(message(int(values[0]), float(values[1]), int(values[2])))

    except FileNotFoundError:
        print("input.dat file not found.")
    except ValueError:
        print("Error in converting data.")