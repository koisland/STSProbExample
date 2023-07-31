# Probability Exercise for Slay the Spire
Source: https://www.haskellforall.com/2021/06/probability-for-slay-spire-fanatics.html


### Questions
1. Next turn I draw 5 cards.
    * What is the likelihood that I draw at least 3 Strikes if:
        * There are 7 cards left in the deck, 4 of which are Strikes.

> Answer: 5 / 7 ≈ **71% chance**

2. One Neow bonus to lose 7 max HP to select from 1 of 3 random rare cards.
    * What is the chance that I get at least 1 of 6 of the 17 possible rare cards?

> Answer: 103 / 136 ≈ **76% chance**

### Details
Universal Set:
* `U` = All cards in deck.

Subsets (Can overlap)
* `A` = Cards drawn.
* `B` = Cards that are desired.

Use `~` as complement (opposite)
* `~A` = Cards not drawn
* `~B` = Cards that are not desired

Create 4 non-overlapping (disjoint) sets by intersecting sets (`∩`).
1. `A ∩ B`
    * Cards drawn that are desired.
2. `~A ∩ B`
    * Cards not drawn that are desired.
3. `A ∩ ~B`
    * Cards drawn that are not desired.
4. `~A ∩ ~B`
    * Cards not drawn that are not desired.

Use `|S|` to denote size of set `S` and `!` to denote factorial.

Probability of two subsets of fixed sizes overlapping by a given size is:

```
                |A|! * |~A|! * |B|! * |~B|!
p = ────────────────────────────────────────────────────
    |A ∩ B|! * |A ∩ ~B|! * |~A ∩ B|! * |~A ∩ ~B|! * |U|!
```
```
    {The number of correct hands}
p = ──────────────────────────────
    {The number of possible hands}
```

`|A|`, `|~A|`, `|B|`, `|~B|` are derived from `|A ∩ B|`, `|~A ∩ B|`, `|A ∩ ~B|`, `|~A ∩ ~B|`.
```
|A| = |A ∩ B| + |A ∩ ~B|
|~A| = |~A ∩ B| + |~A ∩ ~B|
|B| = |A ∩ B| + |~A ∩  B|
|~B| = |A ∩ ~B| + |~A ∩ ~B|
|U| = |A ∩ B| + |A ∩ ~B| + |~A ∩ B| + |~A ∩ ~B|
```

Now, rephrasing the question:
* I have a deck containing `|B|` desirable cards out of `|U|` total cards. If I draw `|A|` cards from that deck, what is the chance that I draw (exactly / at least / at most) `|A ∩ B|` desirable cards?
