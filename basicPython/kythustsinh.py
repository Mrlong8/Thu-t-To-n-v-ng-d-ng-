

def binh_phuong_gen(n):
    for i in range(n):
        yield i *i

if __name__ == '__main__':
    bp = binh_phuong_gen(10)
    t = next(bp)
    print(t)
    t = next(bp)
    print(t)