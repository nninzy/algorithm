croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=']
string = input()
# 크로아티아 알파벳 개수 = 특수알파벳 개수 + 일반알파벳 개수
# 이외 알파벳 개수 (1개짜리)= 전체 문자 - (특수알파벳 글자수 * 특수알파벳 개수)
answer = 0
left_len = len(string)
# 'dz-' 와 'z-' 제외 크로아티아 알파벳 계산
for alp in croatia :
    cnt_alp = string.count(alp)
    answer += cnt_alp
    left_len -= (len(alp) * cnt_alp)
# 'dz-'와 'z-' 알파벳 계산
cnt_dz = string.count('dz=')
# 만약 'dz-'와 'z-'가 동시에 존재할 경우 z-가 dz-도 계산함
cnt_z = string.count('z=') - cnt_dz if 'dz=' in string and 'z=' in string else string.count('z=')
answer += cnt_dz + cnt_z
left_len -= ((3 * cnt_dz) + (2 * cnt_z))
print(answer + left_len)