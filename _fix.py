# -*- coding: utf-8 -*-
import os
os.chdir(r'C:\Users\Administrator\WorkBuddy\简历\resume-site')
p = 'index.html'
lines = open(p, encoding='utf-8').read().split('\n')

# 找到新看板块的起始行
s = None
for i, l in enumerate(lines):
    if l.strip().startswith('<!-- 看板作品 3：销量预测与库存预警看板'):
        s = i
        break
assert s is not None, 'block start not found'

# 块结束行：起始后第一个缩进8位的 </div>
e = None
for i in range(s + 1, len(lines)):
    if lines[i] == '        </div>':
        e = i
        break
assert e is not None, 'block end not found'

# 其后应为 12sp/10sp/8sp 三个闭合（采购看板的 dash-panel/dash-mock/portfolio-item）
assert lines[e+1].startswith('            </div>'), repr(lines[e+1])
assert lines[e+2].startswith('          </div>'), repr(lines[e+2])
assert lines[e+3] == '        </div>', repr(lines[e+3])

block = lines[s:e+1]
closes = lines[e+1:e+4]
lines = lines[:s] + closes + block + lines[e+4:]

open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('moved ok, block lines:', len(block))
