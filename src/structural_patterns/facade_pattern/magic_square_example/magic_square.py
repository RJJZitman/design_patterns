from low_level import RowGenerator, Splitter, Verifier


class MagicSquareGenerator:
    """Facade to generate a magic square by utilising the RowGenerator, Splitter, Verifier"""
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
