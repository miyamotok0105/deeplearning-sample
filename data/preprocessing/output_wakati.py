#coding:utf-8
import MeCab
tagger = MeCab.Tagger("-Owakati")

f_r = open('../text/text_miyazawa1.txt')
f_w = open('../text/text_miyazawa1_wakati.txt', 'w')
lines = f_r.readlines()
for line in lines:
    f_w.writelines(tagger.parse(line))

f_w.close()
f_r.close()

