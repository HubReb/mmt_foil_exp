# top 15 no words

## 0 - 1
* 0 generally one "hotspot" per image and far fewer high attention areas per
  word
* 0 generally focused on one part of image same for all words
* 1 generally several "hotspots" (up to max. 1 hotspot per word)
* 1 generally far higher visual attention for each word in different locations
  of image
* 1 focus of attention shifts with each word
* 0 textual: always concentrated on <eos>
* 1 textual: always concentrated on visible token


## 1 - 2

* less hotspots for 2 than one (some have more hotspots than one, though)
* more distributed visual attention
* different parts of image, others the same
* no muster erkennbar
* textual: focussed on first/first two

## top 15 maximum image attention values

* image captioning generally works
* ironically more words do not necessarily improve translation (see 3 rem to
  4 rem)

### index 252

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| 0 rem | - |  des gens marchant dans une rue très fréquentée . |  people walking down a busy street. |
| 1 rem | man |  un homme en t-shirt blanc marchant sur le trottoir . |  a man in a white T-shirt walking on the sidewalk. |
| 2 rem | man walking |  un homme marchant dans la rue avec des gens en arrière-plan . | a man walking down the street with people in the background. |
| 3 rem | man walking down |  un homme marchant dans une rue très fréquentée . |  a man walking down a busy street. |
| 4 rem | man walking down | un homme marchant dans la rue avec un parapluie . | a man walking down the street with an umbrella. |
| 6 rem | man walking down street with reflection | un homme marchant dans la rue avec un homme . | a man walking down the street with a man.|
| 12 rem | man walking down street with reflection in glass | un homme marchant dans la rue avec du reflet en verre | a man walking down the street with glass reflection. |
| 20 rem |  man walking down street with reflection in glass |  un homme marchant dans la rue avec son reflet en verre |  man walking down the street with his glass reflection...
| complete | man walking down street with reflection in glass | un homme marchant dans une rue avec un reflet en verre | a man walking down a street with a glass reflection |


