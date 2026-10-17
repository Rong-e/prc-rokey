from pathlib import Path

print(Path.cwd())
# 현재 디렉토리와  (cwd했을때 나오는 디렉토리)
# 작업디렉토리는 다르다 (지금 작업하고 잇는 파일)
print(Path.home()) # 사용자 디렉터리 확인


# 경로 생성 및 조작
folder = r'ch21\classify_file'
path = Path(folder)
#/연산자는 경로 결합 연산자로, pathlib.path 객체에서 지원
print(path / 'file.txt')

# 파일경로 존재 여부 화긴

file = path / 'file.txt'
path = Path(file)
print(path.exists())  #존재여부 확인
print(path.is_file()) #파일 존재여부 확인
print(path.is_dir()) #디렉토리 여부 확인


# 디렉토리 생성 및 삭제

new_folder = r'ch21\classify_file\new_folder'
path = Path(new_folder)
path.mkdir(exist_ok=True) #폴더생성 (기존 존재시에도 에러발생하지 않게 옵션처리)
path.rmdir()

# 파일 생성 및 삭제
new_file = r'ch21\classify_file\file.txt'
file_path = Path(new_file)
# file_path.touch()
file_path.touch(exist_ok = True)
file_path.unlink()
