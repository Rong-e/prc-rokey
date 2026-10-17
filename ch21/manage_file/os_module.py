import os
print(os.getcwd())
# 작업ㄷ 디렉터리 변경

os.chdir(r'ch21\manage_file')
print(os.getcwd())

print('---------------')

print(f'디렉터리 목록: {os.listdir('.')}') #현재위치에 어떤 파일이 있는지 확인

print('------------------------------')
os.mkdir('test_dir') #디렉토리 생성
os.rmdir('test_dir') #디렉토리 삭제

if os.path.exists('file.txt'):
    print('존재')
else:
    print('X')
    
print('------------------------------')
folder = os.getcwd()

# 경로 합치고
print(os.path.join(folder,'file.txt'))
# 파일명만 추출
print(os.path.basename(rf'{folder}\file.txt')) #r 과 f둘다 사용되나??
# 디렉토리 경로 추출
print(os.path.dirname(f'{folder}/file.txt'))

