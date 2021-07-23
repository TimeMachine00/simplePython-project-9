print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to max value picking")


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)





g = 0

for i in student_scores:
  if i>g:
    g = i
print(f"the highest score in the list is {g}")
print()
but1 = print(input("press enter for bye"))