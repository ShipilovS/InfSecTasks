import string
import numpy as np
text = """щ  зсдлъэд фцяб  цоцюъбк сня пбь  емйюсцдъ й  цяъцк  йюцсцъб йюмсэъъбжэ яцжмжэ, м й ясыфцк - яьэъъбж цяъцгюмлъбж еямъэдж зця цяъцк исбудк,  ъдйжцюсн ъм юц, аюц цъц зсэъмяьдлмьц ядйнюимж щьмядьчшдщ. эе щйдо гюэо еямъэк юцьчиц ящм яцжм пбьэ лэьбжэ: яцж, фяд  фцйюэъэшм "ицъюэъдъюмьч", ям йюцнвэк сняцж й ъэж юсмиюэс дфцсцщм, еъмждъэюбк йщцэжэ пьэъмжэ.  цйюмьчъцд щйд ьмщиэ, щзьцюч яц ющдсйицк.
юсмиюэс  дфцсцщм  ицфям-юц  зсэъмяьдлмь щцсцъэъы,  э  ъм  щбщдйид  пбьм эецпсмлдъм щцсцъм,  ядслмвмн  щ  иьтщд пьэъ. щйд  ьмщиэ  цоцюъцфц сням  пбьэ жнйъбд, сбпъбд, м зця  ъэжэ едьдъъбд зцящмьб. емяъэд ящдсэ ьмщци щбоцяэьэ ъм цфсцжъбк  ящцс-жцъдюъбк,  ими  дфц  ъмебщмьэ  эеясдщьд.  ъм  ъдж  пбьэ юцлд цяъцгюмлъбд  жнйъбд,  лэщцсбпъбд  э нэаъбд  ьмщиэ,  м зцйсдяэъд--ящыогюмлъбк "жцъдюъбк"  юсмиюэс. щ емяъдк амйюэ ящцсм - сня  ймсмтуди й зцфсдпмжэ э иьмяцщбжэ, иэудщуэжэ зцьаэвмжэ исбй.
цоцюъбк  сня зцьыаэь  йщцд  ъмещмъэд  двд щ  юд  щсдждъм,  ицфям  еядйч смесдудъц пбьц юцсфцщмюч яэачт, зсэъцйэжцк зцяжцйицщъбжэ цоцюъэимжэ.
щздсдяэ  ьмщци, ъм зьцвмяэ, щяцьч  уэсцицфц юсцюымсм, йюцньэ здсдъцйъбд змьмюиэ   э   юцьзэьэйч   юцсфцщшб  й  ицсеэъмжэ  э   ждуимжэ,  ъмзцьъдъъбжэ щйдщцежцлъбжэ  зсцяыиюмжэ.  оцяэьэ цоцюъэиэ,  цпщдумъъбд  ыюимжэ, юдюдсимжэ, емкшмжэ. ы пмп эе ицсеэъ юцсамьэ фцьцщб иыс э шбзьню, щ ждуимо щэелмьэ зцсцйнюм,  ицюцсбо зсцямщшб, щбъэжмн эе ждуим,аюцпб  зцимемюч  зциызмюдьт,  ъдзсдждъъц зцяъэжмьэ  ъмя  фцьцщцк,  ядслм ем йщнемъъбд  емяъэд  ъцфэ.  ъм  жцйюцщцк  здсдя  змьмюимжэ  йъцщмьэ зэсцлъэиэ, пьэъъэиэ,  юцсфцщшб фсдаъдщэимжэ,  лмсдъъбжэ  ъм зцйюъцж  жмйьд. йпэюдъвэиэ смеьэщмьэ, зц ицздкид ем  йюмимъ,  фцснаэк йпэюдъч - ьтпэжбк  юцфям ждяцщбк
ъмзэюци, йцфсдщмщуэк эещцеаэицщ э йьылмвэо,  емждсемщуэо щ оцьцяъбо  ьмщимо. ьдюцж  йпэюдъвэицщ  йждъньэ юцсфцщшб  ищмймжэ, э  ймжбк  ьтпэжбк эе ъэо  пбь фсыудщбк, эе  щмсдъбо  фсыу,  ицюцсбд  щ  жцадъцж  щэяд ьдлмьэ  яьн  зсцямлэ зэсмжэямжэ ъм ьцюимо, м ищмй адсзмьэ эе щдясм исылимжэ. жнйъбд э сбпъбд ьмщиэ йцйюцньэ эе  ящыо цюядьдъэк. щ  здсщцж ьдлмьц ъм зцьимо жнйц смеъбо йцсюцщ - яэач, иысб, фыйэ, эъядкиэ, змьдъбд зцсцйнюм яьн лмсицфц  э щ ьдянъбо  щмъъмо - пдьбд зцсцйнюм  яьн емьэщъцфц.  ъм истачно  зц йюдъмж пбьэ смещдумъб юыуэ пмсмуицщ э  зцдъъбо жцьцицж юдьню, м щдйч зцюцьци емъню  цицсцимжэ  щйдщцежцлъбо смеждсцщ э  зсэфцюцщьдъэк--ицзадъбо, щмсдъбо, зсцщдйъбо. щц щюцсцж  цюядьдъээ, юджъцж,  цйщдвдъъцж юцьчиц ящдсчт  щц ящцс, щэйдьэ ядйнюиэ жнйъбо  юыу. зця щйджэ ьмщимжэ -- зцящмьб. цоцюъбк  сня пбщмь цйцпдъъц  цлэщьдъъбж  здсдя  пцьчуэжэ  зсмеяъэимжэ.  и ьмщимж  зцяхделмьэ ъм юбйнаъбо сбймимо смйрсмъадъъбд иызаэоэ, э ем ъэжэ йьылмвэд щбъцйэьэ эе ьмщци"""
# text = "щ  зсдлъэд фцяб  цоцюъбк сня пбь  емйюсцдъ й  цяъцк щ щ щщ уу аа фф яяя ммм "

