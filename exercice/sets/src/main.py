def gerer_club_lecture(membres_actuels, personnes_interessees):

    return set(membres_actuels + personnes_interessees)



if __name__ == '__main__':
  print(gerer_club_lecture(["Alice", "Bob"], ["Bob", "Charlie"]))
