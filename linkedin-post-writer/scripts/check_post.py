#!/usr/bin/env python3
"""Check a LinkedIn post for the usual AI tells.

Usage:
    python3 check_post.py post.txt [more.txt ...]
    pbpaste | python3 check_post.py -

FAIL means fix it. WARN means look again.
Exit code 1 if any post has a FAIL, otherwise 0.
With several files it also warns when posts open or end the same way.

Passing does not make a post good. Read it out loud.
"""

import re
import statistics
import sys

BANNED = [
    (r"\bdelv(?:e|es|ed|ing)\b", "say 'look at' or 'dig into'"),
    (r"\btapestry\b|\brealm\b|\bparadigm|\bholistic|\bsynerg|\bmyriad\b|\bplethora\b|\bbustling\b", "cut it"),
    (r"\btestament to\b|\bunderscor(?:e|es|ed|ing)\b", "say what it shows"),
    (r"\bembark(?:s|ed|ing)?\b|\bmeticulous(?:ly)?\b|\bintricate\b", "use a plain word"),
    (r"\bin today'?s\b|\bfast-paced\b|\bever-(?:evolving|changing)\b|\bin the (?:world|realm) of\b", "cut the warm-up, start with the point"),
    (r"\bgame[- ]?chang(?:er|ers|ing)\b", "say what changed"),
    (r"\bunlock(?:s|ed|ing)?\b|\bunleash|\bsupercharg|\bskyrocket", "say what happened, with the real number"),
    (r"\brevolutioni[sz]|\bempower", "use a plain verb: help, let, change"),
    (r"\bseamless(?:ly)?\b", "say 'smooth' or 'easy'"),
    (r"\bcutting[- ]edge\b|\bbest[- ]in[- ]class\b|\bworld[- ]class\b|\bnext[- ]level\b|\bthought leader", "cut it"),
    (r"\bleverag(?:e|es|ed|ing)\b|\butili[sz](?:e|es|ed|ing)\b|\bharness(?:ing)? the\b", "say 'use'"),
    (r"\bactionable\b|\bvalue[- ]add\b", "say what it does"),
    (r"\bmove the needle\b|\blow[- ]hanging fruit\b|\bcircle back\b|\btouch base\b|\bnorth star\b|\bdeep dive\b", "say it in plain words"),
    (r"\b(?:my|this|the|your) journey\b", "say what happened"),
    (r"\bfoster(?:s|ed|ing)?\b|\bspearhead", "say 'build' or 'lead'"),
    (r"\bmoreover\b|\bfurthermore\b|^\s*additionally\b", "cut it, or use 'and' or 'also'"),
    (r"\bit'?s (?:important|worth) (?:to note|noting)\b|\bworth noting\b", "just say it"),
    (r"\bin (?:conclusion|summary)\b|\bto sum up\b|\bat the end of the day\b", "just stop"),
    (r"\bthat being said\b|\bwith that said\b|\bhaving said that\b|\bneedless to say\b", "use 'but', or cut it"),
    (r"\blet that sink in\b|\bread that again\b", "trust the reader"),
    (r"\bhere'?s (?:the thing|the kicker|the truth|the deal|what i learned)\b", "start with the point itself"),
    (r"\bhere'?s (?:why|how)\s*[:.]?\s*$", "just give the reason"),
    (r"\bplot twist\b|\bspoiler alert\b|\bbuckle up\b|\blet'?s dive\b|\blet'?s talk about\b|\bwithout further ado\b", "cut the warm-up"),
    (r"\bthe (?:truth|reality) is\b|\blet'?s be honest\b|\breal talk\b|\bno fluff\b", "just say it"),
    (r"\bunpopular opinion\b|\bhot take\b", "just give the opinion"),
    (r"\b(?:no ?one|nobody) (?:is )?talk(?:s|ing) about\b|\bmost people don'?t (?:realize|realise|know)\b", "cut it"),
    (r"\b(?:uncomfortable|harsh) truth\b|\bthis is your sign\b|\b(?:gentle|friendly) reminder\b", "cut it"),
    (r"\bin a world where\b|\bimagine a world\b|\bever wondered\b|\bpicture this\b", "start with the real thing"),
    (r"\b(?:i'?m|i am) (?:so |beyond |super )?(?:humbled|thrilled|honou?red|excited to (?:share|announce))\b", "say it plainly, if at all"),
    (r"\band (?:that'?s|that is) (?:ok|okay|the point)\b", "cut it"),
    (r"\bfollow (?:me )?for more\b|\brepost (?:if|this)\b|\bdrop a comment\b|\bcomment below\b|\blet me know in the comments\b", "no bait"),
    (r"\bon steroids\b|\brockstar\b|\bninja\b|\bguru\b|\bcrushing it\b", "cut it"),
    (r"\bmy guess is\b", "ask it as a question instead"),
    (r"\bdrop in a pod\b|\bcarry the work\b|\bend[- ]to[- ]end\b|\bquick one\b", "say what you actually do"),
]

