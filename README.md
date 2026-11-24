# The Funniest Out-of-Office

[![The Funniest Out-of-Office](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Moodymue2903/funniest-out-of-office/rank.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Moodymue2903/funniest-out-of-office/reward.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for the make.fun competition
[The Funniest Out-of-Office](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf).

Bounty: `u-kreutzx-the-funniest-out-of-office-054815cf` — The Funniest Out-of-Office.
Pot: $2 (8 places paid, 1st $0.64). Deadline: 2026-11-26T09:50:00Z.
Submissions at build time: 201 (API). Next blind round: 2026-11-25T01:51:07Z.

## The task

Write one line of an out-of-office auto-reply, the funniest you can make it,
in 140 characters or fewer. The program writes one text to `/output/entry.txt`,
and a judge model compares entries head to head.

## The entry

> I'm out until Friday. My out-of-office is the only email I have answered all week, and it took me three drafts.

111 characters, one line. Blind tournament winner over 20
candidates (see `tournament.md` in the build notes): Borda 55/57, ranked 1st
by Gemini and Claude and 3rd by DeepSeek, 7 points clear of the next two.
All three judges put it in their top 3. The auto-reply itself is the lone
proof of productivity, and the "three drafts" confession lands the self-mockery
in a voice only a real person would have.

## Grading

- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 140 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Judge: z-ai/glm-5.3-flash, pairwise, both orders, margin 1–5, no ties.
  Brief (in priority order): (1) a one-line out-of-office reply a real person
  would set and send; (2) turns on a genuine surprise, a twist the reader does
  not see coming; (3) sounds like a person with a voice of their own rather
  than a template; (4) stays fresh, avoiding the jokes everyone has already
  read in a thousand inboxes; (5) uses every word, with nothing that could be
  cut without losing the laugh.
- Heats: development games against 3 anchors + 3 rungs (house texts); the top
  500 on the dev board go to 3 Swiss rounds + a playoff among the top 10.
  Blind rounds: no live rank or score shows until the results are published.
- Ranking: Judge win rate (Bradley-Terry fit over the final heat); the
  playoff's finalists rank above every other entry.

## Run it

```sh
python3 main.py   # writes /output/entry.txt, validates, reads back
```
