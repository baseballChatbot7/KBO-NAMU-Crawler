from glob import glob
#%%
def preprocessing(file_path):
  f = open(file_path, 'r')
  lines = f.readlines()
  f.close()
  print(file_path)
  while True:
    lines, start = delete_team(lines)
    if start == -1:
        break 

  f = open(file_path, 'w')
  for result in lines:
    if result is None:
      continue
    f.write(result.strip()+'\n')
  f.close()
  return


# %%
def delete_team(lines):
    start, end = -1, -1
    for i, line in enumerate(lines):
        if 'Time to Win!연고지를 부산광역시로' in line:
            start = i - 1
            end = i + 265
            break
        elif 'TEAM DOOSAN! 2021KBO 리그의 프로야구단으로' in line:
            start = i - 1
            end = i + 443
            break
        elif 'KBO 리그의 프로야구단. 연고지는 광주광역시.' in line:
            start = i - 1
            end = i + 373
            break
        elif 'One Team, One Dream! V1 HEROESKBO 리그의 프로야구단.' in line:
            start = i - 1
            end = i + 408
            break
        elif '한화그룹 광고 - 한화 이글스편 불꽃 한화, 투혼 이글스!' in line:
            start = i - 1
            end = i + 392
            break
        elif '패기의 SK! 승리의 와이번스! 2000년 창단 당시부터' in line:
            start = i - 1
            end = i + 683
            break
        elif 'KBO 리그에 참여하고 있는 프로야구단. 연고지는 경기도 수원시이며,' in line:
            start = i - 1
            end = i + 153
            break
        elif '2021년 삼성 라이온즈 캐치프레이즈NEW BLUE! NEW LIONS' in line:
            start = i - 1
            end = i + 489
            break
        elif '무적 LG, 끝까지 TWINS!' in line:
            start = i - 1
            end = i + 257
            break   
        elif 'New ChangwonNew ChallengeNew ChampionKBO 리그의 프로야구단이며 연고지는 경상남도 창원시.' in line:
            start = i - 1
            end = i + 532
            break   
        elif 'KBO 리그에 있었던 프로야구단. 연고지는 인천광역시 & 경기도 & 강원도' in line:
            start = i - 1
            end = i + 266
            break      
        elif '대한민국에 존재했던 한국프로야구 소속 구단으로 최초의 인천 연고 구단이다.' in line:
            start = i - 1
            end = i + 152
            break 
        elif '세상에 없던 프로야구단의 시작!KBO 리그 소속 프로야구단.' in line:
            start = i - 1
            end = i + 109
            break  
           

    if start == -1:
        return lines, start
    else:
        del lines[start:end]
        return lines, start
        
# %%
# %%
if __name__ == '__main__':
  file_list = glob('/Users/jb/workspace/webscrapping/player/*.txt')
  for file in file_list:  
    preprocessing(file)