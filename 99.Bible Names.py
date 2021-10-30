#To print the Book no of Bible
def oldTestament(oldBookNumber):
    return{
        1: "Genesis",
        2: "Exodus",
        3: "Levicitus",
        4: "Numbers",
        5: "Deutronomy",
        6: "Joshua",
        7: "Judges",
        8: "Ruth",
        9: "I Samuel",
        10: "II Samuel",
        11: "I Kings",
        12: "II Kings",
        13: "I Chronicles",
        14: "II Chronicles",
        15: "Ezra",
        16: "Nehamiah",
        17: "Esther",
        18: "Job",
        19: "Psamls",
        20: "Proverbs",
        21: "Ecclesiates",
        22: "Song Of Solomon",
        23: "Isaih",
        24: "Jermiah",
        25: "Lamentation of Jermiah",
        26: "Ezekial",
        27: "Daniel",
        28: "Osiah",
        29: "Joel",
        30: "Amos",
        31: "Obadiah",
        32: "Jonah",
        33: "Micah",
        34: "Nahum",
        35: "Abakuk",
        36: "Zepaniah",
        37: "Hagai",
        38: "Zaccariah",
        39: "Malgiah",
        
    }.get(oldBookNumber,"Invalid Book Number\nEnter Correct Number.\n")

def newTestament(newBookNumber):
          return{
          1: "Matthew",
          2: "Maark",
          3: "Luke",
          4: "John",
          5: "Acts of The Apostle",
          6: "Romans",
          7: " I Corinthians",
          8: "II Corinthians",
          9: "Galatians",
          10: "Ephesians",
          11: "Philipians",
          12: "Colessians",
          13: "I Thessalonians",
          14: "II Thessalonians",
          15: "I Timothy",
          16: "II Timothy",
          17: "Titus",
          18: "Philomon",
          19: "Hebrew",
          20: "James",
          21: "I Peter",
          22: "II Peter",
          23: "I John",
          24: "II John",
          25: "III John",
          26: "Judah",
          27: "Revelation To John"
          }.get(newBookNumber,"Give a Correct Book number\n")

whichTestament=int(input("Which Testament? Enter '1'-Old or '2'-New\n"))
if(whichTestament==1):
          BookNumber=int(input("Enter The Book Number\n"))
          print(oldTestament(BookNumber))
elif(whichTestament==2):
          BookNumber=int(input("Enter The Book Number\n"))
          print(newTestament(BookNumber))
else:
          print("Choose '1'-Old or '2'-New\n")
