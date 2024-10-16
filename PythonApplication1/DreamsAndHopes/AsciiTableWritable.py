class ASCII:
    def __init__(self):
        self.asciitable = ""
        self.filepath = ""
        pass

    def create_ascii_table(self):
        unprintable = {0: "nul",
               1: "soh",
               2: "stx",
               3: "etx",
               4: "eot",
               5: "enq",
               6: "ack",
               7: "bel",
               8: "bs",
               9: "ht",
               10: "nl",
               11: "vt",
               12: "np",
               13: "cr",
               14: "so",
               15: "si",
               16: "dle",
               17: "dc1",
               18: "dc2",
               19: "dc3",
               20: "dc4",
               21: "nak",
               22: "syn",
               23: "etb",
               24: "can",
               25: "em",
               26: "sub",
               27: "esc",
               28: "fs",
               29: "gs",
               30: "rs",
               31: "us",
               32: "sp",
               127: "del"}

        self.asciitable = '='*51 + '\n' + "|".join(["Char Dec Hex"]*4) + '\n' + '-'*51 + '\n'

        for i in range(32):
            for j in range(4):
                self.asciitable += "%-5s%3d %2x " %(("(%s)" %unprintable[i+j*32] if i+j*32 in unprintable else " %c" %chr(i+j*32)), i+j*32, i+j*32)
                self.asciitable += '\n' if j==3 else '|'

    def debug_print(self):
        print(self.asciitable)

    def write_file(self, path):
        self.filepath = path
        f = open(self.filepath, "w")
        f.write(self.asciitable)
        f.close()

        print("Successfully wrote into a file!")

    def print_from_file(self, path):
        with open(path, "r") as f: 
            for i in f: print(i, end="")





