class Combine:
    d = {}

    def calc(k: int, n: int) -> int:
        if k == 0 or k == n:
            return 1

        if (k, n) not in Combine.d:
            Combine.d[k, n] = Combine.calc(k-1, n-1) + Combine.calc(k, n-1)

        return Combine.d[k, n]