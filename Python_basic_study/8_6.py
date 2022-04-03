for i in range(1,51):
    with open("{0}주차.txt".format(i),"w",encoding='utf8') as report_file:
        report_file.write("-{0}주차 주간 보고-\n부서:\n이름:\n업무요약:".format(i))

