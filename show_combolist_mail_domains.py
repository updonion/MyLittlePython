import re
import collections

file = input("Combolist: ")
of = open(file, 'r')
# string = """tlouro@ig.com.br:iris75
# nbarncastle@gmx.fr:JJJJJJ
# o.jonson@laposte.net:harb4343
# gwojcicki@wanadoo.fr:110770
# sduriga@wanadoo.co.uk:w5tmp3a3
# hagyeman@yahoo.com.mx:y5dckzdg
# yjedlicka@google.com:k1i2m360
# wleiber@googlemail.com:worf2000
# augustustartamella@wanadoo.fr:3Gwao71pdG
# z.vafiades@hotmail.fr:Marina20059163
# sharicejudon@nate.com:1967040615
# lmickleberry@gmail.com:yemelyanov57
# gosowski@email.com:22011982
# vernetta.turdo@live.com.mx:sto123
# s.prosise@earthlink.net:1584158
# anh.lewandowsky@yahoo.co.in:sim2b
# dainericord@bol.com.br:flicke88
# zmincey@speedy.com.ar:yolanda7
# agoswick@list.ru:owls93
# mforinash@aol.com:the_best68
# jcarriger@yahoo.co.uk:vizorium
# mpinckard@live.com:ded51461
# a.oquenda@yahoo.com:fortheho
# v.pokora@naver.com:89092251529
# jtrowel@voo.be:yana199326123
# klepera@uol.com.br:Vn2L5sNzK5D164
# evonbank@foxmail.com:365ford
# rstaehler@mail.com:verdadeiro80
# ikoelsch@wanadoo.fr:hummasti
# omathelier@live.it:saransk
# ben@live.fr:stas1987
# friggings@mail.com:vbhjplfybt
# htaube@t-online.de:xicu
# marybelle.singlton@daum.net:jgb1gd30
# x.bretthauer@yahoo.co.kr:8Ux3PYvu
# irvinpetrik@cox.net:ylOREPOJe79
# w.quenzer@freeserve.co.uk:icwphbk
# agripinavassall@laposte.net:gang02
# carissawinegarden@web.de:kotikkotik21"""

m = re.compile('[\w\d\-+_.]*@([\w\d\-.]*):.*')

x = m.findall(of.read())
y = collections.Counter(x)

print(y)
for i in sorted(y, key=y.get, reverse=False):
    print("\r", i, "\t\t", y[i])
    # if y[i] >= 100:
    #     print(i, "\t", y[i])
# print(y)

# print(of.read())


# pattern = f"[\w\d\-+_.]*@([\w\d\-.]*):.*$"
# re.compile(pattern)

