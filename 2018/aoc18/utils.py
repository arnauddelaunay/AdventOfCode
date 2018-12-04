def read_input(day, split_lines=True, test=False):
  suf = "_test" if test else ""
  filename = "data/%d%s.txt" % (day, suf)
  inp = open(filename)
  return inp.read() if not split_lines else inp.readlines() 
