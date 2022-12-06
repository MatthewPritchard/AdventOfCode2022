with open("input.txt") as f:
    signal = f.read().strip()
    for i in range(len(signal) - 3):
        window = signal[i:i + 4]
        if len(set(window)) == 4:
            print(i + 4)
            break
