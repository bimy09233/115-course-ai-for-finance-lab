def main() -> None:
    l = 1000
    prime = [1] * (l + 1)
    prime[0] = 0
    prime[1] = 0

    for i in range(2, int(l**0.5) + 1):
        if prime[i]: # 是質數
            for j in range(i * i, l + 1, i): # 從i平方開始看
                prime[j] = 0

    for i in range(l + 1):
        if prime[i]:
            print(i)

if __name__ == "__main__":
    main()