* more words do not guarantee a better translation (see 4 rem with "umbrella"
- there is no umbrella in the image
* 20 remaining words and complete are usually about the same as many sentence
have less than 20 words
* similarity of 0 rem and 3 rem is striking
* unsurpringly, 0 rem has the lowest image attention hotspots and its
attention is spread all over the image (each word in the sentence has
another "hot" area (0.030 is highest value))
* textual information is centered on <eos> (only non-unk token)
* 1 rem has textual information entirely centered on first token
* image attention increases to 0.05 and is still spread all over the image 
* attention values for 0 rem and 1 rem (image) are very similar (heatmap)
but per word attention is different (hot areas are more focused over
several words)
* 2 rem goes down to 0.04 for image attention and focuses most of the
textual attention on "walking" and some on "man"
* though there are still several hotspots and the heatmap is still similar
to 0 rem and 1 rem's, the per-word-image-attention is different
    * more focused on parts of the image 
    * only three hotspots and all in the same image part
    * all other words have far lower image attention than 0 rem and 1 rem
* 3 rem has high textual attention on first three words and higher maximum
image attention 0.08
    * heatmap is still similar 
    * more hotspots in the image 
    * different hotspots per word but a few are very close together and follow
      each other
    * per word image attention is more similar to 1 rem than 2 rem
* 4 rem has textual attention distributed over the 4 words, but nearly none on "down"
    * image attention stops at 0.08
    * overall fewer high attention spots than 3 rem 
    * smaller per-word image attention too with only a few hotspots in the
      sentence
    * image attention is now centered on the right side of the image
* 6 rem has textual attention distributed over all 6 words with "man" and
  reflection firmly black
    * image attention goes up to 0.10
    * overall pattern of heatmap similar to before
    * per-word image attention similar to 4 rem
    * three hotspots all on the right image side
* 12 rem has clear textual attention pattern from english to translated word
    * maximum image attention is now 0.25
    * heatmap somewhat similar but one hotspot now far higher valued
    * per-word image attention similar to before but with far higher values
    * hotspots no longer soly on the right side
* 20 rem has clear textual attention plot
    * maximum image attention is 0.14
    * similar to 12 rem
    * per-word image attention focusses on the same image parts as 12 rem
* complete has textual attention pattern as expected
    * max. image attention is 0.20
    * pattern slighty different from 20 rem but about the same spots with
      different values (smaller/higher)
    * per-word image attention similar to 20 rem but in parts far higher
      (marchant, dans)

### index 138

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| 0 rem | - | des hommes en tenues blanches jouent au football . | men in white suits are playing football. |
| 1 rem | two | deux hommes sont debout sur un terrain . | two men are standing on a field. |
| 2 rem | two baseball |  deux joueurs de baseball se battent . |  two baseball players are fighting. |
| 3 rem | two baseball players | deux joueurs de baseball s&apos; affrontent . | two baseball players go head-to-head. |
| 4 rem | two baseball players talking | deux joueurs de baseball parlant sur un terrain . | two baseball players talking on a field. |
| 6 rem | two baseball players talking on the | deux joueurs de baseball parlant sur le terrain | two baseball players talking on the field | 
| 12 rem | two baseball players talking on the field | deux joueurs de baseball parlant sur le terain |two baseball players talking on the field |
| 20 rem | two baseball players talking on the field | deux joueurs de baseball parlant sur le terain |two baseball players talking on the field |
| complete | two baseball players talking on the field | deux joueurs de baseball parlant sur le terain |two baseball players talking on the field |

* no difference in translation and textual attention from 6 rem up to complete
* rem 0 textual attention as before
   * image attention max. is 0.05
   * again many parts of the image highlighted (heatmap)
   * per-word image attentio is mostly centered on the lower half of the image
* rem 1 textual attention all on two
   * image attention up to 0.12
   * one hotspot but most of the heatmap shows some attention
   * per word image attention also focusses on the lower half of the image
   * only one hotspot most is high blue to yellow
* rem 2 textual attention most focussed on the two visible words, but some
  distributed on the unk tokens
   * image attention up to 0.06
   * again most attention on the bottom half
   * per-word attention is always hot on the bottom half
   * also attention on the top half, though only yellow, not red
* rem 3 textual attention again most distributed on the visible words but
  fitting, few on the unk
   * image attention up to 0.06
   * heatmap very similar to rem 2 (same spots, different values)
   * per-word image attention no longer just focussed on the lower half
     (hotspots) but also on the top left ("un")
* rem 4 textual attention same pattern as before
   * image attention up to 0.06 
   * different hotspots
       * more on the left
       * center gets far less attention
   * per word image attention has less hotspots overall
       * hotspots are no longer centered on almost one half of the image
       * smaller hotspots and more focus on the corner of the image (top left
         and bottom right)
       * center is now only light blue/green
* rem 6
   * image attention up to 0.10
   * most on bottom, one spot in center and one in center right (heatmap)
   * overall distribution of attention on heatmap close to rem 4
   * per-word image attention mostly hotspots on the bottom and bigger than rem
     4
   * only word without hotspot is "la" (only light green)
   * overall more high attention values for every word and only the edges of
     the hotspot move
* rem 12
   * image attention up to 0.20
   * per-word hotspots more distributed over image 
   * only two red zones ("terrain", bottom right - "<eos>" top left)
   * all other hotspot have same values as rem 6
   * only "baseball" has the same area attended
   * heatmap
       * reflects this
       * only one hotspot on the left center
       * some spots share both value and location (center)
* rem 20
   * image attention up to 0.12
   * per-word hotspots more distributed over image and generally smaller
   * red zones do not appear to be assziated with the translated word
     ("baseball" has hotspot on bottom right)
* complete
   * image attention up to 0.20
   * more hot areas than rem 12
   * model "prefers" top left area for per-word image attention
   * some words have attention on almost the entire image

### index 655

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - |  un homme sur un vélo saute d&apos; un rocher . | a man on a bicycle jumps off a rock. |
| rem 1 | pink |  un skieur nautique en train de faire du saut sur une montagne enneigée . | a water-skier jumping on a snow-covered mountain. |
| rem 2 | pink sky | un bateau de montagne et un chien blanc et blanc jouant dans la neige . |  a mountain boat and a white dog playing in the snow . | 
| rem 3 | pink sky on |  des montagnes russes sur un pont surplombant une montagne enneigée , des montagnes russes . |roller coaster on a bridge over a snow-covered mountain, roller coaster. |
| rem 4 | pink sky on a |  un oiseau rouge sur une montagne enneigée en ski de ski bleue et de montagnes |a red bird on a snowy blue ski mountain | 
| rem 6 | pink sky on a snowy day  | le ciel rose sur une colline enneigée avec des montagnes en arrière-plan . | the pink sky on a snowy hill with mountains in the background. |
| rem 12 | pink sky on a snowy day has tents on a platform .  | le ciel rose a des tentes a des tentes sur une plate-forme . | pink sky has tents on a platform. |
| rem 20 |  pink sky on a snowy day has tents on a platform .  |  un ciel rose sur une journée enneigée a des tentes sur une plate-forme . | a pink sky on a snowy day has tents on a platform. |
| rem 20 |  pink sky on a snowy day has tents on a platform .  |  des ciel rose lors d&apos; une journée enneigée a des tentes sur une plate-forme . | pink sky on a snowy day has tents on a platform. |

* it takes up to 6 words to arrive at a translation that has anything in common
  with the image
* interestingly, models trained on foil words succeed to translate this
  sentence whereas models trained with k ablatiions fail to translate correctly
* image captioning appears to literally ignore the image
* ground is white, hence snow-covered is not that far off
* there is no man, bird, bicyle, water-skier, boat, dog, roller coaster,
  mountain or hill in the image
* blue sky might be due to frequency of this combination
* interestingly, "pink" is simply ignored in the translations up to rem 6
* rem 0
    * textual attention as expected
    * image attention up to 0.08
    * most attention is on the left side of image
    * per-word attention very low except for "sur", "d'" and "rocher", all have
      attention on the left side
    * heatmap has hotspot in center, most more attended pixels on the left side
      and more small value pickels in center and very few on the right side
* rem 1
    * textual attention pink for the first two translated words, the others
      have none
    * image attention up to 0.14
    * again centered on the left
    * nearly every per-word attention is on the left with most of them high
      valued
    * <eos> is exception: center receives a bit of attention
    * heatmap has one hotspot on the left center, few light blue in the center
      and many slightly attented pixels in the center and the left.
rem 2
    * textual attention distributed over pink and sky for all french words,
      more evenly than for rem 1
    * hotspot in every per word attention image
    * max. image attention is 0.14
    * overall more attention
    * heatmap
        * one hotspot on the left hand side, one light blue
        * all others distributed over left and center and only slightly
          attended
* rem 3
    * textual attention more focussed now (more word to word attentions)
    * image attention max at 0.04 -> greatly decreased
    * mostly the same pixels with the same attention only the hotspots are
      entirely missing
    * again most per-word image attention focused on the left side
    * last two focussed on top left corner
* rem 4
    * textual attention slightly less focussed, again only the first few
      translated  words have textual attention
    * image attention at max 0.08
    * per-word image attention again focus on the left side  with left bottom corner for almost all words
        * attention only differs in strength
    * heatmap
        * reflects per-word attention
        * one hotspot on the left
        * most likely attended pixels once again in the center
        * very familiar to the heatmap of the other models
* rem 6
    * textual attention strong for "sky", "pink", "snowy" and "day" but almost
      non-existent for "on" and "a"
    * clearer mapping of <unk> tokens to translated words with small attention
      values
    * image attention at max 0.08
    * again focus on the left side but different hotspots
    * some more attended areas are on the top left now
    * heatmap
        * higher values on average now (more semi-hotspots)
        * still centered on the left side
        * more attention given to center and top (one almost hot-spot
          ("orange"))
* rem 12
    * textual attention strong for most of the sentence with word-to-word
      attention mappings
    * "on a snowy day has" have far weaker attention weights with "day" having
      almost no attention to any translated words
        * as "day" is not translated this is not surprising
    * image attention at max 0.12
    * image attention no longer centered on the left
        * hotspots are still mostly left with one bottom right
        * few are at the top of the image
    * heatmape
        * reflects change
        * still most warm spots on the left
        * hotspot now in the center
        * warm spots on the bottom right too
* rem 20
    * textual attention is now word-to-word for all words
    * image attention at max 0.08
    * heatmap
        * most warm pixels overlap
        * more hotspots than before
        * no longer centered on the left side at all
        * most hotspots are now in the center top and center bottom
    * per-word image attention has only a hotspot in the bottom left for the
      first translated word ("une")
    * far smaller image attentions for all the other words
    * except for hotspot the "warmest" spots are at the top
* complete
    * textual attention is still word-to-word but some words are less certain
      mapped ("sky", "a", "day", "has", "tents"), yet "pink" is stronger mapped
    * image attention at max 0.14
    * more hotspots than rem 20
    * all in the bottom left corner
    * heatmap
        * fewer hotspots
        * most on the left side
        * far fewer small attention spots (almost none)

### index 678

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| 0 rem | - | un homme est assis sur un banc devant un bâtiment . | a man is sitting on a bench in front of a building. |
| 1 rem | a | un homme est assis sur un banc devant un bâtiment . | a man is sitting on a bench in front of a building. |
| 2 rem | a monster | un camion truck est garé sur le trottoir . | there's a truck parked on the sidewalk. |
| 3 rem | a monster truck |  un monster truck passe devant un bâtiment bleu . |  a monster truck drives past a blue building. |
| 4 rem | a monster truck flies | un monster truck vole dans les airs pour faire une figure . |  a monster truck flies through the air to make a face.|
| 6 rem | a monster truck flies upside down | un camion truck vole la tête en bas un long de la rue . |  a truck truck flies upside down down along the street. |
| 12 rem | a monster truck flies upside down over a mound of dirt . |  un monster truck vole au-dessus d' un monticule de terre . |   a monster truck flies over a mound of dirt.|
| 20 rem | a monster truck flies upside down over a mound of dirt . | un monster truck vole la tête en bas par-dessus un monticule de terre . | a monster truck flies upside down over a mound of dirt. |
| complete | a monster truck flies upside down over a mound of dirt . | un monster truck vole la tête en bas sur un monticule de terre . | a monster truck flies upside down over a mound of dirt. |

* again up until rem 4 the translation has nothing in common with the image
* again easily solved foiled sentences perform bad with k ablations
* rem 0
    * textual attention as expected
    * image attention up to 0.04
    * most attention is at the top of image
    * per-word attention very low except for "un" and "homme" all have
      attention on the top
    * heatmap has hotspot in left center, most more attended pixels on the center top
      and more 0.02 pickels in center and quite a few on the right side with
      one almost hotspot
* rem 1
    * textual attention not on the one visible word but on "one" (mapped to
      one)
    * image attention up to 0.04
    * no longer centered on parts of the image rather heatmap has warm spots
      all over
    * nearly every per-word attention has its own region of the image
      highlighted with only "un" (second "un")having none
    * heatmap has three hotspot in center and right hand side
    * attention is more focussed on heatmap
        * more "warmer" pixels but overall fewer highlighted pixels
rem 2
    * textual attention has one-to-one mapping for "monster", but "a" has no
      attention!
    * hotspot or at least warm area in every per word attention image
    * max. image attention is 0.08
    * overall less attention
    * heatmap
        * one hotspot on the top half (center) far fewer light blue
        * still many lighter blue colored pixel
* rem 3
    * textual attention more focussed now (monster truck to monster truck)
    * image attention max at 0.030 -> greatly decreased, less than image
      captioning
    * mostly similar to heatmap of rem 1 but far more hotspots
    * attention "cluster" in top left corner, also visible for word images
* rem 4
    * textual attention far more  focussed, again only the first few
      translated  words have textual attention
    * image attention at max 0.07
    * per-word image attention again focus on the left side  with left bottom corner for almost all words and others top left corner
    * heatmap
        * reflects per-word attention
        * one hotspot on the left bottom
        * most focussed heatmap yet
* rem 6
    * tex. att. as expected
    * image attention at max 0.05
    * now focus on the top right corner
    * heatmap
        * similar values, different area of focus
        * still quite few slightly attended areas in the center
* rem 12
    * textual attention strong for most of the sentence with word-to-word
      attention mappings
    * image attention at max 0.14
    * image attention no longer present in every per-word image 
        * only one hotspot
    * heatmape
        * reflects change
        * far fewew warm spots
        * hotspot now on the left
* rem 20
    * textual attention is now word-to-word for all words
    * image attention at max 0.20
    * heatmap
        * barely any  warm pixels now
        * three warmer one (1 center, one left, one bottom center)
    * per-word image attention has only a hotspot in the bottom left for the
    * almost all images have the same hotspot
* complete
    * textual attention is still word-to-word but some words are less certain
    * image attention at max 0.30
    * barely any warm spots
    * image attention shifts with each word image 
    * two words have hotspots both are the same (word is both times "un")
    * heatmap
        * only one hotspot now
        * far fewer small attention spots (almost none)

### index 245

* about the same structure as index 678 except complete model goes up to 0.5
 max image attention in the end and rem 3 is not exceptionally low (max im.
 att. at 0.04 with rem 4 at 0.03)
* attention hotspots are in the center of the image this time
* rem 12 has higher im. max. than rem 20 (0.175 to 0.12)
* im. att. focusses on a handful of points starting at rem 12
* complete again has one hotspot and very few slightly warm areas
* rem 12 is only model that does not have most of its per-word image attentions in one
  spot
 
| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| 0 rem | - |  des gens marchent sur un trottoir . | people walking on a sidewalk. |
| 1 rem | several |  plusieurs personnes marchent sur un trottoir . |  several people are walking on a sidewalk. |
| 2 rem | several children | plusieurs enfants jouent au football sur un terrain de jeu . | several children are playing football on a playground. |
| 3 rem | several children playing |  plusieurs enfants jouant au hockey sur un terrain . |  several children playing hockey on a field. |
| 4 rem | several children playing on | plusieurs enfants jouant sur une balançoire par une journée ensoleillée . |  several children playing on a swing on a sunny day|
| 6 rem | several children playing on a court | plusieurs enfants jouant sur un terrain de tennis . |  several children playing on a tennis court. |
| 12 rem | several children playing on a court with balls |  plusieurs enfants jouant sur un terrain avec des ballons | several children playing on a field with balloons |
| 20 rem | several children playing on a court with balls |  plusieurs enfants jouant sur un terrain avec des ballons | several children playing on a field with balloons |
| complete | several children playing on a court with balls |  plusieurs enfants jouant sur un terrain avec des balles |  several children playing on a field with balls |

* interestingly, the first few translations are not utter nonsense -> image
  easier?
* it takes the complete sentence to get most of the translation right, yet both
  12 and 20 still translate balls with ballons (?)


### index 140

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| 0 rem | - |  une jeune fille en train de jouer avec un jouet . | a young girl playing with a toy.|
| 1 rem | little |   une petite fille blonde avec une robe rose. |   a little blonde girl in a pink dress |
| 2 rem | little girl | une petite fille en train de manger un livre . |a little girl eating a book.|
| 3 rem | little girl looking | une petite fille regardant un petit garçon . |  a little girl looking at a little boy. |
| 4 rem | little girl looking through | une petite fille regardant dans le bas . | a little girl looking down. |
| 6 rem | little girl looking through a dark | une petite fille regardant un petit garçon foncél | a little girl looking at a dark little boy. |
| 12 rem | little girl looking through a dark lense | une petite fille regardant dans un fond sombre | a little girl staring into a dark background |
| 20 rem |  little girl looking through a dark lense |  une petite fille regardant dans un endroit sombre | a little girl looking into a dark place |
| 20 rem |  little girl looking through a dark lense |  une petite fille regardant dans un <unk> sombre |a little girl staring into a dark funk... |

* note: lense is <unk> for model (does not appear in train)
* works better than the last two indices (caption has sth. to do with the
  translation right away)
* textual attention is as expected
* image attention follows the same pattern as before
* rem 6 and rem 12 are the only models having hotspots in almost every per-word
  image attention
* others are more distributed
* progression of heatmap follows the same schematic as before though the
  specific pixels are different
* the bigger k, the more hotspots (until k >= 6)
* hotspots are generally on the top of the image with very few exceptions
* rem 20 has max. im. att. of 0.20 and complete has 0.40
* rem 0 has 0.05, rem 1 0.06, rem 2 0.05, rem 3 0.07, rem 4 0.10, rem 6 0.10,
  rem 12 0.175
* this time foil words hurt model performance whereas k ablations do not result
  in other nonsense translations

### index 706

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | une personne en t-shirt rouge et pantalon noir marchant dans une rue . | a person in a red T-shirt and black pants walking down a street. |
| rem 1 | a | ne femme en t-shirt rouge marche dans la rue . | A woman in a red T-shirt is walking down the street. |
| rem 2 | a woman | une femme en veste noire marche sur un trottoir . | a woman in a black jacket is walking on the sidewalk. |
| rem 3 | a woman walking | une femme marchant dans une rue très fréquentée avec des bâtiments en arrière-plan . | a woman walking down a busy street with buildings in the background. |
| rem 4 | a woman walking down | une femme marchant dans une rue bordée de grands bâtiments de couleur vive . | a woman walking down a street lined with tall, brightly colored buildings. |
| rem 6 |  a woman walking down a street | une femme marchant dans une rue avec un grand bâtiment blanc . | a woman walking down a street with a big white building. |
| rem 12 |  a woman walking down a street lined with cars in the dark | une femme marchant dans une rue bordée de voitures en sombre . | a woman walking down a street lined with dark cars. |
| rem 20 |  a woman walking down a street lined with cars in the dark . |  une femme marchant dans une rue bordée de voitures en sombre . |  a woman walking down a street lined with dark cars. |
| complete |  a woman walking down a street lined with cars in the dark . |  une femme marchant dans une rue bordée de voitures dans la nuit . |  a woman walking down a street lined with cars in the night. |

* same progress as for last index: first translation fits the image, but only
  the complete model gets the entire sentence right
* one example that works for both ablation and foiled words
  (strange)
* detailed analysis
* rem 0
    * textual attention as expected
    * visual attention maxes out at 0.05
    * per-word attention is centered in the middle of the image
    * hotspots is always in the bottom right corner
    * later words have attention on the right
    * red at "en" and "marchant"
    * heatmap
        * reflects this
        * warm regions are mostly on the right half
        * hotspot (one deep red pixel is in bottom right corner)
        * one red pixel is in top right center
        * generally many light deep blue pixels all over the image (0.01
          attention)
* rem 1
    * textual attention mostly on the first three english tokens
    * most attention on first unk token to "une"
    * difference from person to woman is striking and as of yet not explained
      (maybe more woman in training data k=1?)
    * image attention shoots up to max 0.2 (x4!)
    * per-word attention again centered in the middle with bottom right corner
      as hotspot for "la" and "rue"
    * later words have attention on the right
    * heatmap
        * has hotspot in the middle of image (nearly all per-word image
          attentions color this region light blue to green, so unsurprising)
        * again a few lighter dark blue pixels (0.00 - 0.05 region, fits with
          rem 0)
        * overall structure similar to rem 0; difference in coloring stems from
          different total attention
* rem 2
    * greatly different to rem 1
    * textual attention is on "woman"-"femme" and first "<unk>"-"une"
    * "a" has no textual attention to any french word
    * image attention has a maximum of 0.04 (1/5 of rem 1)
    * per-word image attention is closer to rem 0 than rem 0
    * focus of image attention is now the right half of the image
    * first hotspot is top right corner ("une")
    * all other hotspots are bottom right corner and cover about one quarter of
      the entire image 
    * only words with non-hotspots are "femme" and "en" (only green to yellow
      on the right side of the image
    * "." and "<eos>" have light blue to green in top left quarter
    * heatmap
        * similar to rem 0
        * more yellow (0.03 pixels) generally in the center and the right side
        * two hotspots (right center about 4 from top, center 3 from bottom)
        * many slightly attended spots with light blue also on the left
* rem 3
    * textual attention on "woman"-"une"-"femme" with no textual attention on
      "a"
    * image attention per-word overall very similiar to rem 1
    * max. image attention at 0.06
    * per-word attention is actually different for each word both in value and
      region
    * most words have one quarter to half of the image covered in light blue to
      green
    * two yellow ("une" (bottom right half, about one fifth of the image), "une"
     (bottom right corner, one third of the image is covered))
    * one hotspot: "dans", bottom right corner
    * heatmap
        * one hotspot in the top right quarter (most of the words have some
          attention there)
        * two yellow (one slightly to the left of the middle center, one in the
          bottom right quarter)
        * many, many pixels slightly attended (0.01 - 0.02)
        * few pixels in light blue all over the image (0.02-0.03)
* rem 4
    * textual attention on first five tokens
    * mapping "a"-"une" for the first time
    * mapping "woman"-"femme", "walking"-"marchant" and "<unk>"-"dans"
    * visual attention is odd
    * max. image attention at 0.05
    * most per-word image attentions have no attention _at all_
    * only image attention is at "batiments"
    * hotspots covers bottom half of image with only left corner yellow
    * top right corner is entirely light blue
    * heatmap
        * somewhat reflects per-word attention
        * hotspot is in top right quarter
        * two yellow in the middle
        * only the edges are unattended
* rem 6
    * textual attention as expected
    * image attention maxes out at 0.10
    * per-word image attention generally on the center and right half of image,
      hotspot (1) in bottom right corner
    * yellow generally in top right corner
    * heatmap
        * most attention in center to top right
        * few warmer (0.04) in bottom right corner
        * most of the image attended (0.02)
* rem 12
    * textual attention as expected but with is not attended in any way
    * image attention maxes out at 0.10
    * per-word attention mostly on the top to top left corner 
    * two hotspots ("une", "<eos>") in top left corner
    * heatmap
        * reflects this
        * hotspot in top right corner
        * most warm spots (0.09 - 0.04) are in a diagonal line from top line
          (2 from left) to bottom (3 from bottom, 3 from right)
* rem 20
    * textual attention word-word mappings
    * image attention maxes out at 0.150
    * far more per-word attention now
    * several spots
        * "une": yellow with orange in middle in center of image 
        * "marchant": top right corner in red, light blue from hotspot to
          bottom left corner
        * "dans": top right quarter in red, light blue around the red
        * "une": yellow top right corner, light blue to the bottom left
        * "bordèe": yellow top right corner, rest of the right half in green
        * "en":  top right quarter in red, light blue around the red
        * "sombre": top quarter in yellow, light blue around the yellow
        * ".": top right quarter in red, light blue around the red
    * heatmap
        * reflects this

* complete
    * textual attention word-word mappings
    * image attention maxes out at 0.40
    * almost same  per-word attention as rem 20
    * hotspots are hotter
    * few differences in per-word mapping (second "une" now light blue in center, e.g.)
    * heatmap reflects this

### index 829

* same basic structure as index 678, different max. image attentions and
  hotspots but no surprises, most noteable difference
    * max. im. att at 0.10 for rem 20 and 0.25 for complete


| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | deux personnes sont assis sur un rocher , avec des sacs de sécurité et des lunettes de soleil . | two people are sitting on a rock, with safety bags and sunglasses.|
| rem 1 | an | un vieil homme en t-shirt rouge est assis sur un rocher au bord de l' eau .| An old man in a red T-shirt is sitting on a rock by the water's edge. |
| rem 2 | an older | un homme âgé avec un chapeau de sauvetage et un chapeau de natation sur un bateau .| an elderly man in a lifeguard's hat and a swimming hat on a boat. |
| rem 3 | an older woman | une femme âgée en robe rose est assise sur un rocher dans l&apos; eau . |...an elderly woman in a pink dress is sitting on a rock in the water.... |
| rem 4 | an older woman in | une femme âgée en robe rose est assise sur un rocher avec des fleurs et des vêtements . | an elderly woman in a pink dress is sitting on a rock with flowers and clothes. |
| rem 6 | an older woman in a bikini | une femme âgée en bikini est assise sur une planche de surf dans l&apos; océan . | an elderly woman in a bikini sits on a surfboard in the ocean. |
| rem 12 | an older woman in a bikini  is sunbathing on a rock by | une femme âgée en bikini se prend en photo sur un rocher au bord de l&apos; eau . | an elderly woman in a bikini takes a picture of herself on a rock at the water's edge. |
| rem 20 | an older woman in a bikini is sunbathing on a rock by the ocean . |  une femme âgée en bikini fait du soleil sur un rocher au bord de l&apos; océan . | an elderly woman in a bikini is sunbathing on a rock at the edge of the ocean. |
| complete | an older woman in a bikini is sunbathing on a rock by the ocean . | une femme âgée en bikini fait un tour de soleil sur un rocher au bord de l&apos; océan . | an elderly woman in a bikini is sunbathing on a rock by the ocean. |

* again it's impressive how many words the models need to arrive at a sensible
  translation
    * at least there is a pink _towel_ next to the woman (explaining where the
      model has "pink" from)
    * the makes sense structure is similar to 678
    * there are a few intersection with the content of the image long before
      the sentences is a somewhat reasonable describtion of the translation
    * again, the first few words actually make the translation _worse_
    * again, even giving the words does not mean they are translated correctly
      (rem 12)
    * again, the image attention is all over the place 
    * again, good example of it not working

### index 869

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | un homme avec une chemise à carreaux et un chapeau est assis sur un banc dans un parc . | a man in a plaid shirt and a hat is sitting on a bench in a park.|
| rem 1 | a |  un homme avec une chemise à carreaux et un chapeau est assis sur un banc dans un parc . |  man in a plaid shirt and a hat is sitting on a bench in a park.|
| rem 2 | a very |un homme très âgé avec un t-shirt blanc et un jean est assis sur un banc dans un parc . | a very old man in a white T-shirt and jeans is sitting on a park bench.|
| rem 3 | a very young |  un très jeune garçon en costume de camouflage est assis sur un banc dans un parc . | a very young boy in a camouflage suit is sitting on a bench in a park. |
| rem 4 | a very young boy | un très jeune garçon est assis sur un banc devant un mur recouvert de graffitis . | a very young boy sits on a bench in front of a graffiti-covered wall. |
| rem 6 | a very young boy plays with | un très jeune garçon joue avec un ballon de basket sur un tapis à côté d' un bâtiment . | a very young boy plays with a basketball on a carpet next to a building. |
| rem 12 | a very young boy plays with a skateboard on the front step  |  un très jeune garçon joue avec un skateboard sur la marche devant un bâtiment . |  a very young boy plays with a skateboard on the step in front of a building.. |
| rem 20 | a very young boy plays with a skateboard on the front step of a home . |  un très jeune garçon joue avec un skateboard sur la marche devant une maison . | a very young boy plays with a skateboard on the step in front of a house. |
| complete | a very young boy plays with a skateboard on the front step of a home .| un très jeune garçon joue avec un skateboard sur la marche devant une maison . | a very young boy plays with a skateboard on the step in front of a house. |

* the higher k gets the more accurate the models produce image
  description/translations.
* the knowledge revealed by higher k is used and integrated in the translation
* plays/sits confusion as long as plays is not given
* boy is not recognized until _young_ is given
* generally, this is one of the positive examples
* textual attention for all models as expected (word-to-word attentions
  progressing as more words are revealed)
* image attention fits to index 245 with rem 12 as the odd one (nearly all
  hotspots in the same place) and rem 20 having max. im. att of 0.20 and
  complete of 0.175
* greatest difference between the heatmaps is their value, not their warm
  pixels - though rem 1 is the one model that does not have the center top warm

### index 30

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | deux chiens courent dans la neige . | two dogs running through the snow. |
| rem 1 | two | deux chiens se battent sur la plage | two dogs fighting on the beach |
| rem 2 | two people | deux personnes font du ski sur la neige | two people skiing on the snow |
| rem 3 | two people walking |  deux personnes marchant dans la neige . |  two people walking in the snow. |
| rem 4 | two people walking on |  deux personnes marchant sur la plage . |  two people walking on the beach. |
| rem 6 | two people walking on the beach | deux personnes marchant sur la plage | two people walking on the beach |
| rem 12 | two people walking on the beach | deux personnes marchant sur la plage | two people walking on the beach |
| rem 20 | two people walking on the beach | deux personnes marchant sur la plage | two people walking on the beach |
| complete | two people walking on the beach | deux personnes marchant sur la plage | two people walking on the beach |

* translations/captions overall good (people are very small in the picture)
* dogs confusion is fixed with k=2
* same progression as for index 869
* textual attention is word-to-word right from rem 1 - no surprises here
* rem 3 and rem 4 have the smallest maximum image attention (0.05 and 0.04, rem
  0 has 0.08)
* most hotspots are on the bottom left quarter (where the two people are)
* differences in heatmaps is once again mostly for differences in given
  attention, only a few spots of where attention is given change
* rem 3 and rem 4 have lower max image attention and change the location of the
  hotspots more often 
* rem 3
    * not just lower left
    * rem 3 has lower left for the first 4 words, then lower right for "la",
      then again lower left and ends with bottom (all three very low attentions)
* rem 4
    * starts with top (hotspot)
    * then lower left (hotspot)
    * lower left (yellow)
    * lower left (light blue)
    * top left corner and right edge (light yellow)
    * bottom right (light yellow)
    * bottom left (light blue)
    * left edge (light blue)


### index 546

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | un homme en veste rouge joue de la guitare . |  a man in a red jacket plays the guitar |
| rem 1 | a |  un jeune homme en costume joue de la guitare . |  a young man in a suit plays the guitar. |
| rem 2 | a young | une jeune femme en robe de couleur vive joue de la guitare . | a young woman in a brightly colored dress plays the guitar. | 
| rem 3 | a young girl | une jeune fille en robe rouge se tient sur une balançoire . | a young girl in a red dress is standing on a swing.
| rem 4 | a young girl is | une jeune fille joue sur un terrain de jeux. | a young girl plays on a playground.
| rem 6 |  a young girl is holding a | une jeune fille tient un drapeau américain avec des arbres . | a young girl is holding an American flag with trees. |
| rem 12 | a young girl is holding a large stick while performing |  une jeune fille tient un grand bâton en jouant . |  a young girl holds a big stick while playing. | 
| rem 20 | a young girl is holding a large stick while performing |  une jeune fille tient un gros bâton en jouant . | a young girl holds a big stick while playing. |
| complete | a young girl is holding a large stick while performing |  une jeune fille tient un gros bâton tout en jouant . | a young girl holds a big stick while playing. |

* most of the sentence needs to be known for the models to translate somewhat
  correctly
* k <= 3 has next to nothing in common with the image
* "stick" has to be given for the model not to replace it with nonsense
* textual attention follows the same pattern as index 678
* image attentions differ from index 678
* most of the hotspots are in the top right corner of the image 
* again the complete model has max.im.att. of 0.175 while rem 20 has 0.20
* rem 0 - rem 3 have their hotspots all in the top right corner with a few
  yellow, but mostly light blue areas in the center, top right and bottom right
* both rem 0 and rem 20 have the most hotspots (5)
    * all in top right corner
* all models except the complete have their attention mostly on the right side
  of the picture
    * the complete model focuses its hotspots on the top left corner - where
      only a wall is (useless)
    * top right has the face of the girl
* heatmaps mostly differ in the value of attentions
    * exception is complete model: attention is transfered from right side of
      image to left side


### index 946

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | un homme en t-shirt noir et pantalon noir est debout devant un bâtiment avec des graffitis . | a man in a black T-shirt and black pants is standing in front of a building with graffiti. |
| rem 1 | two | deux hommes sont debout devant un bâtiment , l&apos; un en train de jouer avec un ballon de basket , l&apos; un en train de frapper . | Two men are standing in front of a building, one is playing with a basketball, one is kicking. |
| rem 2 | two woman | deux femmes en tenues de sécurité sont debout devant un bâtiment avec un mur en arrière-plan . | two women in security uniforms are standing in front of a building with a wall in the background. | 
| rem 3 | two women sit | deux femmes sont assises sur un banc , regardant un livre , tandis qu&apos; un homme est assis sur un banc . | Two women are sitting on a bench, looking at a book, while a man is sitting on a bench. |
| rem 4 | two woman sit on | deux femmes sont assises sur un banc , regardant un livre et un homme est debout derrière un mur en bois . | Two women are sitting on a bench, looking at a book and a man is standing behind a wooden wall.|
| rem 6 | two woman sit on a bench | deux femmes sont assises sur un banc devant un grand bâtiment avec un sac à dos rouge et un sac à dos . | two women are sitting on a bench in front of a large building with a red backpack and a backpack. |
| rem 12 | two women sit on a bench in front of a cafe , | deux femmes sont assises sur un banc devant un café , tandis qu&apos; un autre est assis . |Two women are sitting on a bench in front of a cafe, while another is sitting down.|
| rem 20 | two women sit on a bench in front of a cafe , while one holds up a device . | deux femmes sont assises sur un banc devant un café , tandis que l&apos; un tient un appareil .| two women are sitting on a bench in front of a cafe, while one is holding an appliance. |
| complete | two women sit on a bench in front of a cafe , while one holds up a device . |  deux femmes sont assises sur un banc devant un café , tandis que l&apos; une tient un appareil . | two women are sitting on a bench in front of a cafe, while one is holding an appliance. |

* again the entire sentence is needed to get the correct translation
* starting from k=3 is needed to get the first half of the sentence somewhat
  right
* again, image captioning drastically fails
* k<=2 is entirely false (nothing in common with the image)
* textual attention is word-to-word with no surprises
    * tends to be when small k are utterly wrong?
* image attention (maximum) is overall as expected
    * k=0 has 0.035 this time and most of the image is attended (what else?!)
    * there is always only one hotspot for all words
        * only one word has an attention visualisation with red in it
        * rem 0 :"batiment" diagonal cut over image, attended region is top
          right half, scatters attentio values of 0.005 over areas of image,
          e.g. left top corner for "des"
        * rem 1 : "," same as rem 0 (small attention to l' (0.02)
        * rem 2 : "femmes", right half of the image, stronger in top right
          corner
        * rem 3 : "regardant": top left corner
            * also attends with a small bit of attention "banc" (0.01)
        * rem 4: "un", right half
        * rem 6: "un", diagonal again, attended region is top left
        * rem 12: "un", diagonal again, attended region is top right
        * rem 20: "deux": left half
        * complete: "un": right half

    * heatmap correspond to this and greatly differ for each model
    * unclear on what causes this behaviour

### index 996

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | un homme avec une chemise rouge et une casquette noire tient un sac rouge et un chapeau de sécurité . |a man in a red shirt and a black cap is holding a red bag and a safety hat. |
| rem 1 | a | un homme avec une chemise blanche et une chemise blanche et une femme en t-shirt noir sont debout dans la rue . | a man in a white shirt and a woman in a black T-shirt are standing in the street. |
| rem 2 | a man |  un homme avec une casquette rouge et un chapeau de sécurité est assis sur un banc , regardant quelque chose dans un grand arbre . |  a man in a red cap and a safety hat is sitting on a bench, looking at something in a big tree. |
| rem 3 | a man with | un homme avec une veste rouge et un chapeau de cow-boy et une femme avec une veste rouge se tient debout devant un bâtiment . | a man in a red jacket and a cowboy hat and a woman in a red jacket are standing in front of a building. |
| rem 4 | a man with dark | un homme avec des cheveux foncés et une femme aux cheveux foncés se tenant à une table avec un micro et se fait prendre en photo . | a dark-haired man and a dark-haired woman standing at a table with a microphone and getting their picture taken. |
| rem 6 | a man with dark colored hair | un homme aux cheveux foncés et une chemise blanche et une casquette blanche tient un appareil photo tandis qu&apos; il marche dans un parc . | a dark-haired man in a white shirt and white cap is holding a camera as he walks through a park. |
| rem 12 | a man with dark colored hair and a short beard wearing a | un homme avec des cheveux de couleur foncés et une barbe et une barbe à motifs portant une chemise blanche , assis dans un parc . | man with dark hair and a patterned beard and beard wearing a white shirt, sitting in a park. |
| rem 20 | a man with dark colored hair and a short beard wearing a rust colored tshirt is eating spaghetti at a table | un homme avec des cheveux foncés et une petite barbe portant une chemise de couleur vive mange des poids dans un endroit . |  man with dark hair and a small beard wearing a brightly colored shirt eats weights in one place. |
| complete | a man with dark colored hair and a short beard wearing a rust colored tshirt is eating spaghetti at a table | un homme avec des cheveux colorés foncés et une petite barbe portant un <unk> de couleur vive mange des saucisses sur une table | a man with dark colored hair and a small beard with a brightly colored <unk> is eating sausages on a table. |

* similar to index 946
    * no translation is entirely right
    * again k < 6 has nothing to do with the image
    * the additional information is used and not ignored
    * textual attention is once again word-to-word
* image attention:
    * again each model has one hotspot, different for each model
    * image is not known, hence no in-depth analysis of chosen hotspots
    * complete model has max. im. att. 0.35
    * steady increase in im. max. attention (only exception rem 12 goes from
      0.175 to 0.12 for rem 20)
    * rem 1, 2, 3, 6, complete each have one hotspot and one slightly attended area
      per-word image
    * rem 12 and 20 have > 1 slightly attended area per-word image
    * heatmaps reflect this structure


### index 39

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | deux hommes travaillant sur des chaises . | two men working on chairs. |
| rem 1 | seamstress | un homme en train de manger un livre dans un restaurant . | a man eating a book in a restaurant. | 
| rem 2 | seamstress carefully |  un homme d&apos; âge moyen travaillant sur un projet . | a middle-aged man working on a project. |
| rem 3 | seamstress carefully performing | des chefs aux chefs préparent de la nourriture dans un restaurant . | from chefs to chefs preparing food in a restaurant. |
| rem 4 | seamstress carefully performing her | des étudiants vendent son travail . | some students are selling his work. |
| rem 6 | seamstress carefully performing her art . | un tableau rampant à ses coudre . |  picture crawling to his sewing. |
| rem 12 | seamstress carefully performing her art . |  voici quelque chose en forme d&apos; art . |  here's something in the form of an art form. | 
| rem 20 |  seamstress carefully performing her art . | des fléchettes effectuent sa création artistique . | darts perform his artistic creation. |
| complete | seamstress carefully performing her art . | des agriculteurs effectuant une œuvre d&apos; art . | farmers making a work of art. |


* all translations are utter and complete non-sense
* all translation have nothing in common with both the image and the source
  sentence
* textual attention is all over the place
* k<= 6: information given in the source sentence is ignored by the model
    * k=1: seamstress -> man
    * k=2: seamstress -> middle-aged man
    * ...
* textual attention is concerning
    * rem 1 maps seamstress to "un homme en"
    * rem 2 maps seamstress to "un homme" and to a lesser extent to "d' àge
      moyen"; carefully is mapped to "d' àge moyen"
    * rem 3 maps seamstress to "des" most, lesser to "chefs aux chefs"
      (performing is mapped to "chefs" most and carefully to "aux chefs")
    * and so on
    * very few words are mapped one-to-one (exception "her" (rem 20, rem 12,
      rem 4) and "art")
* image attention drastically different for each model, hardly anything in
  common
    * rem 0 has maximum image of 0.07
    * each model has different regions of hotspots and a different number of
      hotspots
        * rem 0:
            * 4 hotspots:
                * top left x1 ("deux")
                * 3x bottom right("des", "chaises", ".")
            * three yellows
                * 1x bottom left ("hommes")
                * 2x bottom right("travaillant", "sur")
        * rem 1:
            * 1 hotspot (top left)("un")
            * 3x yellow 
                * left, bottom right
                * top right ("homme", "manger", ".")
        * rem 2:
            *  4 hotspots
                *  "sur", bottom right quarter
                * "un", bottom right corner
                * "projet" , top right corner
                * <eos> top right corner
            * 2 yellow 
                * "un", bottom left
                * "moyen", top right quarter
            * rest has varying light blue green shades
        * rem 3:
            * 1 hotspot ("<eos>", top right corner)
            * no yellows
            * only light blue/green for 4 words
        * rem 4:
            * 1 hotspot ("son", bottom left corner)
            * all other words are yellow/green most of it in center of image to
              top right and bottom left corner
        * rem 6:
            * 4 hotspots 
                * "un", bottom right corner
                * "à", entire right half of image
                * "." top right corner
                * "<eos>" top right corner to top right middle
            * all other are yellow/yellow-to-orange (either center or bottom
               right - 1 bottom left)
        * rem 12:
            * 2 hotspots
                * "voici", bottom left corner
                * "art" top right corner
            * all light blue and one yellow ("en", top right corner-to-quarter)
        * rem 20:
            * 3 hotspots 
                * "des", bottom right corner
                * "effectuent", top right corner
                * "." top right corner
            * all others are yellow
        * complete:
            * 2 hotspots
                * "des" top right to middle right
                * "une", top right to middle right
            * two yellow
                * "œuvre" top right corner
                * "art" top right corner 
            * all others are green to yellow
        * heatmaps reflect this
            * center spots and top right quarter are generally colored warm
            (except rem 0 - no right top quarter), though to varying
              degrees (hotspots,  slightly above 0, ...)
            * all others depend on points written above
            * up untit rem 12 the center right spots are also given similar
              amounts of attention

### index 948 

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| rem 0 | - | une femme en t-shirt rouge et un homme en t-shirt rouge sont debout devant un mur de briques . | a woman in a red T-shirt and a man in a red T-shirt are standing in front of a brick wall. |
| rem 1 | a | une femme en robe rouge et blanche est debout devant une femme en robe rouge . | a woman in a red and white dress is standing in front of a woman in a red dress. |
| rem 2 | a woman | une femme avec un t-shirt rouge et un chapeau noir se tient à côté d&apos; un homme en veste rouge . | a woman in a red T-shirt and black hat stands next to a man in a red jacket. |
| rem 3 | a  women bending |  une femme se penchant en avant tandis qu&apos; un homme en t-shirt rouge se tient debout devant un micro . |  a woman leaning forward while a man in a red T-shirt stands in front of a microphone. |
| rem 4 | a women bending over | une femme se penche en arrière avec sa main gauche tandis qu&apos; elle se tient à côté d&apos; un autre homme en veste rouge . | a woman leans back with her left hand while she's standing next to another man in a red jacket. |
| rem 6 | a women bending over with a | un femme se penchant en avant avec un sac à dos à côté d&apos; un homme et un homme en veste de cuir . | a woman leaning forward with a backpack next to a man and a man in a leather jacket. |
| rem 12 | a women bending over with a kissing expression at a black |  une femme se penchant en avant avec une expression s&apos; appuyant sur une femme noire avec un homme plus âgé . |  a woman leaning forward with an expression based on a black woman with an older man. |
| rem 20 |  women bending over with a kissing expression at a black primate creature while standing on a harwood floor . | une femme se penchant en avant avec un embrassant pour une créature noire tandis qu&apos; il est debout sur un sol . | a woman leaning forward with a kiss for a black creature while he's standing on the floor. |
| complete |women bending over with a kissing expression at a black primate creature while standing on a harwood floor . | une femme se penchant en avant avec un baiser à une main , en train de s&apos; embrasser , en train d&apos; être en train de descendre d&apos; un sol <unk>  | a woman leaning forward with a one-handed kiss, kissing each other, going down from behind; a sol <unk> |

* translations are nonsense until the very end
* translation became grammatic nonsense with increased source words remains
* up until k=6 textual attention is word-to-word
* k >= 20: first 6 words are word-to-word, then most of the following have no
  clear mapping, complete is worst example of this
* image attention except for complete model is one hotspot, nothing else
* complete model has max. im. attentio of 0.4 with 3 hotspots and 5 warm
  regions (per-word images)
* k = 12 has max. image attention of 0.20, whereas k=20 only has 0.150
* heatmaps fit


# random replacements

* high image attention for complete model correlates with correct attention
* note: hotspot or high image attention generally refers to an attention value
  close to 0.1 - 0.4 (significantly higher than the other spots, but only about
  4x more, not 8-9x)
* in these cases, the translation is correct despite the foil words
   * lndex 138 is a good example for this 
       * hotspot is 0.12 to 0.20, lower total value correlates with
          overall more smaller attention spots (many light blue)
   * index 655 
       * 0.10 to 0.175
       * also 0.10 has the most small spots (replacement of nn)
   * index 678
       * 0.10 to 0.30
       * complete model has 0.30 and almost no small value spots
       * the smaller the hottest spot the more small value spots
       * complete random replacement has 0.10 and many small spots all over the
         image though slighty focused on the left
       * random jj replacement also has 0.10 and many small value spots though
         the hotter spots are more scattered all over the image
       * random pos has the most differnt hotspots for the words
   * replacing "players" with handkerchiefs/tubs does not foil the translation
       * textual attention takes a dive for handkerchief/tubs while image
         attention rises
       * tubs has more textual attention with less image attentions but arrives
         at the correct translation
   * verb replacement is more tricky (ranging for talking resuls in the
     translation working); image attention is clearly focused on the players on
     this part
   * prp replacement (on with via) results in in instead of on, but is better
     than expected
   * another good example is index 245
* once model itself is less certain of correct translation the foil words
  affect the translation (see index 140 for example)
   * hotspot 0.12 - 0.40 (complete model)
   * replacement of prp, in closest to heatmap of complete model, but far away
     from per word attention images
   * foil words than change the translations meaning (leaning instead of
     looking -> lying)
   * translation go entirely "of the hook" and have next to nothing in common
     with the english sentence (looking through -> hiking by replacing looking
     with all-white; replacing dark with key leads to the translation "green
     house" instead of dark <unk>)
   * image attention grealy increases (mean has far more high spots regardless
     of chosen replacement version)
      * all per word image attentions are close to the complete model except
        totally random replacement
          * many small attention spots per word instead of one concentrated
            area
   * fittingly, textual attention is always high
   * other good (and funny) examples of this are index 706
      * replacing cars with cartoons leads to the translation of cars to garbage
      * hotspots range from 0.08 (vb replacement) to 0.4 (complete), others
        range from 0.10 to 0.150
      * vb has the most all over the image attentions 
      * jj has the most confusing per word attentions: one image with attention
        nearly everywhere (l&apos; = l'), others are all no attention
   * index 829
      * attention hotspot 0.05 (vb replacement)to 0.25 (complete)
      * models share attention hotspots
   * index 869
      * attention hotspot 0.12 to 0.30 (jj replacement, 0.25 in replacement)
      * complete at 0.175
      * again some hotspots are shared
      * most models have similar word image attention pattern
* models are capable of dealing with foil words well in most cases (index 252
  is an excellent example of this - use in report?)
   * models always arrive at a reasonable translation despite the foil word
     with increased image attention
* model with nn replacement has more issues than the other models (index 30
  shows this perfectly as it is the only model not translating the sentence
  correctly as well as index 546)
   * index 30 has greater differences in maximum attention values than most
       * random 0.20
       * random pos 0.30
       * random nn 0.14
       * random vb 0.175
       * random jj 0.40
       * random prp 0.14
       * random in 0.30
       * complete 0.20
       * some higher areas are similar (bottom left corner)
       * high textual attention and low image attention do _not_ go together
       * no correlation between image attention and textual attention visible
         (from a value standpoint)
           * e.g. random has both smaller textual attention values and image
             attention values than random pos
   * index 546
       * attention hotspots 0.10 - 0.25; again unusal pattern
       * random 0.25
       * random pos 0.175
       * random nn 0.10
       * random vb 0.12
       * random jj 0.25
       * random prp 0.175
       * random in 0.10
       * complete 0.175
       * again no correlation between image and textual attention
   * replacement of jj often results in "funny" translation of sentences in which
  no jj has been replaced (index 829 "an older woman in a bikini is sunbathing
  on a rock by the ocean " is translated to "une femme âgée en bikini prend un rocher
  sur un rocher au bord de l' océan ." (an elderly woman in a bikini picks up
  a boulder on a rock by the ocean.)

* translations turn to utter nonsense for the images with the most visual
  attention if complete model itself is wrong (index 948 is utter nonsense, and
  foil models are actually better (read: closer to a grammatically corret
  sentence, content is also utter nonsense)
   * index 948
       * attention hotspots 0.14 - 0.40; again unusal pattern
       * random 0.14
       * random pos 0.175
       * random nn 0.20
       * random vb 0.25
       * random jj 0.35
       * random prp 0.30
       * random in 0.35
       * complete 0.40
       * again no correlation between image and textual attention
       * very few hotspots (2-3) shared between models (heatmaps)
* prp replacement leads to some utter nonsense sentences (index 996 repeats the
  second half of the sentences several times, while all other models deal with
  it mostly correctly)
   * index 996
       * 0.10 - 0.40
       * random 0.10
       * random pos 0.12
       * random nn 0.12
       * random vb 0.175
       * random jj 0.12
       * random prp 0.40
       * random in 0.30
       * complete 0.20
       * again no correlation between image and textual attention
       * high visual attentions for prp replacement
* for index 39: seamstress carefully performing her art . <eos>

| model | foiled sentence | hypothesis | translation |
|-------|------------|-----------------|-------------|
| complete | - |  agriculteurs effectuant une œuvre d' art . | making a work of art |
| random replacement | seamstress carefully performing her containing | une couturière faisant soigneusement son métier  | rescuer doing an activity |
| random replacement (pos) |  seamstress carefully performing her slip | diverses chirurgiens qu&apos; elle fait tourner son éventail | various surgeons that she spins her fan. |
| replacement of nn | stake carefully performing her art | des hommes examinent son œuvre . | men examine his work. |
| random replacement of vb | seamstress carefully building her art  |  des indiens montrent quelque chose du doigt | Indians are pointing a finger |
| random replacement of jj | seamstress carefully building her art | on voit une art faisant du art sur sa œuvre . | we see art making art on his work. |
| random replacement of prp | seamstress carefully performing my art |  ces nageuses se produisant dans leur œuvre . |   these swimmers performing in their work. | 
| random replacement of in | seamstress carefully performing her art |  il y a pas l&apos; art qu&apos; il effectue un art . | it's not the art he's doing an art. |

* complete model fails to translate this sentence correctly
* replacement thoroughly confuses model -> trained models perform considerably
  worse on sentences even without replacement (in and jj)
* yet meteor score barely decreases -> only few sentences result in chaos
* high image attention correlates with nonsense translations!
* image attention
    * 0.20 - 0.35
    * random 0.20
    * random pos 0.25
    * random nn 0.10
    * random vb 0.25
    * random jj 0.20
    * random prp 0.30
    * random in 0.25
    * complete 0.20
* note: prp replacement leads to a few high attention values (image)
* replacement of same pos:
    * results in high attention of different part of the image
    * low textual attentions (ironicaly drastically false translated words
      have highest textual attention)
    * model uses image attention but does not arrive at a translation befitting the image (e. g. elle (she) has image
      attention on the right hand side on a sack of some kind)
* replacement of nn
    * work better as in the translation can be roughly drafted from the image ("men" has image attention on the womans face, "work" on the
      table with the utensilien, etc.)
    *  has the most differentiated mean image attention of all replacements:
      instead of two or three hotspots the attention is centered on the middle with
      a few far "lighter" patches and one hotspot (see heatmap)
    * higher textual attention than complete model (model is more certain than
      complete model)
* replacement of vb:
    * textual attention only high on the first two words
    * image attention low except for two hotspots
    * image attention per words generally in the top right corner and once low
      left corner
    * even low textual attention on <eos>
    * most likely rooted in utterly wrong translation
* replacement of jj:
    * higher textual attention than replacement of vb
    * most of the sentence with low textual attention
    * image attention not centered on one spot
    * image attention still has two hotspots and few more attended image areas
      (mean)
    * art is confused with the window
    * faisant has image attention on the woman
* replacement of prp
    * focused textual attention
    * only non-focused on prp 
    * carefully is omitted from sentence and has low textual attention
    * seamstress is linked to these (???? no reason visible) with image
      attention on the stuff left of the woman (most likely reason for
      translation)
    * nageuses (swimmers) is focused on the woman's face
    * though sentence is nonsense, textual attention is higher than for 
      complete model
* replacement of in
    * seamstress is translated with the entire first half of the sentence (il
      y a pas l' (there is no )
    * other words have textual attention to the second half of the sentence
    * more hotspots of attention in the second sentence half
    * both translations art are hotspots (image) but differently focused
        * first on woman's face
        * second on the window
    * model appears to be the most confused in this example
* tagging has quite a few tagging errors -> differention by replacing only same
  pos-tags is noisy
* replacing does not result in focus on image
* replaced word is translated
* furthermore (in case of nn replacement) the image attention goes down on this
  word not up
    * "influence" on image attention on model behaviour is exact opposite of
      expected behaviour
* for some overall image attenion goes up, but textual attention always wins
  over information extracted from the image
    * idea: replace more than one word?
    * same as k-ablations, possibly
* replacing NN leads to the greatest increase of image attention 
* replacing by pos tag (total) results in greatest decrease of textual
  attention 
    * combination with barely increasing image attention: highest increase of
      uncertainty in this case
* replacing IN barely changes anything, simply translation of foil word
* 17 is great example of wrong translations
    * image attentions: 0.10 - 0.40
    * random 0.175
    * random pos 0.25
    * random nn 0.10
    * random vb 0.20
    * random jj 0.175
    * random prp 0.30
    * random in 0.12
    * complete 0.40
* 706 is great example of replacing words not mattering (cars -> cartoons: Who
  cares?) and mattering (walking -> used; translated correctly; increase in
  image attention for this word (on a car), down -> so,
  translated correctly, drastic increase of image attention for this word)
* 254 good example of it working
    * image attentions: 0.08 - 0.20
    * random 0.10
    * random pos 0.08
    * random nn 0.12
    * random vb 0.12
    * random jj 0.175
    * random prp 0.14
    * random in 0.12
    * complete 0.20


# careful: random has some indices messed up (+1 in script)
