import shutil
import os

# 파일복사 
# shutil.copy('source.txt','destination.txt') # 파일복사
# shutil.copy2('source.txt','destination.txt') # 파일생성 날짜 등 메타데이터 유지

path = r'ch21\manage_file'
src = f'{path}/file.txt'
dst = f'{path}/copiedfile.txt'

shutil.copy(src,dst)
shutil.copy2(src,dst)

# 디렉토리복사
# 생성
folder = f'{path}/test_dir'
if not os.path.exists(folder):
    os.mkdir(folder)

# 파일복사

src = f'{path}/file.txt'
dst = f'{path}/test_dir/file.txt'
if not os.path.exists(dst):
    shutil.copy(src,dst)

# 디렉토리 전체 복사
src = f'{path}/test_dir'
dst = f'{path}/copied_test_dir'
if not os.path.exists(dst):
    shutil.copytree(src,dst)

# 파일 및 디렉토리 이동
src = f'{path}/copiedfile.txt'
dst = f'{path}/copied_test_dir/copiedfile.txt'
if not os.path.exists(dst):
    shutil.move(src,dst)


# 파일 및 디렉토리 삭제

# 디렉토리 및 하위파일 모두 삭제
dir1 = f'{path}/test_dir'
dir2 = f'{path}/copied_test_dir'
shutil.rmtree(dir1)
shutil.rmtree(dir2)