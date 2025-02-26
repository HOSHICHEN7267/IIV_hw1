import math

def calculate_Bi(i, msg_list):
    lower_equal_priority = [msg for msg in msg_list if msg.p >= msg_list[i].p]
    Bi = max(msg.c for msg in lower_equal_priority)
    return Bi

def cal_rhs(i, msg_list, tau):
    higher_priority = [msg for msg in msg_list if msg.p < msg_list[i].p]

    Bi = calculate_Bi(i, msg_list)

    sum_wtime = sum(math.ceil((Bi + tau) / msg.t) * msg.c for msg in higher_priority)

    rhs = Bi + sum_wtime

    return rhs

def cal_ri(i, msg_list, tau, qi):
    rhs = cal_rhs(i, msg_list, tau)

    if rhs + msg_list[i].c > msg_list[i].t:
        return -1
    elif rhs == qi:
        return qi + msg_list[i].c
    else:
        return cal_ri(i, msg_list, tau, rhs)

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
            tau = float(data[1].strip())

            msg_list = list()

            for line in data[2:]:
                values = line.strip().split()
                msg_list.append(message(int(values[0]), float(values[1]), int(values[2])))

            for i in range(msg_len):
                Bi = calculate_Bi(i, msg_list)
                ri = cal_ri(i, msg_list, tau, Bi)
                print(ri)
                
    except FileNotFoundError:
        print("input.dat file not found.")
    except ValueError:
        print("Error in converting data.")