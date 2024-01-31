
import os
import time

file=os.path.abspath(input("파일 경로 입력:"))
print(file)

song=[]
score=0

f=open(file,"r")
lines=f.readlines()
for line in lines:
    line=line.strip()
    song.append(line)
f.close()

start_time=time.time()

for i in range(0,len(song)):
    print(song[i])
    answer=input()
    if song[i]==answer:
        score+=1

end_time=time.time()
total=end_time-start_time


print(f"{total:.4}초 동안 {len(song)}개의 문장 중에서 {score}개 맞춤")