new_text = text.strip().replace('  ', ' ').split(' ')
print(new_text)

def n_grams(text, n):
    d = {}
    count = 0
    for elem in text:
        if len(elem) == n and elem.isalpha():
            if d.get(elem):
                d[elem] += 1
            else:
                d[elem] = 1
    return dict(reversed(sorted(d.items(), key=lambda x : x[1])))
one = n_grams(new_text, 1)  
two = n_grams(new_text, 2)
three = n_grams(new_text, 3)
print(one)
print(two)
print(three)

print(f"====")

def n_grams(text, n):
    text = str(text).strip().replace('-', '').replace(' ', '').replace('  ', '')
    d = {}
    for key in range(len(text)):
        sub_text = text[key : key+n]
        if d.get(sub_text):
            d[sub_text] += 1
        else:
            d[sub_text] = 1
    return dict(reversed(sorted(d.items(), key=lambda x : x[1])))
one = n_grams(text, 1)  
two = n_grams(text, 2)
three = n_grams(text, 3)
print(one)
print(two)
print(three)

"""э - часто как буква 'и'
эе - может быть как 'из'
ем - "за"
ъм - "?а" - на

"""

global_dict = {
    'э' : 'и',
    'е' : 'з',
    'м' : 'а',
    'ъ' : 'н',
    'и' : 'к', # иАи - КАК
    # 'п' : 'к',
    # 'щ' : 'о',
    # 'й' : 'с',
    
    'я' : 'д',
    'д' : 'е',
    'ж' : 'м',
    'у' : 'ш',
    'ц' : 'о',
    'ь' : 'л',
    'с' : 'р',
    'з' : 'п',
    'л' : 'ж',
    'н' : 'я',
    'в' : 'щ',
    'б' : 'ы',
    'й' : 'с', # ?
    'п' : 'б',
    'ю' : 'т',
    'к' : 'й',
    'щ' : 'в',
    'а' : 'ч',
    'ы' : 'у',
    'ф' : 'г',
    'ы' : 'у',
    'ш' : 'ц',
    'о' : 'х',
    'г' : 'э',
    'ч' : 'ь',
    'т' : 'ю',
    'х' : 'ъ',
    'р' : 'ф',
}
# ЗАДНдк ЗАДНИд  д - е?
# НА  НЕж на нем?
# МЕуКАМИ - мешками?
# ДцМА - Дома
# МОьОКОМ - молоком
# ИЗ КОсЗИН - из корзин
# зРИНАДЛЕлАЛО  - принадлежало
# ЛЕЖАЛИ  ДЛн  ПРОДАЖИ ПИРАМИДАМИ -  ДЛн - для
# ПЛОвАДИ - площади
# ДЛИННбМ - длинным 
# йМЕНЯЛИ - сменяли?
# пбЛ  - пЫЛ - был
# СюОРОНЫ  - стороны
# ОДНОк   - одной
# аТО - что
# ы БАБ ИЗ КОРЗИН ТОРЧАЛИ фОЛОВЫ КыР И шЫПЛЯТ  СЛУЖАЩИо,  ЗАМЕРЗАВШИо ДЛИННЫМ ОДНОгТАЖНЫМ ЗДАНИЕМ

res_text = ''
for sym in text:
    if global_dict.get(sym):
        res_text += str(global_dict[sym]).upper()
    else:
        res_text += sym

