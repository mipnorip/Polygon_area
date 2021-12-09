def main() -> tuple:
    data = []
    s = 0

    with open('area.in', 'r') as file:
        for i in file.readlines():
            data.append(i.split())

    N = int(data.pop(0)[0])

    for i in range(0, len(data)-1):
        s += int(data[i][0]) * int(data[i+1][1]) - \
            int(data[i+1][0]) * int(data[i][1])
        if i+2 == N:
            s += int(data[N-1][0]) * int(data[0][1]) - \
                int(data[0][0]) * int(data[N-1][1])

    s = abs(s/2)

    with open('area.out', 'w') as file:
        file.write(str(s))

    return (N, data, s)

if __name__ == "__main__":
    main()