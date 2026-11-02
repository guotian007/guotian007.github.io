"""Build the Chinese web subset; pass the original Adobe variable WOFF2 path."""
from pathlib import Path
from html.parser import HTMLParser
from fontTools import subset
from fontTools.ttLib import TTFont
import sys
root = Path(__file__).resolve().parent
class PageText(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=False
    def handle_starttag(self, tag, attrs):
        if tag in ('style','script'): self.skip=True
    def handle_endtag(self, tag):
        if tag in ('style','script'): self.skip=False
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
p = PageText(); p.feed((root/'index.html').read_text())
chars = {ord(c) for c in ''.join(p.parts) if ord(c)>127}
font = TTFont(sys.argv[1])
chars.intersection_update(font.getBestCmap())
options = subset.Options()
options.flavor='woff2'; options.name_IDs=['*']; options.name_legacy=True; options.name_languages=['*']
subsetter = subset.Subsetter(options=options)
subsetter.populate(unicodes=chars); subsetter.subset(font)
# Adobe's reserved name is omitted from the modified font's family identifiers.
names={1:'TinySky Han Serif',3:'TinySkyHanSerif-WebSubset-1',4:'TinySky Han Serif',6:'TinySkyHanSerif',16:'TinySky Han Serif',17:'Regular',21:'TinySky Han Serif',22:'Regular',25:'TinySkyHanSerif'}
for record in font['name'].names:
    if record.nameID in names: record.string=names[record.nameID].encode(record.getEncoding())
font.flavor='woff2'; font.save(root/'tinysky-han-serif.woff2')
print('Chinese serif subset:', len(chars), 'characters;', (root/'tinysky-han-serif.woff2').stat().st_size, 'bytes')