print(str(res_text))

text_en = """pyt viqebov, xp q bqcvmc oxgvmzv jylof myc bvtexc tyrqocr-ptvv tvfxzctxhlcxym yp cwv btystqe hr
qoo cwyzv jwy tvgvxnv gybxvz fxtvgcor yt xmfxtvgcor cwtylsw ryl, cwvm cwv ymor jqr ryl gylof zqcxzpr hycw xc qmf cwxz oxgvmzv jylof hv cy tvptqxm vmcxtvor ptye fxzctxhlcxym yp cwv btystqe. 
xp qmr bytcxym yp cwxz zvgcxym xz wvof xmnqoxf yt lmvmpytgvqhov lmfvt qmr bqtcxgloqt gxtglezcqmgv, cwv hqoqmgv yp cwv zvgcxym xz xmcvmfvf cy qbbor qmf cwv zvgcxym qz q jwyov xz xmcvmfvf cy qbbor xm ycwvt gxtglezcqmgvz.
xc xz myc cwv bltbyzv yp cwxz zvgcxym cy xmflgv ryl cy xmptxmsv qmr bqcvmcz yt ycwvt btybvtcr txswc goqxez yt cy gymcvzc nqoxfxcr yp qmr zlgw goqxez; cwxz zvgcxym wqz cwv zyov bltbyzv yp btycvgcxms cwv xmcvstxcr yp cwv ptvv zypcjqtv fxzctxhlcxym zrzcve, jwxgw xz xebovevmcvf hr blhoxg oxgvmzv btqgcxgvz.  eqmr bvybov wqnv eqfv svmvtylz gymctxhlcxymz cy cwv jxfv tqmsv yp zypcjqtv fxzctxhlcvf
cwtylsw cwqc zrzcve xm tvoxqmgv ym gymzxzcvmc qbboxgqcxym yp cwqc zrzcve; xc xz lb cy cwv qlcwyt/fymyt cy fvgxfv xp wv yt zwv xz jxooxms cy fxzctxhlcv zypcjqtv cwtylsw qmr ycwvt zrzcve qmf q oxgvmzvv gqmmyc xebyzv cwqc gwyxgv.
cwxz zvgcxym xz xmcvmfvf cy eqdv cwytylswor govqt jwqc xz hvoxvnvf cy hv q gymzvalvmgv yp cwv tvzc yp cwxz oxgvmzv. 
  xp cwv fxzctxhlcxym qmf/yt lzv yp cwv btystqe xz tvzctxgcvf xm gvtcqxm gylmctxvz vxcwvt hr bqcvmcz yt hr gybrtxswcvf xmcvtpqgvz, cwv ytxsxmqo gybrtxswc wyofvt jwy boqgvz cwv btystqe lmfvt cwxz oxgvmzv eqr qff qm viboxgxc svystqbwxgqo fxzctxhlcxym oxexcqcxym vigolfxms cwyzv gylmctxvz, zy cwqc fxzctxhlcxym xz bvtexccvf ymor xm yt qeyms gylmctxvz myc cwlz vigolfvf.  xm zlgw gqzv, cwxz oxgvmzv xmgytbytqcvz cwv oxexcqcxym qz xp jtxccvm xm cwv hyfr yp cwxz oxgvmzv. 
 cwv ptvv zypcjqtv pylmfqcxym eqr blhoxzw tvnxzvf qmf/yt mvj nvtzxymz yp cwv svmvtqo blhoxg oxgvmzv ptye cxev cy cxev.  zlgw mvj nvtzxymz jxoo hv zxexoqt xm zbxtxc cy cwv btvzvmc nvtzxym, hlc eqr fxppvt xm fvcqxo cy qfftvzz mvj btyhovez yt gymgvtmz.
vqgw nvtzxym xz sxnvm q fxzcxmslxzwxms nvtzxym mlehvt.  xp cwv btystqe zbvgxpxvz q nvtzxym mlehvt yp cwxz oxgvmzv jwxgw qbboxvz cy xc qmf "qmr oqcvt nvtzxym", ryl wqnv cwv ybcxym yp pyooyjxms cwv cvtez qmf gymfxcxymz vxcwvt yp cwqc nvtzxym yt yp qmr oqcvt nvtzxym blhoxzwvf hr cwv ptvv
zypcjqtv pylmfqcxym.  xp cwv btystqe fyvz myc zbvgxpr q nvtzxym mlehvt yp cwxz oxgvmzv, ryl eqr gwyyzv qmr nvtzxym vnvt blhoxzwvf hr cwv ptvv zypcjqtv pylmfqcxym.
  xp ryl jxzw cy xmgytbytqcv bqtcz yp cwv btystqe xmcy ycwvt ptvv btystqez jwyzv fxzctxhlcxym gymfxcxymz qtv fxppvtvmc, jtxcv cy cwv qlcwyt cy qzd pyt bvtexzzxym.  pyt zypcjqtv jwxgw xz gybrtxswcvf hr cwv ptvv zypcjqtv pylmfqcxym, jtxcv cy cwv ptvv zypcjqtv pylmfqcxym; jv zyevcxevz
eqdv vigvbcxymz pyt cwxz.  ylt fvgxzxym jxoo hv slxfvf hr cwv cjy syqoz yp btvzvtnxms cwv ptvv zcqclz yp qoo fvtxnqcxnvz yp ylt ptvv zypcjqtv qmf yp btyeycxms cwv zwqtxms qmf tvlzv yp zypcjqtv svmvtqoor.
hvgqlzv cwv btystqe xz oxgvmzvf ptvv yp gwqtsv, cwvtv xz my jqttqmcr pyt cwv btystqe, cy cwv vicvmc bvtexccvf hr qbboxgqhov oqj.  vigvbc jwvm ycwvtjxzv zcqcvf xm jtxcxms cwv gybrtxswc wyofvtz qmf/yt ycwvt bqtcxvz btynxfv cwv btystqe "qz xz" jxcwylc jqttqmcr yp qmr dxmf, vxcwvt vibtvzzvf
yt xeboxvf, xmgolfxms, hlc myc oxexcvf cy, cwv xeboxvf jqttqmcxvz yp evtgwqmcqhxoxcr qmf pxcmvzz pyt q bqtcxgloqt bltbyzv.  cwv vmcxtv txzd qz cy cwv alqoxcr qmf bvtpyteqmgv yp cwv btystqe xz jxcw ryl.  zwylof cwv btystqe btynv fvpvgcxnv, ryl qzzlev cwv gyzc yp qoo mvgvzzqtr zvtnxgxms, tvbqxt yt gyttvgcxym"""