SOFT = [
    r"\blandscape\b", r"\brobust\b", r"\bcrucial\b", r"\bpivotal\b", r"\bvital\b",
    r"\bscalable\b", r"\bstreamlin\w*", r"\btakeaways?\b", r"\bultimately\b",
    r"\bin essence\b", r"\bsimply put\b", r"\bdouble down\b", r"\bis dead\b",
    r"\bhustle\b", r"\bnevertheless\b", r"\belevat(?:e|es|ed|ing)\b",
    r"\bnavigat(?:e|es|ed|ing)\b", r"\binvaluable\b", r"\bshowcas\w*",
    r"\binsights?\b", r"\bnuanced?\b",
]

MIRRORS = [
    r"\b(?:it|this|that)(?:'s| is| was) not\b[^.?!\n]{1,60}[,.;]\s*(?:it|this|that)(?:'s| is| was)\b",
    r"\b(?:isn'?t|wasn'?t|is not|was not)\b[^.?!\n]{1,60}[,.;]\s*(?:it|this|that)(?:'s| is| was)\b",
    r"\bnot (?:just|only|merely) [^.?!\n]{1,40},? but\b",
    r"\bnot because\b[^.?!\n]{1,80}[,.;]\s*(?:but )?because\b",
    r"\bless \w+(?: \w+)?, more \w+",
    r"\bthe more\b[^.?!\n]{1,40}, the (?:more|less|better|worse)\b",
    r"(?:^|(?<=[.!?])\s)\s*not [^.?!\n]{1,30}\.\s+not [^.?!\n]{1,30}\.",
]

NOUN_QUESTION = r"(?:^|(?<=[.!?])\s)\s*(?:and |but |so )?(?:the|my|our|your|his|her|their)\s+(?:\w+\s+){0,2}\w+\?"
COLON_REVEAL = r"^\s*(?:the )?(?:lesson|takeaway|result|bottom line|moral|secret|kicker|catch)s?\s*:"
BAIT_END = r"^(?:agree|thoughts|any thoughts|what do you think|what are your thoughts|what'?s your take|agree or disagree|am i wrong|sound familiar|who else)\b"
POSTER_END = r"\b(?:beats?|wins?|matters?|is everything|is king)\b"

DASH = re.compile("\u2014|\\s\u2013\\s| -- ")
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF]")
FANCY = re.compile("[\U0001D400-\U0001D7FF]")
BULLET_SYMBOL = re.compile("^\\s*(?:\u2192|->|=>|\u27A1|\u25B6|\u2714|\u2705|\U0001F449|\U0001F539|\U0001F538)", re.M)
MARKDOWN = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__|^#{1,6} |\[[^\]\n]+\]\(", re.M)
HASHTAG = re.compile(r"(?<![\w&/])#[A-Za-z]\w*")
LIST_MARK = re.compile(r"^\s*(?:\d+[.)]|[-\u2022*])\s+")
WORD = re.compile(r"[A-Za-z0-9']+")
ITEM = r"[\w'-]+(?: [\w'-]+){0,3}"
TRIPLES = [
    re.compile(rf"({ITEM}), ({ITEM}),? (?:and|or) ({ITEM})\b", re.I),
    re.compile(rf"({ITEM}), ({ITEM}), ({ITEM})[.!?]", re.I),
]
FLAGS = re.I | re.M


