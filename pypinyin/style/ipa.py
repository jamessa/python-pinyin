import re

from pypinyin.constants import Style
from pypinyin.style import register
from pypinyin.style._utils import replace_symbol_to_no_symbol, get_initials, get_finals, replace_symbol_to_number
from pypinyin.style._constants import RE_TONE3

initials = {
    'b': 'p',   # ㄅ
    'p': 'pʰ',  # ㄆ
    'm': 'm',   # ㄇ
    'f': 'f',   # ㄈ
    'd': 't',   # ㄉ
    't': 'tʰ',  # ㄊ
    'n': 'n',   # ㄋ
    'l': 'l',   # ㄌ
    'g': 'k',   # ㄍ
    'k': 'kʰ',  # ㄎ
    'h': 'h',   # ㄏ
    'j': 'tɕ',  # ㄐ
    'q': 'tɕʰ',  # ㄑ
    'x': 'ɕ',   # ㄒ
    'zh': 'ʈʂ',  # ㄓ
    'ch': 'ʈʂʰ',  # ㄔ
    'sh': 'ʂ',  # ㄕ
    'r': 'ʐ',  # ㄖ
    'z': 'ts',  # ㄗ
    'c': 'tsʰ',  # ㄘ
    's': 's',  # ㄙ
}

specials = {
    'zhi': 'ʈʂʅ',   # ㄓ
    'chi': 'ʈʂʰʅ',  # ㄔ
    'shi': 'ʂʅ',    # ㄕ
    'ri': 'ʐʅ',     # ㄖ
    'zi': 'tsɨ',   # ㄗ
    'ci': 'tsʰɨ',   # ㄘ
    'si': 'sɨ',   # ㄙ
    'yi': 'i',  # ㄧ
    'wu': 'w',  # ㄨ
    'yu': 'y',   # ㄩ
    'ya': 'ja',     # ㄧㄚ
    'yao': 'jau',   # ㄧㄠ
    'ye':   'jɛ',   # ㄧㄝ
    'you':  'jou',  # ㄧㄡ
    'yan':  'jɛn',  # ㄧㄢ
    'yang': 'jɑŋ',  # ㄧㄤ
    'yin':  'jin',  # ㄧㄣ
    'ying': 'jiŋ',  # ㄧㄥ
    'yue':  'yɛ',   # ㄩㄝ
    'yuan': 'yan',  # ㄩㄢ
    'wa':   'wɑ',   # ㄨㄚ
    'wo':   'wɔ',   # ㄨㄛ
    'wai':  'wai',  # ㄨㄞ
    'wei':  'wei',  # ㄨㄟ
    'wan':  'wan',  # ㄨㄢ
    'wen':  'wʊn',  # ㄨㄣ
    'wang': 'wɑŋ',  # ㄨㄤ
    'weng': 'wɔŋ',  # ㄨㄥ
    'yun':  'yn',   # ㄩㄣ
    'yong': 'jɔŋ ',     # ㄩㄥ
}

finals = {
    'a': 'a',   # ㄚ
    'o': 'ʊ',   # ㄛ
    'e': 'ə',   # ㄜㄝ
    'ai': 'ai',     # ㄞ
    'ei': 'ei',     # ㄟ
    'ao': 'au',     # ㄠ
    'ou': 'ou',     # ㄡ
    'an': 'an',     # ㄢ
    'en': 'ən',     # ㄣ
    'ang':  'ɑŋ',   # ㄤ
    'eng':  'əŋ',   # ㄥ
    'er':   'ɚ',    # ㄦ
    'i': 'i',  # ㄧ
    'u': 'u',  # ㄨ
    'v': 'y',  # ㄩ

    'ia': 'ia',  # ㄧㄚ
    'iao': 'iau',  # ㄧㄠ
    'ie': 'iɛ',  # ㄧㄝ
    'iu': 'iou',  # ㄧㄡ
    'ian': 'iɛn',  # ㄧㄢ
    'iang': 'iɑŋ',  # ㄧㄤ
    'in': 'in',  # ㄧㄣ
    'ing': 'iŋ',  # ㄧㄥ
    'ue': 'yɛ',  # ㄩㄝ
    'uan': 'yan',  # ㄩㄢ
    'ua': 'uɑ',  # ㄨㄚ
    'uo': 'ʊɔ',  # ㄨㄛ
    'uai': 'uai',  # ㄨㄞ
    'uei': 'uei',  # ㄨㄟ
    'uan': 'uan',  # ㄨㄢ
    'un': 'ʊn',  # ㄨㄣ
    'uang': 'uɑŋ',  # ㄨㄤ
    'ong': 'ɔŋ',  # ㄨㄥ
    'un': 'yn',  # ㄩㄣ
    'iong': 'iɔŋ ',  # ㄩㄥ
}

symbols = ['', '˦˦', '˧˦', '˨˩', '˥˩']


class IpaConverter(object):
    def to_ipa(self, pinyin, **kwargs):
        number = replace_symbol_to_number(pinyin)
        s = 0
        try:
            s = int(RE_TONE3.sub(r'\2', number))
        except ValueError:
            pass
        pinyin = replace_symbol_to_no_symbol(pinyin)
        # for find_re, replace in IPA_REPLACE:
        #     pinyin = find_re.sub(replace, pinyin)
        initial = get_initials(pinyin, True)
        final = get_finals(pinyin, True)
        if initial in initials.keys():
            initial = initials[initial]
        if final in finals.keys():
            final = finals[final]
        return initial + final + symbols[s]



converter = IpaConverter()
register(Style.IPA, func=converter.to_ipa)

