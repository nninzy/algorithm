croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=']
string = input()
answer = 0
left_len = len(string)
for alp in croatia :
    cnt_alp = string.count(alp)
    answer += cnt_alp
    left_len -= (len(alp) * cnt_alp)
cnt_dz = string.count('dz=')
cnt_z = string.count('z=') - cnt_dz if 'dz=' in string and 'z=' in string else string.count('z=')
answer += cnt_dz + cnt_z
left_len -= ((3 * cnt_dz) + (2 * cnt_z))
print(answer + left_len)