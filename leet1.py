

brojevi = [2,11,7,15,3,6]
res = 9
# indexi = -1
# indexj = -1
# for i in(brojevi):
#     indexi +=1
#     for j in(brojevi):
#         indexj += 1
#         if(i + j == res):
#             print(f" index i {indexi} i index j {indexj} , brojevi  {i} {j}")
    
    
for i in range(len(brojevi)):
    for j in range(len(brojevi)):
        if(brojevi[i] + brojevi[j] == res):
            print(i, j)