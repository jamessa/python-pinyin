import re

from pypinyin.constants import Style
from pypinyin.style import register
from pypinyin.style._utils import replace_symbol_to_no_symbol


IPA_REPLACE = (
    (re.compile(r'^zhi$'), 'tʂɭ'),
    (re.compile(r'^chi$'), 'tʂʰɭ'),
    (re.compile(r'^shi$'), 'ʂɭ'),
    (re.compile(r'^ri$'), 'ʐɭ'),

    (re.compile(r'^zhi'), 'tʂ'),
    (re.compile(r'^chi'), 'tʂʰ'),
    (re.compile(r'^shi'), 'ʂ'),
    (re.compile(r'^ri'), 'ʐ'),

    (re.compile(r'^zi$'), 'tsɨ'),
    (re.compile(r'^ci$'), 'tsʰɨ'),
    (re.compile(r'^si$'), 'sɨ'),

    (re.compile(r'^zi'), 'ts'),
    (re.compile(r'^ci'), 'tsʰ'),
    (re.compile(r'^si'), 's'),

    (re.compile(r'^b'), 'p'),
    (re.compile(r'^p'), 'pʰ'),
    # m 不變
    # f 不變
    (re.compile(r'^d'), 't'),
    (re.compile(r'^t'), 'tʰ'),
    # n 不變
    # l 不變
    (re.compile(r'^g'), 'k'),
    (re.compile(r'^k'), 'kʰ'),
    # h 不變
    (re.compile(r'^j'), 'tɕ'),
    (re.compile(r'^q'), 'tɕʰ'),
    (re.compile(r'^x'), 'ɕ'),

    # ㄚ 不變
    (re.compile(r'o$'), 'ɔ'),
    (re.compile(r'e$'), 'ɘ'),  # ㄜ ㄝ 為什麼是一樣的
    # ㄞ 不變
    # ㄟ 不變
    (re.compile(r'ao$'), 'au'),  # ㄠ
    # ㄡ 不變
    # ㄢ 不變
    (re.compile(r'en$'), 'ən'),  # ㄣ
    (re.compile(r'ang$'), 'ɑŋ'),  # ㄤ
    (re.compile(r'eng$'), 'əŋ'),  # ㄥ
    (re.compile(r'er'), 'ɚ'),  # ㄦ
    (re.compile(r'r$'), 'ɚ'),  # ㄦ

    (re.compile(r'yi'), 'i'),
    (re.compile(r'wu'), 'u'),
    (re.compile(r'yu'), 'y'),

)

class IpaConverter(object):
    def to_ipa(self, pinyin, **kwargs):
        pinyin = replace_symbol_to_no_symbol(pinyin)
        for find_re, replace in IPA_REPLACE:
            pinyin = find_re.sub(replace, pinyin)
        return pinyin



converter = IpaConverter()
register(Style.IPA, func=converter.to_ipa)

