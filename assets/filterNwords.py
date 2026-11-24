def main():
  howManyLetters = 5
  readFile = "lithuanian-words-list.txt"
  writeFileName = f"{howManyLetters}-letter-lithuanian-words-list.txt"

  validWords = []
  with open(readFile, "r", encoding="utf-8") as fr:
    for line in fr:
      word = line.strip()
      if len(word) == howManyLetters and word[0].islower():
        validWords.append(word)
  
  with open(writeFileName, "w", encoding="utf-8") as fw:
    for word in validWords:
      fw.write(f"{word}\n")
main()