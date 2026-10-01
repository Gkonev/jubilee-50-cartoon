# Собирает index.html (цветная) и gazeta.html (газетная) из src/template.html
t=open('src/template.html',encoding='utf-8').read()
open('index.html','w',encoding='utf-8').write(t.replace('__SWITCH_HREF__','gazeta.html').replace('__SWITCH_LABEL__','Газетная версия →').replace('__THEMIS__','themis.png'))
open('gazeta.html','w',encoding='utf-8').write(t.replace('data-theme="mix"','data-theme="paper"').replace('__SWITCH_HREF__','index.html').replace('__SWITCH_LABEL__','Цветная версия →').replace('__THEMIS__','themis_bw.png'))
print('built')
