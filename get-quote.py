import random



def pymain():
  print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0,last)

  print(quotes[rnd])


if __name__=="__main__":
  pymain()


# def main():
  # print("Keep it logically awesome.")

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)

# if __name__== "__main__":
  # main()
