import os


def read_input(day, split_lines=True, test=False, root_path=""):
  suf = "_test" if test else ""
  filename = os.path.join(root_path, "data/%d%s.txt" % (day, suf))
  inp = open(filename)
  return inp.read() if not split_lines else inp.readlines() 
