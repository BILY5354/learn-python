


a = [36.59 ,36.80 ,36.94 ,35.94 ,37.29 ,36.69 ,36.51 ,36.90 ,36.69 ]

sum=0
for i in a:
    sum+=i
print(round(sum/len(a),2))
print(round(20480/(sum/len(a)),2))