class perfectsq:
    def __init__(self):
        self.a=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x*x

        else:
            raise StopIteration
it=perfectsq()
while True:
    print(it.__next__())