new_text_en = text_en.strip().replace('  ', ' ').split(' ')
print(new_text_en)

def n_grams(text, n):
    d = {}
    count = 0
    for elem in text:
        if len(elem) == n and elem.isalpha():
            if d.get(elem):
                d[elem] += 1
            else:
                d[elem] = 1
    return dict(reversed(sorted(d.items(), key=lambda x : x[1])))
one = n_grams(new_text_en, 1)  
two = n_grams(new_text_en, 2)
three = n_grams(new_text_en, 3)
four = n_grams(new_text_en, 4)
five = n_grams(new_text_en, 5)
print(one)
print(two)
print(three)
print(four)
print(five)
print(f"====")

def n_grams(text, n):
    text = str(text).strip().replace('-', '').replace(' ', '').replace('  ', '')
    d = {}
    for key in range(len(text)):
        sub_text = text[key : key+n]
        if d.get(sub_text):
            d[sub_text] += 1
        else:
            d[sub_text] = 1
    return dict(reversed(sorted(d.items(), key=lambda x : x[1])))
one = n_grams(text_en, 1)  
two = n_grams(text_en, 2)
three = n_grams(text_en, 3)
four = n_grams(text_en, 4)
five = n_grams(text_en, 5)
print(one)
print(two)
print(three)
print(four)
print(five)

global_dict_en = {
    'c' : 't',
    'w' : 'h',
    'v' : 'e',
    't' : 'r',
    'p' : 'f',
    'x' : 'i',
    'z' : 's',
    'y' : 'o',
    'j' : 'w',
    'm' : 'n',
    'n' : 'v',
    'q' : 'a',
    'f' : 'd',
    'l' : 'u',
    'b' : 'p',
    'o' : 'l',
    'h' : 'b',
    'g' : 'c',
    'e' : 'm',
    's' : 'g',
    'i' : 'x',
    'r' : 'y',
    'd' : 'k'
}
# REDISTRIhlTION lNDER
# IT IS NyT
# DIREgTor OR INDIREgTor
# REgEIVE - receive
# SOFTWqRE FOlNfqTION
# nERSIONS - versions
#  fISTRIhlTIOm - TION
# xf - if
# mOT - not hot
# jHO - who
# THOzE - THOSE
# WHxz - what
# RyrqoWr-pREE - -free
# ypcw  ycwv  zypc - pc
# blhoIg
# cwvtv - where
# yp to
# cy at
# xz 
# xp
# xc
# yt

res_text_en = ''
for sym in text_en:
    if global_dict_en.get(sym):
        res_text_en += str(global_dict_en[sym]).upper()
    else:
        res_text_en += sym

print(str(res_text_en))



