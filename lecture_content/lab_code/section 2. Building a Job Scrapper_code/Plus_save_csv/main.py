from indeed import get_jobs as get_indeed_jobs
from save import save_to_file
# import so -> stackOverFlow 생략

indeed_jobs = get_indeed_jobs()
#so_jobs = get_jobs() -> stackOverFlow 생략
# print(indeed_jobs) -> 입력값 확인
save_to_file(indeed_jobs)