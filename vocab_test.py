import random

def open_dict(path):
  opened_dict = {} 
  with open(path, "r", encoding='utf-8') as file:
    for line in file:
        key, val = line.strip().split(" : ")
        value = val.strip().split(", ")
        opened_dict[key] = value
  return(opened_dict)
  
def main():
  selected_dict = "dict_1.txt"
  test_dict = open_dict(selected_dict)
  
  mode = input("""Select one of these options:
1 for German -> Czech
2 for Czech -> German
3 for both German -> Czech and Czech -> German
Pick the option:""")
  print(test_dict)
  


if __name__ == "__main__":
  main()
