import sys

if __name__ == "__main__":
    arg = len(sys.argv)
    stock = []
    print("=== Player Score Analytics ===")
    if arg == 1:
        print("No scores provided. Usage: python3", end=" ")
        print("ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            for i in sys.argv:
                if i != sys.argv[0]:
                    i = int(i)
                    stock.append(i)
            print(f"Scores processed: {stock}")
            print(f"Total players: {arg - 1}")
            print(f"Total score: {sum(stock)}")
            print(f"Average score: {sum(stock) / (arg - 1)}")
            print(f"High score: {max(stock)}")
            print(f"Low score: {min(stock)}")
            print(f"Score range: {max(stock) - min(stock)}")
        except ValueError:
            print("ValueError : You can't enter other thing than one", end="")
            print("numeric value")
