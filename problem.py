class Problem:
    def __init__(self, statement, data, nrPasiUnu, nrPasiDoi, nrPasiTrei):
        self.statement = statement
        self.data = data
        self.nrPasiUnu = nrPasiUnu
        self.nrPasiDoi = nrPasiDoi
        self.nrPasiTrei = nrPasiTrei

    def solve(self):
        raise NotImplementedError

    def __str__(self):
        return self.statement