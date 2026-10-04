#!/usr/bin/env python3
"""
AHMII LABS · profile visuals
Fetches the contribution calendar through the GitHub GraphQL API and writes two
self-contained gold SVGs (no third-party image services involved):

    dist/contribution-skyline.svg   3D contribution skyline (last 12 months)
    dist/activity-graph.svg         activity line graph (last 30 days)

Usage:  python scripts/generate_profile.py --user mrz3ron3x --out dist
        python scripts/generate_profile.py --mock --out dist     (offline preview)
Auth:   GITHUB_TOKEN (or PROFILE_TOKEN) environment variable.
Only the Python standard library is used.
"""
import argparse, datetime as dt, json, math, os, random, sys, urllib.request
from html import escape

GOLD, GOLD_L, GOLD_D, TEXT, DIM = "#C9A961", "#EBD9A0", "#8a6d2b", "#D9D4C7", "#8f8878"
SERIF = "Cinzel,'Trajan Pro',Georgia,'Times New Roman',serif"
SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"

QUERY = """
query($login:String!){
  user(login:$login){
    contributionsCollection{
      contributionCalendar{
        totalContributions
        weeks{ contributionDays{ date contributionCount weekday } }
      }
    }
  }
}"""


# ───────────────────────── data ─────────────────────────
def fetch_days(user, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": user}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "ahmii-labs-profile"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload or not payload.get("data", {}).get("user"):
        sys.exit(f"GraphQL error: {payload.get('errors') or 'user not found'}")
    cal = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return [(dt.date.fromisoformat(d["date"]), d["contributionCount"], d["weekday"])
            for w in cal["weeks"] for d in w["contributionDays"]]


def mock_days():
    random.seed(7)
    end = dt.date.today()
    start = end - dt.timedelta(days=364)
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)  # back to Sunday
    out, d = [], start
    while d <= end:
        c = random.choice([0, 0, 0, 1, 2, 3, 5, 8, 13]) if random.random() < .55 else 0
        out.append((d, c, (d.weekday() + 1) % 7))
        d += dt.timedelta(days=1)
    return out


def stats(days):
    today = dt.date.today()
    counted = [(d, c) for d, c, _ in days if d <= today]
    total = sum(c for _, c in counted)
    longest = cur = 0
    for _, c in counted:
        cur = cur + 1 if c else 0
        longest = max(longest, cur)
    cur = 0
    for _, c in reversed(counted):
        if c:
            cur += 1
        elif cur or _ != today:  # today with 0 doesn't break a streak yet
            if _ == today:
                continue
            break
    best = max((c for _, c in counted), default=0)
    return total, cur, longest, best


def level(c, mx):
    if c <= 0: return 0
    q = c / max(mx, 1)
    return 1 if q <= .25 else 2 if q <= .5 else 3 if q <= .75 else 4


LV = {0: "#2b2318", 1: "#5a4a29", 2: "#8c7339", 3: "#b8994f", 4: "#e6c978"}


