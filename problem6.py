# python quiz game
qustions=(("১.মালিহার বয়স কত?:")
        , ("২.মালিহার জন্মদিন কবে?:"),
          ("৩.মালিহার প্রিয় রং কী:"),
          ("৪.মালিহা কোন দেশে যেতে চায়:"),
          ("৫.মালিহার প্রিয় SUBJECT কি?:"),
          ("৬.মালিহার কোচিং এর বান্ধবির নাম নিচের কোন টি?"),
          ("৭.মালিহার লাস্ট Exam কোন Subject এর?"),
          ("৮.তোমাদের Anniversary কবে?"),
          ("৯.আম্মুর Birthday কবে?"),
          ("১০.আবিরের Cadet এর Written Exam কবে হয়েছিল?"))
Options=(("A.৯ বছর ", "B.৮ বছর","C.১১ বছর", "D.১০ বছর"),
         ("A.১৪/৬/২০১৪" ,"B.১২/৬/২০১৫", "C.১২/৬/২০১৪", "D.১২/৫/২০১৪"),
         ("A.Black" ,"B.Red","C.Pink" ,"D.Blue"),
         ("A.Italy", "B.Dubai" ,"C.Saudi Arab" ,"D.Korea"),
         ("A.Bangla" ,"B.Math" ,"C.English" ,"D.Science"),
         ("A.ঐশী","B.ইচ্ছে","C.বরিসাইল্লা","D.সবগুলো"),
         ("A.Bangla","B.Region","C.Science","D.English"),
         ("A.3/1/2008","B.1/3/2009","C.3/2/2007","D.3/1/2007"),
         ("A.7/7/1979","B.7/7/1989","C.8/7/1987","D.7/8/1979"),
         ("A.2/1/2025","B.5/1/2024","C.5/1/2025","D.1/5/2025"))
Answer=(("C"),("C"),("C"),("D"),("B"),("D"),("B"),("D"),("A"),("C"))
gesses=[]
score=0
qustion_num=0
for qustion in qustions:
    print("------------------------")
    print(qustion)
    for option in Options[qustion_num]:
        print(option)
    gesse=input("Enter your answer(A,B,C,D):").upper()
    gesses.append(gesse)
    if gesse==Answer[qustion_num]:
        score+=1
        print("Correct!")
    else:
         print("Incorrect!")
    qustion_num += 1
print("-------------------")
print("       SCORE       ")
print("-------------------")
result=int(score/len(qustions)*100)
print(f"Your score is:{result}%")
print(f"Correct answer were {Answer}")
print(f"Your guesses were   {gesses}")
