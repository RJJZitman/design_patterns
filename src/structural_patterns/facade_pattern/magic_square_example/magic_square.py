from low_level import RowGenerator, Splitter, Verifier


class MagicSquareGenerator:
    @staticmethod
    def generate(size):
        g = RowGenerator()
        s = Splitter()
        v = Verifier()
        while True:
            square = []
            for x in range(size):
                square.append(g.generate(size))
            if v.verify(s.split(square)):
                break
        return square