def normalize(text):
    for old, new in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\r\n", "\n")):
        text = text.replace(old, new)
    return text.strip()


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def words(s):
    return WORD.findall(s)


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def sentences(block):
    out = []
    for line in block.splitlines():
        line = LIST_MARK.sub("", line).strip()
        out += [s.strip() for s in re.split(r"(?<=[.!?])\s+", line) if WORD.search(s)]
    return out


def shown(m):
    return " ".join(m.group(0).split())


def check(raw):
    """Return (fails, warns, word_count) for one post."""
    text = normalize(raw)
    fails, warns = [], []
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    body = [ln for ln in lines if not re.fullmatch(r"(?:#\w+\s*)+", ln)]
    last = body[-1] if body else ""

    for pattern, fix in BANNED:
        for m in re.finditer(pattern, text, FLAGS):
            fails.append(f'line {line_of(text, m.start())}: "{shown(m)}" -> {fix}')
    for pattern in MIRRORS:
        for m in re.finditer(pattern, text, FLAGS):
            fails.append(f'line {line_of(text, m.end())}: mirror line "{shown(m)}" -> keep the true half')
    for m in re.finditer(NOUN_QUESTION, text, FLAGS):
        fails.append(f'line {line_of(text, m.end())}: noun-question reveal "{shown(m)}" -> just say it')
    for m in re.finditer(COLON_REVEAL, text, FLAGS):
        fails.append(f'line {line_of(text, m.start())}: colon reveal "{shown(m)}" -> start with the point')
    for m in DASH.finditer(text):
        fails.append(f"line {line_of(text, m.start())}: dash -> use a full stop, a comma or 'and'")
    if MARKDOWN.search(text):
        fails.append("markdown -> LinkedIn shows it as raw symbols, use plain text")
    if FANCY.search(text):
        fails.append("fancy unicode letters -> screen readers can't read them, use plain text")
    emoji = EMOJI.findall(text)
    if len(emoji) > 1:
        fails.append(f"{len(emoji)} emoji -> none, or one that really earns its place")
    if BULLET_SYMBOL.search(text):
        fails.append("arrow or emoji bullets -> they read as a template, use plain lines")
    tags = HASHTAG.findall(text)
    if len(tags) > 3:
        fails.append(f"{len(tags)} hashtags -> three at most, at the very end")
    if len(text) > 3000:
        fails.append(f"{len(text)} characters -> LinkedIn's limit is 3,000")
    if last and len(words(last)) <= 6 and re.match(BAIT_END, last, re.I):
        fails.append(f'bait ending "{last}" -> ask a real question, or just stop')

    for pattern in SOFT:
        for m in re.finditer(pattern, text, FLAGS):
            warns.append(f'line {line_of(text, m.start())}: "{shown(m)}" -> is there a plainer word?')
    if lines and len(lines[0]) > 140:
        warns.append(f"first line is {len(lines[0])} characters -> it may get cut before '...see more' on a phone")
    if re.search(r"https?://|www\.", text):
        warns.append("link in the post -> put it in the first comment and pin it")
    if text.count("!") > 1:
        warns.append(f"{text.count('!')} exclamation marks -> one at most")
    if ";" in text:
        warns.append("semicolon -> reads formal, use a full stop")
    if any(HASHTAG.search(ln) for ln in body):
        warns.append("hashtags mid-post -> move them to the very end, or drop them")
    personal = re.search(r"\b(?:i|i'm|i've|me|my|we|our)\b", last, re.I)
    if last and len(words(last)) <= 8 and re.search(POSTER_END, last, re.I) and not personal:
        warns.append(f'last line sounds like a poster: "{last}" -> stop on the last real thing')
    n_words = len(words(text))
    if n_words > 250:
        warns.append(f"{n_words} words -> long, most good posts here run 80 to 220")
    elif n_words < 40:
        warns.append(f"{n_words} words -> short, fine if the idea is small")

    sents = [s for p in paragraphs(text) for s in sentences(p)]
    sizes = [len(words(s)) for s in sents]
    if len(sizes) >= 6:
        mean = statistics.mean(sizes)
        if statistics.pstdev(sizes) / mean < 0.35:
            warns.append(f"sentences are all about {mean:.0f} words -> join two into one long one, cut another right down")
        if min(sizes) > 5:
            warns.append("no short sentence -> add one of five words or fewer")
        if max(sizes) < 13:
            warns.append("no long sentence -> let one run on a bit")
    seen = {"start": -9, "end": -9, "frag": -9}
    for i in range(len(sents) - 2):
        trio = [words(s) for s in sents[i:i + 3]]
        found = {
            "start": (len({t[0].lower() for t in trio}) == 1, f'three sentences in a row start with "{trio[0][0]}" -> change one'),
            "end": (len({t[-1].lower() for t in trio}) == 1, f'three sentences in a row end with "{trio[0][-1]}" -> change one'),
            "frag": (all(len(t) <= 3 for t in trio), 'three tiny fragments in a row ("' + " ".join(sents[i:i + 3]) + '") -> reads like a slogan'),
        }
        for key, (hit, message) in found.items():
            if hit and i > seen[key] + 2:
                warns.append(message)
                seen[key] = i
    paras = paragraphs(text)
    counts = [len(sentences(p)) for p in paras]
    if len(paras) >= 6 and counts.count(1) / len(paras) >= 0.8:
        warns.append("one sentence per paragraph all the way down -> group some lines together")
    elif len(paras) >= 5 and len(set(counts)) == 1:
        warns.append(f"every paragraph has {counts[0]} sentence(s) -> make one longer or shorter")
    for s in sents:
        for rx in TRIPLES:
            m = rx.search(s)
            if m and abs(len(m.group(2).split()) - len(m.group(3).split())) <= 1:
                warns.append(f'group of three "{m.group(0)}" -> fine if it is a real list, cut one if it is just rhythm')
                break
    runs, run = [], 0
    for ln in text.splitlines():
        if LIST_MARK.match(ln):
            run += 1
        elif ln.strip():
            runs.append(run)
            run = 0
    runs.append(run)
    if 3 in runs:
        warns.append("a list of exactly three -> is three the real count?")

    return list(dict.fromkeys(fails)), list(dict.fromkeys(warns)), n_words


