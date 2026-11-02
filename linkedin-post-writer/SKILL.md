---
name: linkedin-post-writer
description: Write LinkedIn posts that sound like one real, keen person sharing what happened at work or reacting to industry news, in plain English that does not read as AI. Use when asked to write, draft, rewrite, fix or check a LinkedIn post, whether it is a story or lesson from the writer's own work or a take on news in GTM, sales, outbound, email deliverability, CRM or automation. Not for cold emails or LinkedIn DMs (cold-email-writer covers those).
---

# LinkedIn Post Writer

## What this is for

This skill writes LinkedIn posts that sound like a person, not a content machine.

Someone reading the post should hear a voice: a person who was actually there and would say the same thing over coffee. That voice is why people trust a post and believe it.

It covers the two kinds of post the writer does:

- **Experience.** Something that happened in their own work, and what they took from it.
- **News.** A reaction to something that changed in the industry, seen from their own desk.

## Assumptions (change these if they're wrong)

| Setting | Assumed |
|---|---|
| Writer | Vishal Ghosh, Growth Lead at SynthWeb |
| Topics | GTM, cold outbound, email deliverability, CRM and automation (HubSpot, GoHighLevel, Attio, n8n), AI in sales |
| Readers | Founders, sales and growth people, RevOps, startup marketers |
| Tone | Warm and curious by default. Can be excited, annoyed or unsure. Never preachy, never a guru. |
| Length | 80 to 220 words most days. Shorter is fine when the idea is small. |
| Format | No hashtags, no emoji, no em-dashes. Links go in the first comment, not the post. |
| Selling | None. A post is not an ad. |
| Language | Plain English. Short, common words. |

If `voice-samples.md` (next to this file) has real posts or messages in it, read them before writing. Real samples beat this guide. Copy the writer's habits, like how they open and how long their lines run. Never copy their sentences.

## Never make things up

Every fact in a post comes from the writer, or from a source you checked yourself.

- No invented numbers, results, clients, quotes or feelings.
- If a number would help and you don't have it, ask. Or write the post without it.
- Don't name clients, prospects or colleagues unless the writer says it's fine.
- For news, read the actual source, not just the headline, and note the date. If you can't confirm it, say so, or don't write the post.

## Get the raw material first

**Experience post.** You need:

1. The moment. One thing that happened: a day, a screen, a message, a meeting.
2. One detail only the writer would know. The real number, the exact error, the words someone used.
3. What they did or felt next.
4. What they'd tell a friend about it.

**News post.** You need:

1. The source link and its date.
2. What actually changed, in one plain line.
3. Who it hits, and how, in real life.
4. The writer's honest take, from their own work. "Not sure yet" counts.

If something's missing, ask. Three short questions at most. Don't fill the gaps with guesses.

## How to write it

1. **Find the point.** Write it in one plain sentence, just for you. If it needs two, it's two posts. Pick one.
2. **Start where the story starts**, or with the plain fact. No warm-up. Only the first two or three lines show before "...see more", so they have to make someone want the rest.
3. **Write it fast**, the way you'd tell a friend. Don't polish yet.
4. **Rough it up.** Do the pass further down. This is the step that makes it sound like a person.
5. **Run the checker** from this skill's folder: `python3 scripts/check_post.py post.txt`
6. **Read it out loud.** Any line you wouldn't say to someone's face, rewrite the way you'd say it.

Hand back:

- The post, ready to paste.
- A first comment, if there's a link or source. Tell the writer to pin it (LinkedIn brought pinned comments back in October 2026).
- One different first line, in case the first one doesn't land.

Don't explain the post or list what you changed. Just give it.

## The voice

How this person sounds:

- **Talks, doesn't announce.** "I sent 20 emails on Thursday." Not "I recently embarked on an outbound campaign."
- **Specific.** One real detail beats three claims. A tool name, a number, a time of day, the exact words.
- **Owns the mess.** Talks about the mistakes and the wrong calls. Shows the middle of the story, not only the win.
- **Has a view, holds it loosely.** Says what they think, and says when they're not sure.
- **Curious.** Asks questions they really want answered.
- **Funny in small doses**, mostly at their own expense.
- **Fair.** Gives credit by name. Argues with ideas, not people.