def shade(hex_, f):
    h = hex_.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    if f >= 0: r, g, b = (int(v + (255 - v) * f) for v in (r, g, b))
    else: r, g, b = (int(v * (1 + f)) for v in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def num(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


STYLE = """<style>
.bar{animation:grow 1.1s cubic-bezier(.2,.8,.2,1) both;transform-box:fill-box;transform-origin:50% 100%}
@keyframes grow{from{transform:scaleY(0);opacity:0}to{transform:scaleY(1);opacity:1}}
.glint{animation:glint 5s ease-in-out infinite;opacity:0}
@keyframes glint{0%,100%{opacity:0}6%{opacity:.6}14%{opacity:0}}
.scan{animation:scan 7s linear infinite}
@keyframes scan{from{transform:translateX(0)}to{transform:translateX(960px)}}
.draw{stroke-dasharray:1;stroke-dashoffset:0;animation:draw 2.2s ease-out both}
@keyframes draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
.fade{animation:fade 1.6s ease-out .8s both}
@keyframes fade{from{opacity:0}to{opacity:1}}
.pt{animation:pop .5s ease-out both;transform-box:fill-box;transform-origin:center}
@keyframes pop{from{transform:scale(0);opacity:0}to{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""


def shell(w, h, label, inner, defs=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title>{STYLE}
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0A0A0A"/><stop offset=".5" stop-color="#1b150e"/><stop offset="1" stop-color="#0A0A0A"/></linearGradient>
<linearGradient id="bd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOLD}"/><stop offset=".5" stop-color="#4a3c20"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOLD_D}"/><stop offset=".5" stop-color="{GOLD_L}"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
<pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{GOLD}" stroke-opacity=".07"/></pattern>
{defs}
</defs>
<rect width="{w}" height="{h}" rx="16" fill="url(#bg)"/>
<rect width="{w}" height="{h}" rx="16" fill="url(#grid)"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="15" fill="none" stroke="url(#bd)" stroke-width="1.4"/>
<rect x="9" y="9" width="{w-18}" height="{h-18}" rx="10" fill="none" stroke="{GOLD}" stroke-opacity=".2"/>
{inner}
</svg>"""


def header(w, title, right):
    return (f'<text x="34" y="46" font-family="{SERIF}" font-weight="700" font-size="17" letter-spacing="4" fill="{GOLD}">{escape(title)}</text>'
            f'<text x="{w-34}" y="45" text-anchor="end" font-family="{SANS}" font-size="12" letter-spacing="1.5" fill="{DIM}">{escape(right)}</text>'
            f'<rect x="34" y="58" width="{w-68}" height="1.2" fill="url(#gold)" opacity=".55"/>')


# ───────────────────── skyline (oblique 3D bars) ─────────────────────
def skyline(days):
    today = dt.date.today()
    days = [x for x in days if x[0] <= today]
    first = days[0][0]
    week_of = lambda d: (d - first).days // 7 + (0 if (first.weekday() + 1) % 7 == 0 else 0)
    # normalise: weekday 0=Sunday .. 6=Saturday, week index from first column
    start_sun = first - dt.timedelta(days=(first.weekday() + 1) % 7)
    cells = [((d - start_sun).days // 7, wd, c, d) for d, c, wd in days]
    nweeks = max(x[0] for x in cells) + 1
    mx = max((c for *_, c, _ in cells), default=0)
    total, cur, longest, best = stats(days)

    W, H = 900, 300
    a, bw = 15.0, 11.4          # week pitch / bar width
    ox, oy = 7.0, 5.6           # day pitch (up-right)
    tx, ty = 5.4, 4.4           # bar thickness vector
    maxh = 66
    left = (W - (a * (nweeks - 1) + bw + ox * 6 + tx)) / 2
    base = 190                  # baseline of the front row

    def hgt(c):
        return 3.0 if c == 0 else 8 + (maxh - 8) * math.sqrt(c / mx)

    out = [header(W, "CONTRIBUTION SKYLINE", f"{total:,} CONTRIBUTIONS · LAST 12 MONTHS")]
    out.append(f'<ellipse cx="{W/2}" cy="{base-18}" rx="{W*0.42}" ry="46" fill="{GOLD}" opacity=".06"/>')
    bars = []
    for row in range(6, -1, -1):
        for wk, wd, c, d in sorted((x for x in cells if x[1] == row), key=lambda x: x[0]):
            x = left + wk * a + row * ox
            y = base - row * oy
            h = hgt(c)
            lv = level(c, mx)
            col = LV[lv]
            top, side = shade(col, .18), shade(col, -.38)
            tip = f"{d.isoformat()} · {c} contribution{'s' if c != 1 else ''}"
            topd = f"M{num(x)} {num(y-h)}h{bw}l{tx} {-ty}h{-bw}z"
            if c == 0:
                bars.append(f'<path d="{topd}" fill="{col}" opacity=".85"><title>{tip}</title></path>')
                continue
            delay = round(wk * 0.016 + (6 - row) * 0.02, 3)
            g = (f'<g class="bar" style="animation-delay:{delay}s"><title>{tip}</title>'
                 f'<path d="M{num(x)} {num(y)}h{bw}v{num(-h)}h{-bw}z" fill="{col}"/>'
                 f'<path d="M{num(x+bw)} {num(y)}l{tx} {-ty}v{num(-h)}l{-tx} {ty}z" fill="{side}"/>'
                 f'<path d="{topd}" fill="{top}"/>'
                 f'<path class="glint" style="animation-delay:{round(wk*0.07,2)}s" d="{topd}" fill="#fff6d8"/></g>')
            bars.append(g)
    out += bars
    # moving light scan across the field
    out.append(f'<clipPath id="field"><rect x="20" y="64" width="{W-40}" height="{base-64+16}"/></clipPath>'
               f'<g clip-path="url(#field)"><g transform="skewX(-24)"><rect class="scan" x="-140" y="64" width="90" height="170" fill="url(#sweep)"/></g></g>')
    # month labels
    seen = set()
    for wk, wd, c, d in cells:
        if wd == 0 and d.day <= 7 and (d.year, d.month) not in seen and wk < nweeks - 1:
            seen.add((d.year, d.month))
            out.append(f'<text x="{num(left+wk*a)}" y="{base+22}" font-family="{SANS}" font-size="10" letter-spacing="1.5" fill="{DIM}">{d.strftime("%b").upper()}</text>')
    # footer stats
    out.append(f'<rect x="34" y="228" width="{W-68}" height="1" fill="{GOLD}" opacity=".18"/>')
    items = [("CURRENT STREAK", f"{cur} day{'s' if cur != 1 else ''}"), ("LONGEST STREAK", f"{longest} day{'s' if longest != 1 else ''}"),
             ("BEST DAY", f"{best} commit{'s' if best != 1 else ''}"), ("TOTAL", f"{total:,}")]
    for i, (k, v) in enumerate(items):
        x = 34 + i * 165
        out.append(f'<text x="{x}" y="256" font-family="{SANS}" font-size="9" font-weight="700" letter-spacing="2.4" fill="{GOLD}">{k}</text>'
                   f'<text x="{x}" y="278" font-family="{SERIF}" font-weight="700" font-size="18" fill="{GOLD_L}">{escape(v)}</text>')
    # legend
    lx = W - 34 - 5 * 18 - 70
    out.append(f'<text x="{lx}" y="272" text-anchor="end" font-family="{SANS}" font-size="10" fill="{DIM}">Less</text>')
    for i in range(5):
        out.append(f'<rect x="{lx+8+i*18}" y="262" width="12" height="12" rx="2" fill="{LV[i]}"/>')
    out.append(f'<text x="{lx+8+5*18+4}" y="272" font-family="{SANS}" font-size="10" fill="{DIM}">More</text>')
    defs = (f'<linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOLD_L}" stop-opacity="0"/>'
            f'<stop offset=".5" stop-color="{GOLD_L}" stop-opacity=".22"/><stop offset="1" stop-color="{GOLD_L}" stop-opacity="0"/></linearGradient>')
    return shell(W, H, f"Contribution skyline — {total} contributions in the last 12 months", "".join(out), defs)


# ───────────────────── activity line graph ─────────────────────
def smooth(pts, lo=-1e9, hi=1e9):
    d = f"M{num(pts[0][0])} {num(pts[0][1])}"
    for i in range(len(pts) - 1):
        p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        c1 = (c1[0], min(max(c1[1], lo), hi)); c2 = (c2[0], min(max(c2[1], lo), hi))
        d += f"C{num(c1[0])} {num(c1[1])} {num(c2[0])} {num(c2[1])} {num(p2[0])} {num(p2[1])}"
    return d


def activity(days, span=30):
    today = dt.date.today()
    rows = [(d, c) for d, c, _ in days if d <= today][-span:]
    W, H = 900, 300
    x0, x1, y0, y1 = 70, W - 40, 92, 232
    vals = [c for _, c in rows]
    top = max(max(vals), 4)
    top = int(math.ceil(top / 4.0) * 4)
    px = lambda i: x0 + (x1 - x0) * i / (len(rows) - 1)
    py = lambda v: y1 - (y1 - y0) * v / top
    pts = [(px(i), py(v)) for i, v in enumerate(vals)]
    line = smooth(pts, y0, y1)
    area = line + f"L{num(x1)} {y1}L{num(x0)} {y1}Z"
    total = sum(vals)
    out = [header(W, "ACTIVITY", f"LAST {span} DAYS · {total} CONTRIBUTIONS")]
    for k in range(5):
        v = top * k / 4
        y = py(v)
        out.append(f'<path d="M{x0} {num(y)}H{x1}" stroke="{GOLD}" stroke-opacity="{.22 if k == 0 else .08}" {"" if k == 0 else "stroke-dasharray=\"3 6\""}/>'
                   f'<text x="{x0-12}" y="{num(y+4)}" text-anchor="end" font-family="{SANS}" font-size="10" fill="{DIM}">{int(v)}</text>')
    step = 5
    for i in range(0, len(rows), step):
        out.append(f'<text x="{num(px(i))}" y="{y1+22}" text-anchor="middle" font-family="{SANS}" font-size="10" letter-spacing="1" fill="{DIM}">{rows[i][0].strftime("%b %d").upper()}</text>')
    out.append(f'<path class="fade" d="{area}" fill="url(#ar)"/>')
    out.append(f'<path d="{line}" fill="none" stroke="{GOLD}" stroke-width="6" stroke-opacity=".18" stroke-linecap="round" pathLength="1" class="draw"/>')
    out.append(f'<path d="{line}" fill="none" stroke="url(#gold)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" pathLength="1" class="draw"/>')
    peak = vals.index(max(vals)) if max(vals) else None
    for i, (x, y) in enumerate(pts):
        if vals[i] == 0 and i not in (0, len(pts) - 1):
            continue
        r = 4.6 if i == peak else 3
        out.append(f'<circle class="pt" style="animation-delay:{round(1.2+i*0.03,2)}s" cx="{num(x)}" cy="{num(y)}" r="{r}" fill="#0A0A0A" stroke="{GOLD_L}" stroke-width="1.6"><title>{rows[i][0].isoformat()} · {vals[i]}</title></circle>')
    if peak is not None:
        x, y = pts[peak]
        bx = min(max(x, x0 + 40), x1 - 40)
        out.append(f'<g class="fade"><rect x="{num(bx-34)}" y="{num(y-34)}" width="68" height="20" rx="10" fill="#14100b" stroke="{GOLD}" stroke-opacity=".6"/>'
                   f'<text x="{num(bx)}" y="{num(y-20)}" text-anchor="middle" font-family="{SANS}" font-size="10" font-weight="700" letter-spacing="1.5" fill="{GOLD_L}">PEAK {vals[peak]}</text></g>')
    defs = (f'<linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GOLD}" stop-opacity=".38"/>'
            f'<stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></linearGradient>')
    return shell(W, H, f"Activity graph — {total} contributions in the last {span} days", "".join(out), defs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default=os.environ.get("GH_USER", ""))
    ap.add_argument("--out", default="dist")
    ap.add_argument("--mock", action="store_true")
    a = ap.parse_args()
    if a.mock:
        days = mock_days()
    else:
        token = os.environ.get("PROFILE_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not (a.user and token):
            sys.exit("need --user and GITHUB_TOKEN")
        days = fetch_days(a.user, token)
    os.makedirs(a.out, exist_ok=True)
    for name, svg in (("contribution-skyline.svg", skyline(days)), ("activity-graph.svg", activity(days))):
        with open(os.path.join(a.out, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"wrote {name} ({len(svg)//1024} KB)")


if __name__ == "__main__":
    main()
