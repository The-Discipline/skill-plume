# Intents

Intent is a field of the brief, never a format. It sets the default CTA, whether the angles step runs, and the question the Reader critic answers.

## inform
- **Angles:** yes
- **CTA default:** none or soft (a question that keeps the conversation going, at most)
- **Reader asks:** What did I learn? What will I remember tomorrow?

## convince
- **Angles:** yes
- **CTA default:** soft
- **Reader asks:** Was I convinced? By what exactly? What objection is left?

## ask
- **Angles:** no
- **CTA default:** explicit, one request, with a date if relevant
- **Reader asks:** Do I know exactly what is asked of me, by when, and why me?

## announce
- **Angles:** yes
- **CTA default:** explicit (sign up, try, read, book)
- **Reader asks:** Do I know what it is, who it is for, and what to do now?

## reply
- **Angles:** no
- **CTA default:** none
- **Reader asks:** Does this answer what I actually said? Does it add something?

## relationship
Thanks, congratulations, news, keeping in touch.
- **Angles:** no
- **CTA default:** none
- **Reader asks:** Does this sound like a person, and does it feel addressed to me?

## Rules for all intents
- One CTA at most.
- The CTA's destination comes from the pack's `facts.md`. Missing: use a placeholder.
- The hook default comes from the family. Intents `ask`, `reply` and `relationship` lower it to `light` or `none`.
