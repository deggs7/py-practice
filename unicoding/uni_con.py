#-*- coding=utf-8 -*-
unicodestring = u"中国"
utf8string = unicodestring.encode("utf-8")
utf16string = unicodestring.encode("utf-16")
gbstring = unicodestring.encode("gb2312")

print utf8string
print utf16string
print gbstring