Use "I" and "you". Use contractions (I'm, didn't, it's). Use the words people say out loud.

## Rhythm: why AI text sounds like AI

AI text is too even. The sentences are all about the same length, the paragraphs match, things come in threes, and nearly every paragraph ends on a little punchline. Real people are lumpier than that.

- Mix sentence lengths. A long one that runs on for a bit, then a short one. Sometimes just a fragment.
- Make paragraphs different sizes. One line here, four there.
- Don't put one sentence on every line all the way down. That's a LinkedIn habit, not how anyone talks.
- Starting with "And" or "But" is fine. So is the odd comma splice, or an aside in brackets (like this). You can leave a thought open, too.
- Small slips are fine if that's how the writer really types ("ok", "gonna", a missing comma). Don't fake typos, though. And never get a name or a number wrong.

## Do and don't

| Don't | Do instead |
|---|---|
| Groups of three: "faster, cheaper, simpler" | Use the real number of things. If it really is three, make them very different lengths. |
| Mirror lines: "It's not X, it's Y." "Less X, more Y." | Say the true half and stop. |
| Noun-question reveals: "The result? Chaos." | Just say it: "It was chaos." |
| Colon reveals: "Here's what I learned:" | Start with the thing you learned. |
| Big words: leverage, unlock, elevate, seamless, robust, journey, game-changer | Small ones: use, get, lift, smooth, solid, the last year, big deal |
| AI glue: moreover, furthermore, it's worth noting, in today's fast-paced world | Cut it, or use "and", "also", "but". |
| A poster line at the end: "Consistency beats talent." | Stop on the last real thing, or ask a real question. |
| Bait: "Agree?", "Thoughts?", "Repost if...", "Follow for more" | A question you'd actually like answered, or nothing. |
| Fake drama: "This changes everything." "X is dead." | Say what changed and who it hits. |
| Big feelings: "I'm humbled", "I was speechless" | Say what you actually felt, plainly, if it matters. |
| The hero arc: struggle, big lesson, win | Keep the messy middle. It's fine if it isn't solved yet. |
| Lecturing: "You need to...", "Stop doing X" | "What I do now is...", "What tripped me up was..." |
| Rewriting the press release | One plain line on what changed, then your view. |
| Em-dashes | A full stop, a comma, or "and". |
| Hashtag walls, emoji bullets, fancy bold letters | Plain text. Fancy unicode letters also break screen readers. |
| Building every post the same way | Change the way in. Don't open two posts in a row the same way. |

## Experience posts

Pick one way in. These are shapes, not lines to reuse.

- **Mid-moment.** Drop the reader into the scene while it's happening.
- **The plain number.** Lead with the figure, then say what it meant.
- **What someone said.** A short, real quote.
- **The mistake.** Say what you got wrong, right in line one.

Then get to what actually happened, and what you did about it. If there's a lesson, say it once, plainly, near the end. Or let the story say it for you.

Watch for making yourself the hero, sad stories told for likes, the humblebrag ("so grateful this went viral"), and the same lesson said three different ways.

## News posts

1. **Check it.** Read the source and get the date. Make sure it's current and true.
2. **Say what changed** in one plain line, with who and when.
3. **Say who it hits**, in real terms. "If you send cold email from your main domain..."
4. **Give your take**, tied to something from your own work. That part is the post. Anyone can repeat the news.
5. **Say what you're doing about it**, or what you'd check this week. Skip this if you're not doing anything.
6. **Put the link and date in the first comment.**

Ways in: the plain fact, your gut reaction said straight, who should care, or the question it left you with.

Skip "BREAKING", "huge news" and "this changes everything". Don't predict the future like you're sure. Don't dunk on the company or on people who got caught out. And if you don't have a take of your own, don't post. The news is already everywhere.

## The rough-it-up pass

Do this after the first draft.

1. Read it out loud. Rewrite any line you wouldn't say to a friend.
2. Find any group of three. Cut one, or make them clearly uneven.
3. Find any mirror line. Keep the true half.
4. Check sentence lengths. If they're all alike, join two into one long one and cut another right down.
5. Check paragraph sizes. If they all match, change one.
6. Swap one general word for one real detail.
7. Check the last line. If it sounds like a poster, cut it.
8. Leave one thing a bit loose, like an aside in brackets or a question you don't answer.

## Format

- 80 to 220 words most days. LinkedIn's hard limit is 3,000 characters.
- The first two or three lines carry the post. Keep line one short enough to show on a phone.
- A blank line between paragraphs. Paragraphs of one to four lines, mixed.
- No markdown. LinkedIn doesn't render it, so `**bold**` shows up as stars.
- Lists only when it really is a list, and one list per post at most.
- No hashtags by default. If the writer wants them, three at most, at the very end.
- No emoji by default, and never as bullets.
- Tag people only if they're part of the story and won't mind.
- No pitch. If the story is about SynthWeb work, tell what happened, not what SynthWeb sells.

## The checker

`scripts/check_post.py` catches the common AI tells. It needs Python 3 and nothing else.

```bash
python3 scripts/check_post.py post.txt
python3 scripts/check_post.py mon.txt wed.txt fri.txt   # also flags posts that open or end the same way
pbpaste | python3 scripts/check_post.py -              # check what's on the clipboard (Mac)
```

- **FAIL** means fix it: em-dashes, banned phrases, mirror lines, noun-question reveals, bait endings, too many hashtags or emoji, markdown, more than 3,000 characters.
- **WARN** means look again: even rhythm, groups of three, one sentence per line, a long first line, links in the post, very short or very long posts.

It exits with code 1 if anything fails. Passing doesn't make a post good. It only means the obvious tells are gone. Reading it out loud still decides.

## Worked example 1: experience post

**Raw material** (real, from the writer's October 2026 outreach):

- Sent 20 cold emails on a Thursday morning.
- By late morning there were 4 replies: 1 bounce, 2 out-of-office, and 1 auto-reply saying the contact had left the company.
- The email had been rewritten three times for tone before it went out.

**The point, just for you:** check the person is still there before you polish the email.

**The post:**

```text
Sent 20 cold emails on Thursday morning.

By lunch I had four replies. All four were robots.

One address bounced. Two people were out of office. The fourth was an auto-reply telling me the person I'd written to had left the company.

That one bugged me. I'd rewritten that email three times to get the tone right, and it landed on an empty desk.

Out of office I don't mind, people come back. But a bounce or a "they've left" means my list was already out of date before I typed a word.

So next batch, before I write anything, I'm checking the person is still in the job and the address actually works. Boring. Should've done it this time.

Still waiting on the other 16. Hoping at least one of them is a human.
```

**Why it works:**

- It opens on a plain number. No warm-up.
- One picture does the work: "landed on an empty desk".
- There were three kinds of reply, so it's a real list of three, and the three lines are very different lengths.
- It owns the mistake ("Should've done it this time").
- It ends on where things stand, not on a lesson.
- No companies are named.

## Worked example 2: news post

**Raw material:**

- Source: [How LinkedIn is Continuing to Tackle AI Slop](https://news.linkedin.com/2026/how-linkedin-is-tackling-ai-slop), LinkedIn, 15 Sep 2026.
- What changed: a "Seems like AI slop" option on posts and comments, launched in August. Over 1 million members used it in the first two weeks. LinkedIn says its recent efforts cut views of AI slop by 40%. It's also replacing its "enhance your post" tool with ones that proofread and improve clarity without changing your voice.
- Who it hits: anyone posting generic AI output.
- Writer's take (assumed for this example, swap in the real one): glad about it. He's thrown out a pile of AI drafts himself lately. Thinks the fix is having something real to say. Unsure whether people who just write neatly will get caught.

**The post:**

```text
LinkedIn added a "Seems like AI slop" button to posts back in August.

Over a million people used it in the first two weeks. LinkedIn says its recent changes have cut views of slop by 40%.

A million people in two weeks is a lot of people who were sick of reading the same post with a new name on top.

I get it. Lately I've thrown out a pile of drafts for sounding like a machine wrote them. To be fair, a machine did.

LinkedIn is fine with AI help, by the way. It's swapping its "enhance your post" tool for ones that proofread and tidy up without changing your voice. For me the real fix is having something only I could say. Usually a number from my own week, or something I got wrong.

The part I'm not sure about is real people getting flagged for writing neatly. Some people just write like that.

Has anyone had a real post flagged yet? What was in it?
```

**First comment (pin it):**

```text
LinkedIn's own post on it, from 15 Sep 2026: https://news.linkedin.com/2026/how-linkedin-is-tackling-ai-slop
```

**Why it works:**

- The first line is the plain fact, with a date.
- The numbers come straight from the source, and the source sits in the pinned comment.
- The take comes from his own week, not from the article.
- It admits a doubt instead of pretending to know.
- It ends on a question he'd actually like answered.

## Worked example 3: fixing an AI draft

**Before** (this fails the checker):

```text
In today's fast-paced B2B landscape, cold email isn't dead. It's evolving.

Here's what I learned from sending 20 personalized emails:

1. Data quality matters.
2. Timing matters.
3. Persistence matters.

The result? A pipeline that actually converts. 🚀

Agree? 👇
```

What's wrong with it: an AI warm-up, a mirror line, a colon reveal, three matching list items, a noun-question reveal, two emoji and a bait ending. And nothing in it that only this writer could say.

**After:** worked example 1. Same 20 emails, but this time the post says what actually happened.
