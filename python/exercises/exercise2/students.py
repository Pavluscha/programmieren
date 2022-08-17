students = {"student_1" : 13 , "student_2" : 17 , "student_3" : 9 , "student_4" : 15 , 
             "student_5" : 8 , "student_6" : 14 , "student_7" : 16 , "student_8" : 12 , 
             "student_9" : 13 , "student_10" : 15 , "student_11" : 14 , "student_112" : 9 , 
             "student_13" : 10 , "student_14" : 12 , "student_15" : 13 , "student_16" : 7 ,
             "student_17" : 12 , "student_18" : 15 , "student_19" : 9 , "student_20" : 17 ,}

good_students = {}
bad_students = {}

for x, y  in students.items():
  if y >= 10:
      good_students.update({x: y})
  else:
      bad_students.update({x: y})

print(good_students)
print(bad_students)