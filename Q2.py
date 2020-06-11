def find_char(inputstring):
  n = len(inputstring)//3
  char_dict = {}
  for ele in inputstring:
    if ele not in char_dict.keys():
      char_dict[ele]=0
    if ele in char_dict.keys():
      char_dict[ele]=char_dict[ele]+1
  s = ""
  for char in char_dict.items():
    if(char[1]<n):
      s=s+char[0]
  return s

print(find_char("GGGGGGGVNG"))