def cross_check(posts):
    warns, opens, ends = [], {}, {}
    for name, raw in posts:
        text = normalize(raw)
        lines = [ln.strip().lower() for ln in text.splitlines() if ln.strip()]
        first = " ".join(w.lower() for w in words(text)[:3])
        last = lines[-1] if lines else ""
        if first and first in opens:
            warns.append(f'{name} opens like {opens[first]} ("{first}...") -> change the way in')
        if last and last in ends:
            warns.append(f"{name} ends like {ends[last]} -> change the ending")
        opens.setdefault(first, name)
        ends.setdefault(last, name)
    return warns


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        return 2
    posts = []
    for arg in argv[1:]:
        if arg == "-":
            posts.append(("stdin", sys.stdin.read()))
        else:
            with open(arg, encoding="utf-8") as f:
                posts.append((arg, f.read()))
    failed = 0
    for name, raw in posts:
        fails, warns, n_words = check(raw)
        print(f"\n{name} ({n_words} words)")
        for msg in fails:
            print(f"  FAIL  {msg}")
        for msg in warns:
            print(f"  WARN  {msg}")
        if not fails and not warns:
            print("  PASS  no obvious AI tells. Now read it out loud.")
        failed += bool(fails)
    across = cross_check(posts) if len(posts) > 1 else []
    if across:
        print("\nAcross posts")
        for msg in across:
            print(f"  WARN  {msg}")
    print(f"\n{len(posts) - failed} of {len(posts)} post(s) clear the hard rules.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
