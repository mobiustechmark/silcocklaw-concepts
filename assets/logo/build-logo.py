# Regenerates silcocklaw-logo.svg: outlines the wordmark in Poppins ExtraBold and places the original
# V3 feather vector exactly where the live page draws it (positions measured in headless Chrome, 54px).
# Needs fonttools + Poppins-ExtraBold.ttf (google/fonts, OFL) in ./font/.
# Usage: python build-logo.py ../../mockups/index.html silcocklaw-logo.svg
import re, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

f = TTFont('font/Poppins-ExtraBold.ttf')
gs = f.getGlyphSet(); cmap = f.getBestCmap()
asc = f['hhea'].ascent; upm = f['head'].unitsPerEm
SIZE = 54.0; k = SIZE / upm
TOP = 34.359375; BASE = TOP + asc * k
chars = [('S',0),('I',34.03125),('L',51.21875),('C',78.265625),('O',119.734375),('C',162.78125),('K',204.25),('L',244),('A',271.046875),('W',312.359375)]
RUST, NAVY = '#9A4A22', '#31336E'
paths = []; xs=[]; ys=[]
for i,(ch,x) in enumerate(chars):
    g = gs[cmap[ord(ch)]]
    t = (k,0,0,-k,x,BASE)
    pen = SVGPathPen(gs); g.draw(TransformPen(pen, t))
    bp = BoundsPen(gs); g.draw(TransformPen(bp, t)); b = bp.bounds
    xs += [b[0], b[2]]; ys += [b[1], b[3]]
    d = re.sub(r'(\d+\.\d{3})\d+', r'\1', pen.getCommands())
    paths.append((d, RUST if i < 7 else NAVY))
html = open(sys.argv[1], encoding='utf-8').read()
fsvg = re.search(r'<svg class="lg-feather"[^>]*>(.*?)</svg>', html, re.S).group(1)
FX, FY, FW = 19.1953125, -0.53125, 46.859375
s = FW / 81.0
xs += [FX, FX+FW]; ys += [FY, FY + 105*s]
pad = 2
x0, y0 = min(xs)-pad, min(ys)-pad
w, h = max(xs)-min(xs)+2*pad, max(ys)-min(ys)+2*pad
out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.2f %.2f %.2f %.2f" width="%.0f" height="%.0f" role="img" aria-label="Silcock Law">' % (x0,y0,w,h,w,h),
       '  <title>Silcock Law</title>',
       '  <!-- Wordmark: Poppins ExtraBold 800, 54px, letter-spacing .01em, outlined. Feather: original V3 vector. -->',
       '  <g id="silcock" fill="%s">' % RUST]
out += ['    <path d="%s"/>' % d for d,c in paths if c == RUST]
out += ['  </g>', '  <g id="law" fill="%s">' % NAVY]
out += ['    <path d="%s"/>' % d for d,c in paths if c == NAVY]
out += ['  </g>', '  <g id="feather" transform="translate(%.4f %.4f) scale(%.6f) translate(-174 -109)">' % (FX, FY, s), '    ' + fsvg.strip(), '  </g>', '</svg>', '']
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out))
print('viewBox', x0, y0, w, h)
