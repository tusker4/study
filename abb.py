status_counter = {}

with open('access.log.2017-10-13', 'r', encoding='utf8') as fp:
    for line in fp:
        stat = line.split()[8]
        if stat in status_counter:
            status_counter[stat] += 1
        else:
            status_counter[stat] = 1
print(status_counter)

with open('statics.txt', 'w') as fp:
    for key,value in status_counter.items():
        print(f"{key} : {value}", file=fp)
print("통계를 출렦ㅎㅇㅅㄴㄷ")

wb = openpyxl.Workbook()  # wb는 엑셀파일 데이터
ws = wb.active  # 엑셀파일에는 기본시트 얻어내기
for key, value in status_counter.items():
    ws.append(item) # 데이터를 기록
count = len(status_counter)
ws.append(['요청합계', f'='])
wb.save('statics.xlsx')
wb.close()
        



