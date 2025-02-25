import math

def cal_rhs(i, msg_list, tau):
    higher_priority = list()
    lower_equal_priority = list()

    # Split the list into higher and lower/equal priority
    for msg in msg_list:
        if msg.p < msg_list[i].p:
            higher_priority.append(msg)
        else:
            lower_equal_priority.append(msg)

    # Calculate Bi
    Bi = 0
    for msg in lower_equal_priority:
        if msg.c > Bi:
            Bi = msg.c

    # Calculate the sum of waiting time
    sum_wtime = 0
    for msg in higher_priority:
        sum_wtime += math.ceil((Bi + tau) / msg.t) * msg.c

    rhs = Bi + sum_wtime

    return rhs

def cal_ri(i, msg_list, tau, qi):

    rhs = cal_rhs(i, msg_list, tau)

    if rhs + msg_list[i].c > msg_list[i].t:
        return -1
    elif rhs == qi:
        return qi + msg_list[i].c
    else:
        cal_ri(i, msg_list, tau, rhs)


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
                ri = cal_ri(i, msg_list, tau, )
                print(ri)
                
    except FileNotFoundError:
        print("input.dat file not found.")
    except ValueError:
        print("Error in converting data.")