t = int(input("Enter total seconds: "))
        y = t // 31536000; t %= 31536000
        d = t // 86400; t %= 86400
        h = t // 3600; t %= 3600
        m = t // 60; s = t % 60
        print(f"Years: {y}, Days: {d}, Hours: {h}, Minutes: {m}, Seconds: {s}")

