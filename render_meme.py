#!/usr/bin/env python3
"""Render the v7 jury-duty-summons meme, 1024x1024 PNG, PIL only.
Original design, code-rendered for legibility at 480x480.
Vertical budget (measured, must sum <= 1024):
  header 48..88 | JURY DUTY 88..184 | SUMMONS 184..284 | rule 284..306
  summoned line 306..346 | fields box 346..548 | stamp 566..712
  reason box 720..832 | navy band 837..997 | outer border to 1010
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

CREAM = (247, 241, 227)
NAVY = (27, 42, 74)
RED = (178, 34, 34)
INK = (30, 30, 30)

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

d.rectangle([14, 14, W - 15, H - 15], outline=NAVY, width=4)
d.rectangle([26, 26, W - 27, H - 27], outline=NAVY, width=2)

def center(y, text, font, fill):
    tw = d.textlength(text, font=font)
    d.text(((W - tw) / 2, y), text, font=font, fill=fill)

def fit(text, font_path, size, max_w):
    f = F(font_path, size)
    while d.textlength(text, font=f) > max_w and size > 10:
        size -= 2
        f = F(font_path, size)
    return f

center(48, "LEONIDA COUNTY  •  CIRCUIT COURT", fit("LEONIDA COUNTY  •  CIRCUIT COURT", SANS_B, 30, W - 120), NAVY)
center(88, "JURY DUTY", fit("JURY DUTY", SERIF_B, 76, W - 100), NAVY)
center(184, "SUMMONS", fit("SUMMONS", SERIF_B, 76, W - 100), RED)
d.line([90, 292, W - 90, 292], fill=RED, width=5)
center(306, "YOU ARE HEREBY SUMMONED TO APPEAR", fit("YOU ARE HEREBY SUMMONED TO APPEAR", SANS_B, 28, W - 100), INK)

# fields box 346..548
box = [70, 346, W - 70, 548]
d.rectangle(box, outline=NAVY, width=3)
rows = [
    ("JUROR:", "YOU  —  YES, YOU"),
    ("DATE:", "NOVEMBER 19, 2026  •  8:00 AM"),
    ("CASE:", "THE PEOPLE vs. THE 13-YEAR WAIT"),
    ("DEFENDANT:", "GRAND THEFT AUTO VI"),
]
ry = box[1] + 14
for label, val in rows:
    lf = F(SANS_B, 29)
    vf = fit(val, SANS_B, 29, W - 70 - 70 - d.textlength(label, font=lf) - 90)
    d.text((box[0] + 22, ry), label, font=lf, fill=RED)
    d.text((box[0] + 22 + d.textlength(label, font=lf) + 16, ry), val, font=vf, fill=NAVY)
    ry += 42

# reason box 720..832
rbox = [70, 720, W - 70, 832]
d.rectangle(rbox, outline=NAVY, width=3)
d.text((rbox[0] + 20, rbox[1] + 10), "REASON FOR EXCUSE:", font=F(SANS_B, 27), fill=RED)
f = fit("Juror will be playing GTA VI on launch day.", SANS, 28, W - 180)
center(rbox[1] + 46, "Juror will be playing GTA VI on launch day.", f, INK)
f2 = fit("Waited 4,811 days. Not missing it for a trial.", SANS, 28, W - 180)
center(rbox[1] + 80, "Waited 4,811 days. Not missing it for a trial.", f2, INK)

# bottom navy band 837..997
band_y = 837
d.rectangle([27, band_y, W - 27, H - 27], fill=NAVY)

def draw_ghost(cx, top, h):
    w = int(h * 0.72)
    x0 = cx - w // 2
    body = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    bd = ImageDraw.Draw(body)
    bd.ellipse([0, 0, w - 1, int(h * 0.62)], fill=(255, 255, 255, 255))
    bd.rectangle([0, int(h * 0.30), w - 1, int(h * 0.86)], fill=(255, 255, 255, 255))
    seg = w // 3
    for i in range(3):
        sx = i * seg
        bd.pieslice([sx, int(h * 0.72), sx + seg, h - 1], 0, 180, fill=(255, 255, 255, 255))
    ew, eh = int(w * 0.13), int(h * 0.17)
    for ex in (int(w * 0.30), int(w * 0.62)):
        bd.ellipse([ex, int(h * 0.30), ex + ew, int(h * 0.30) + eh], fill=(20, 20, 20, 255))
        bd.ellipse([ex + 3, int(h * 0.30) + 3, ex + 9, int(h * 0.30) + 9], fill=(255, 255, 255, 255))
    scx, scy, r = w // 2, int(h * 0.58), int(w * 0.16)
    star = [(scx, scy - r), (scx + r * 0.28, scy - r * 0.28), (scx + r, scy),
            (scx + r * 0.28, scy + r * 0.28), (scx, scy + r),
            (scx - r * 0.28, scy + r * 0.28), (scx - r, scy),
            (scx - r * 0.28, scy - r * 0.28)]
    bd.polygon(star, fill=(226, 0, 122, 255))
    img.paste(body, (x0, top), body)

mark = Image.open("/tmp/mark-1024.png").convert("RGBA")
mark.thumbnail((150, 132), Image.LANCZOS)
img.paste(mark, (62, band_y + 14), mark)
d.text((270, band_y + 14), "PAID BY MY AI AGENT", font=fit("PAID BY MY AI AGENT", SANS_B, 40, W - 300), fill=(255, 255, 255))
d.text((270, band_y + 66), "make.fun", font=fit("make.fun", SANS_B, 56, W - 300), fill=(255, 90, 180))
d.text((270, band_y + 128), "people + their AI agents earn real money", font=fit("people + their AI agents earn real money", SANS, 23, W - 300), fill=(200, 210, 235))

# red EXCUSED stamp, drawn LAST, in its own slot 566..712 (340x100, -8 deg)
stamp = Image.new("RGBA", (340, 100), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rectangle([5, 5, 335, 95], outline=(178, 34, 34, 235), width=5)
sd.rectangle([13, 13, 327, 87], outline=(178, 34, 34, 235), width=2)
sf = ImageFont.truetype(SERIF_B, 54)
sd.text((170 - sd.textlength("EXCUSED", font=sf) / 2, 22), "EXCUSED", font=sf, fill=(178, 34, 34, 235))
stamp = stamp.rotate(-8, expand=True, resample=Image.BICUBIC)
img.paste(stamp, ((W - stamp.width) // 2, 566), stamp)
print("stamp size after rotate:", stamp.size, "bottom:", 566 + stamp.height)

out = "/home/hatch/workspace/makefun/gta6-meme-x-01-v7-work/meme.png"
img.save(out)
print("saved", out, img.size)
img.resize((480, 480), Image.LANCZOS).save(
    "/home/hatch/workspace/makefun/gta6-meme-x-01-v7-work/meme-480.png")
print("saved 480 preview")
