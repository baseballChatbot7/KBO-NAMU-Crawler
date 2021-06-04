# %%
from glob import glob
from tqdm import tqdm
import re 
import kss
# 1. [] 제거
# 2. ... 제거
# 3. (.) 제거
# 4. 내부 포문 돌면서 공백 제거
# 5. 자세한 내용은 ... 참고하십시요. (이전 역사) 문서의 r 판  제거
# . 으로 시작하는 문장 수정

# %%
def remove_square_bracket(sentence):
  sentence = re.sub(r"\[.{1,3}\]", "", sentence)
  return sentence
# %%
def remove_duplicated_dot(sentence):
  sentence = re.sub(r"\.+", '.', sentence)
  return sentence
# %%
def remove_only_dot_bracket(sentence):
  sentence = re.sub(r"\(.\)", '', sentence)
  return sentence

def remove_hyperlink(sentence):
  if ('(이전 역사) 문서의 r 판' in sentence) or (('자세한 내용은' in sentence) and ('참고하십시오.' in sentence)) or ('문서의 r' in sentence):
    return
  return sentence

def remove_first_dot(sentence):
  if '.' in sentence[:2]:
    return sentence[2:]
  return sentence
# %%
def filtering(sentence):
  sentence = remove_square_bracket(sentence)
  sentence = remove_duplicated_dot(sentence)
  sentence = remove_only_dot_bracket(sentence)
  sentence = remove_hyperlink(sentence)
  if sentence:
    sentence = remove_first_dot(sentence)
  return sentence

# %%
def preprocessing(file_path):
  f = open(file_path, 'r')
  lines = f.readlines()
  f.close()

  results = [filtering(sentence.strip()) for line in lines 
              for sentence in kss.split_sentences(line)]
  f = open(file_path, 'w')
  for result in results:
    if result is None:
      continue
    f.write(result.strip()+'\n')
  f.close()
# %%
if __name__ == '__main__':
  file_list = glob('/Users/jb/workspace/webscrapping/player/*.txt')
  for file in tqdm(file_list):  
    preprocessing(file)
    
# %%