with open("input.txt") as f:
    signal = f.read().strip()
    for i in range(len(signal) - 13):
        window = signal[i:i + 14]
        if len(set(window)) == 14:
            print(i + 14)
            break
