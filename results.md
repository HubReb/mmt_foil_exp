# top 15 no words

# bis zu index 245 for rem 6 gekommen
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

### index 17
| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| 0 | - | un homme en train de jouer avec des instruments de musique | ein Mann, der mit Musikinstrumenten spielt. |
| 1 | two | deux hommes jouent au tennis |  two men play tennis |
| 2 | two young men | deux jeunes hommes jouent au basket | two young men are playing basketball |
| 3 | two young men| deux jeunes hommes jouant au tennis | two young men playing tennis | 
| 4 | two young men wrestling | deux jeunes hommes se battant. | two young men fighting. |
| 6 | two young men wrestling competitively | deux jeunes hommes se battant | two young men fighting |
| 12 | two young men wrestling competitively | 
| 20 | two young men wrestling competitively |
| complete | two young men wrestling competitively |


* 0: visual attentions generally low
    * un is focused of head of one man
    * homme is also focused on head of the same man but value is lesser
    * all other attentions have nothing to do with the translation
* 1: textual: two to deux
    * visual attentions generally higher
    * un is focused of head of one man
    * homme is also focused on head of the same man
    * jouent is focused on the background and middle of man on the right
    * tennis is focused on left man's legs,  middle of man on the right, legs
      of right man and top right background
* 2: textual: two to deux, young to jeunes, tiniest bit of two to basket, rest
  among remaining french sentence
    * visual attention on un jeunes is low
    * first hotspot is on hommes: right of the first men's face
    * jouent is on the two men: head to toe
    * au basket has a hotspot on the left man's legs; basket also has light
      blue spot right to the left man's face
* 3: textual: two to deux, young to jeunes, men to hommes, rest distributed over remaining
  french sentence
    * deux has red hotspot on left man's middle
    * jeunes has light blue  on right man's folded leg
    * hommes as light blue  on right man's head and folded leg
    * jouant has four light blue spots: left man's leg, under right man's head,
      right of left man's head and right man's folded leg
    * au has yellow/red hotspot on  right man's folded leg
    * tennis has hotspot to the right of left man's head and light blue on its
      left, on left man's leg and right man's folded leg

* 4: textual: two to deux, young to jeunes, men to hommes,for wrestling: se battant,
     competitively, rest to remaining french sentence.
    * deux has red hotspot on the right of the right man (nothing there)
    * jeunes light blue (all on background spots)
    * dark blue around the men
    * se dark blue around the men and light blue on the left man's upper legs
    * battant:dark blue around the men and light blue on the right man's left
      leg
* 6
    * textual word-word except for wrestling: se battant, competitively
    * visual: deux has red hotspot on chest of right man
    * jeunes has yellow-red hotspot on folded leg of right man and light blue
      on stomach of right man, one blue spot on the background on the left side
    * hommes: same hotspot as jeunes but yellow and blue on right man's stomach
      and light blue on left man's stomach, blue on non-folded leg of right man
    * se: light blue on folded leg, on left man's stomach, blue on right man's
      left knee and next to left man's head, blue on left of left man on
      background
    * battant: yellow spot next to left man's head, blue on right man's
      stomach, left knee and left man's leg, blue on spot to the left on
      background



### index 252

| model | remaining sentence | hypothesis | translation |
|-------|------------|-----------------|----------------|
| 0 rem | - |  un homme et une femme sont debout dans un tunnel. |  a man and a woman are standing in a tunnel. |
| 1 rem | a | un petit garcon joue avec son instrument |   a little boy plays his instrument|
| 2 rem | a boy |  un garcon joue de la guitare dans une salle de classe . |  a boy plays guitar in a classroom. |
| 3 rem | a boy is | un garcon est debout à còte d' un feu . | a boy is standing next to a fire. |
| 4 rem | a boy is folding | un garçon est en train de faire du skateboard dans un bateau . | a boy is skateboarding in a boat. |
| 6 rem | man walking down street with reflection | un homme marchant dans la rue avec un homme . | a man walking down the street with a man.|
| 12 rem | man walking down street with reflection in glass | un homme marchant dans la rue avec du reflet en verre | a man walking down the street with glass reflection. |
| 20 rem |  man walking down street with reflection in glass |  un homme marchant dans la rue avec son reflet en verre |  man walking down the street with his glass reflection...
| complete | man walking down street with reflection in glass | un homme marchant dans une rue avec un reflet en verre | a man walking down a street with a glass reflection |


* no connection between image and sentence for 0
    * vis. att. mostly focused on boy / different parts of boy
    * tunnel is bottom left corner
* 1:
    * first three words have hotspots
    * all focus on different parts of the boy
    * petit on his neck
    * joue is focused on some part as garcon but with less intensity (bottom of
      boy)
    * intstrument focusses on hand of boy
    * textual maps an <unk> to un
* 2:
    * un is light blue on man's legs and boy's face
    * garcon has hotspot on the boy
    * joue has two light blue/yellow spots on the boy (hands and feet)
    * guitare has two light blue spots (boy's face and legs of the woman in the
      background)
    * dans has hotspot on boy's feet
    * une is light blue on the boy's face
    * salle is light blue on the woman's legs in the background
    * classe: light blue spots on the boy and the woman
* 3:
    * textual attention : a boy mappet to un and boy mapped to garcon
    * visual attention:
    * un has attention all over the image
    * garcon too, with light blue/yellow spot on the left edge of image
    * est same as garcon, but no brighter spot
    * debout (standing) has hotspot beneath the boy's legs
    * à còtè d': very similar light blue spot placing: man's shoes,boy's face
      left of the man
    * feu (fire): yellow to red hotspot to the left of the woman's feet on the
      children on the background
* 4
    * textual attention: an boy is mapped; is not; folding is mapped to est en
      and less so to faire (folding -> is in the process of doing)
    * un has blue spot on the right side of the boy (nothing there) and dark
      blue on the man
    * garçon has light blue under the boy's hands and dark blue on the man and
      the woman's legs
    * est has dark blue under the boy's bossom and blue under his hands
    * en has dark under  the boy's bossom 
    * train dark blue on the boy's chest
    * de blue right of the boy
    * du light blue on the spot between boy and man's legs
    * skateboard: dark blue on center of image
    * dans: light blue on man's feet
    * un light blue on the spot between boy and man's legs
    * bateau (boat): dark blue on the boy and red hotspot on the bottom left corner
      (nothing there)



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
   * deux shows focus on players faces -> hotspot
   * hommes is slightly attends players and area around them
   * tenues (outfits/suits) is clearly focused on the upper half of the
     players
        * blanches also, but with hotter point of focus left from them
        * same for jouent
        * football has focus on green field beneath them (point of green field)
* rem 1 textual attention all on two/deux
   * image attention up to 0.12
   * one hotspot but most of the heatmap shows some attention
   * hommes again on the people
   * debout is righ to the two people (standing)
   * terrain is on the green feald
* rem 2 textual attention most focussed on the two visible words, but some
  distributed on the unk tokens
   * image attention up to 0.06
   * again most attention on the bottom half
   * per-word attention is always hot on the bottom half
   * also attention on the top half, though only yellow, not red
   * deux has two hotspots on the left of the left player and one hotspot on
     the right of the right player
   * joueurs is light blue-to-yellow on the left of the left player
   * baseball has one hotspot: on the right edge of the picture on the edge of
     green/brown
   * battent has light blue attention on the green bottom
   -> translation of baseball player is not rooted in image
* rem 3 textual attention again most distributed on the visible words but
  fitting, few on the unk
   * image attention up to 0.06
   * heatmap very similar to rem 2 (same spots, different values)
   * deux has red hotspot on the two people
   * jouneurs has red hotspot on the left of the people
   * baseball has light blue on the green on bottom and top
   * affrontent has yellow beneath the two players and light blue to their left
     and right
   * s' has same as affrontent but no on the right
* rem 4 textual attention same pattern as before
   * image attention up to 0.06 
   * per word image attention has less hotspots overall
       * center is now only light blue/green
    * deux has light blue spot on the left edge and on the players
    * jouners has light blue on the players
    * de same
    * baseball has red hotspot on the bottom edge on the green gras (right
      side)
    * parlant has some dark blue attention on the players and yellow-to-red
      spot beneath them
    * sur same, but less value
    * un has attention light blue on the left top corner on the grass
    * terrain has two light blue spots: on on the top left side on the grass
      and one on the bottom right side on the grass
* rem 6
   * image attention up to 0.10
   * most on bottom, one spot in center and one in center right (heatmap)
   * overall distribution of attention on heatmap close to rem 4
   * deux has red hotspot on the players
   * joueurs dark blue under the players and on the green field on the top,
     light blue to the right players right
   * de dark bleu on and around the players
   * baseball: dark blue on the players and on their right
   * parlant : same as baseball but one more dark spot over the left player's
     shoulder and on the edge green/brown at the top
   * sur: almost identical to parlant, except dark spot over shoulder 
   * le: (the) almost no attention on the image, two dark spots : one in the
     middle (height) on the right side, one on the left edge on the green
   * terrain: two dark blue spots: one underneath the players, the other at the
     height of their feet to the left
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
    * un is focused on area beneath yellow tent
    * homme on left part of mountain
    * rest has very small attentions and no connection output word attention

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
    * montagne enneigèe has low attention on the montain (wide spread in
      center)
    * saut (jump) on one part of left edge of image
    * un is on the yellow tent
    * no further connection output word - to attention
    * heatmap has one hotspot on the left center, few light blue in the center
      and many slightly attented pixels in the center and the left.
rem 2
    * textual attention distributed over pink and sky for all french words,
      more evenly than for rem 1
    * max. image attention is 0.14
    * heatmap
        * one hotspot on the left hand side, one light blue
        * all others distributed over left and center and only slightly
          attended
    * debout is only hotspot (standing) on the left side, right at the edge 
    * other words have attention in the same spot, but only light blue at most
* rem 3
    * textual attention more focussed now (more word to word attentions)
    * image attention max at 0.04 -> greatly decreased
    * again most per-word image attention focused on the left side
    * des has only red hotspot on the tents
    * montagnes has light blue attention on one spot on the left edge
    * russes  has light blue attention on one spot on the top edge
    * un has has light blue attention on the tents and more beneath the yellow
      tents
    * no similarity between attention spot and output words

* rem 4
    * textual attention slightly less focussed, again only the first few
      translated  words have textual attention
    * image attention at max 0.08
    * per-word image attention again focus on the left side (lower half) for almost all words
        * attention only differs in strength
        * some other spots get some attention as well
        * again no relation to sentence
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
    * un is focused on the monster truck
    * homme is focused on two different parts of the monster truck (räder)
    * "assis" is focused on one of the banners
    * background audience is seen as background building -> attention patterns
      are on different parts of the background -> ramp, mountain and audience
      are interpreted as building
    * heatmap has hotspot in left center, most more attended pixels on the center top
      and more 0.02 pickels in center and quite a few on the right side with
      one almost hotspot
* rem 1
    * textual attention not on the one visible word but on "one" (mapped to
      one)
    * image attention up to 0.04
    * similar attentions as rem 0, but different values
    * un is less focused on the truck and light blue, but has yellow spots on
      bottom left corner and left edge
    * homme is less focused on truck and has a hotspot on the ramp's edge
    * est is focused on the truck (light blue)
    * assis is focused on truck
    * banc on audience on the right
    * devant on one part of the audience on the right (yellow)
    * batiment is focused on ground left of ramp
    * heatmap has three hotspot in center and right hand side
    * attention is more focussed on heatmap
        * more "warmer" pixels but overall fewer highlighted pixels
rem 2
    * textual attention has one-to-one mapping for "monster"
    * hotspot or at least warm area in every per word attention image
    * max. image attention is 0.08
    * overall less attention
    * un has hotspot beneath the truck
    * camion has hotspot on the truck (camion)
    * truck has attention all over the image (dark blue)
    * est same but more on truck
    * gare on truck and audience
    * le has hotspot on the right edge 
    * trottoir light blue/yellow on the same spot
    * both have dark blue over rest of image
    * heatmap
        * one hotspot on the top half (center) far fewer light blue
        * still many lighter blue colored pixel
* rem 3
    * textual attention more focussed now (monster truck to monster truck)
    * image attention max at 0.030 -> greatly decreased, less than image
      captioning
    * mostly similar to heatmap of rem 1 but far more hotspots
    * attention "cluster" in top left corner
    * un has light blue spots all over
    * monster has yellow-red hotspot on the truck
    * truck has light blue on the truck and yellow on the ramp
    * passe has yellow on the right most part of the audience
    * devant un bàtiment: all yellow on left part of top banner with batiment
      having a red hotspot on top edge on one of the trucks wheels
    * bleu has yellow hotspot on yellow banner on the right (blue)
* rem 4
    * textual attention far more  focussed, again only the first few
      translated  words have textual attention
    * image attention at max 0.07
    * un monster truck has no focus on the truck
    * vole (flies) light blue on the left of the truck and on the bottom left
      corner
    * dans light blue on the bottom left corner and dark blue on the top left
      corner
    * les (the) light blue over the audience on the right most side
    * airs (Air) ight blue on the bottom left corner deep blue on the audience
    * pour (to) red hotspot on the left most audience (image edge)
    * faire (make) light blue on the top most wheel of the truck, deep blue on
      the lowest wheel of the truck
    * une blue on two spots: one at the start of the ramp, one on the banner in
      the background on the left
    * figure: same pattern as monster truck
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
* 0:
    * des is focused on the people in the background with hotspot on the right
      half of them
    * same for gens ("people")
    * marchent on legs 
    * sur ("on") on the feet touching the ground
    * un trottoir is focused less and on more parts of the image
        * partly on the building on the background
        * mostly on the feet touching the street
* 1
    * pluesieurs is focused on the people in the background with hotspot on the left
      half of them
    * same for personnes ("people"), but with less intensity
    * marchent on legs 
    * sur ("on") on the feet touching the ground
    * un trottoir is focused less 
        * mostly on the feet touching the street
* 2
    * pluesieurs is now one hotspot on a few people in the background
    * enfants has dark blue over the people in the background
    * jouent has dark blue over the people in the background and one light blue
      spot over the legs of one person at the right edge of the image
    * football has light blue hotspot over the legs of one walking person in
      the middle of the picture
    * un has hotspot on the bottom left corner in which nothing is shown
    * terrain has two light blue dots on two peoples walking legs
    * jeu has them in the same spots as terrain but with less value
* 3
    * pluesiers has one hotspot on the right on one person's legs and light
      blue on the people on the background
    * enfants: light blue on the background
    * jouant light blue on the background but with more value on their legs
    * hockey: hotspot (jellow to red) on the girl's legs in the foreground, light blue on the
      people left from her in the background
    * terrain: red hotspot on the people left from her in the background
* 4
    * plusiers: dark blue on the people in the background on the right, light
      blue on the people in the background on the left
    * enfants: dark bleu on the girl in the front, lighter blue on the middle
      of the people on the background
    * jouant: one blue spot on the aspahlt on the left, one on the people in
      the background on the left, dark blue on the people in the background on the 
      right
    * sur: red hotspot on the same asphalt spot as jouant
    * une again asphalt spot in light blue and light blue on the bottom right
      corner
    * balançoire (swing): on the leg of the people walking past and beneath the
      girl on the front (on her right)
    * par : same light blue spot as enfants
    * une: dark blue on the girl in the front and the leftmost woman walking by
    * journèe (day): blue on the building in the back
    * ensoleilèe (sunny): blue on the building in the back and light blue on
      the most left people in the background
* 6
    * plusieurs: light blue spot on the left beneath next to the left most walking woman,
      blue spots on the right side on the right most person walking to the
      left, on the heads of the people in the background, dark blue on the
      street on the up arrow
    * enfants: light blue on the second woman walking to the right, blue from
      that spot to the people standing in the background and covering them 
    * jouant: yellow on the woman walking to the right
    * sur: yellow to red right from the girl in the front, blue on the legs of
      the right most woman walking to the right, blue on the other women
      walking to the right and on the ground left of them
    * un: red hotspot on the left bottom corner, light blue to yellow on the edge of the
      building in the back
    * terrain: edge of the building now blue, bit higher (height on image) than for previous
      word, light blue on legs of women walking to the right and on and next to
      the legs of the girl
    * de: light blue on the up arrow, yellow/blue spot of un is now blue, people in
      the background are dark blue (left side and center)
    * tennis: yellow to red on spot right to the girl's legs at the front and
      beneath the legs of the person walking to the left, light blue from top
      of that spot to the middle of image over the legs of the woman walking to
      the right (right most woman walking to the right)






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
    * later words have attention on the right
    * "une" is focused on the woman and surrounding background
    * personne gives attention to area surrounding woman and edge of parked
      cars on the right
    * "en" is hotspot in bottom right corner - where nothing is
        *  - marchant has exact same pattern
    * t-shirt focuses on edge of parked cars on the right
    * rue highlights edges of street (buildings and cars)

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
    * more focused than rem 0
    * difference from person to woman is striking and as of yet not explained
      (maybe more woman in training data k=1?)
    * image attention shoots up to max 0.2 (x4!)
    * most per-word attention is on the woman 
    * "un" is hotspot
    * femme is on woman
    * en and t-shirt as well but with higher value (yellow)
    * rouge is hotspot on woman
    * marche light blue to the left of the woman's legs
    * la rue is focused on the reifen of front right car
    * later words have attention on the right
    * heatmap
        * has hotspot in the middle of image (nearly all per-word image
          attentions color this region light blue to green, so unsurprising)
        * again a few lighter dark blue pixels (0.00 - 0.05 region, fits with
          rem 0)
        * overall structure similar to rem 0; difference in coloring stems from
          different total attention
* rem 2
    * textual attention is on "woman"-"femme" and first "<unk>"-"une"
    * "a" has no textual attention to any french word
    * image attention has a maximum of 0.04 (1/5 of rem 1)
    * une and femme is now light blue on a building on the right
    * en is now a light blue / yellow spot to top right of woman
    * veste is now on center and right cars' edge
    * noire is on woman and more (red hotspot) in bottom right corner
    * trottoir is on various parts of the street before the woman (light blue)
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
    * une has red hotspot on right edge (nothing there)
    * femme is light blue/yellow on the left of the woman
    * marchant is around the woman in dark blue
    * dans is light blue on the cars on the right front
    * une is light blue on a car on the right
    * rue (street) is light bue on the cars on the left and darker blue on the cars on
      the right
    * tres has same attention as femme
    * frequentèe (frequentation) is light blue on the left of the woman lighter
      blue on one spot on the building on the right side
    * avec same as rue
    * bàtiments: dark blue behind the woman and on foremost right car, light
      blue on the building on the right (buildings)
    * en arrière-plan: dark blue on the sky and light blue on the same building
      spot
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
    * max. image attention at 0.05
    * une has light blue on the building on the right and dark blue on the cars
      and blue in the sky
    * femme has same light blue spot as une but smaller, dark blue on the cars
    * marchant: dark blue on the edge left building/sky and the cars
    * dans dark blue on the cars, right car at the front has blue spot
    * une: red hotspot on the bottom edge next to the foremost right car
    * rue: blue on the foremost right car
    * bordèe (lined) has attention on a car on the left (2nd), right building
      has light blue spot
    * de same as bordèe (bul
    * grands : blue on center, bottom end of building, dark blue on left
      foremost car
    * bàtiments: dark blue on left side of picture, small light blue spot on
      the building on the right
    * de:  same as femme, but no attention to the left side 
    * coleur: same as marchant
    * vive same as marchant
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
    * again, good example of it not working
* 0:
    * deux is focused on womans face
    * personnes is focused on parts of the woman and on her stuff next to her
    * assis is focused on the parts of the rock under the woman
    * rocher is ironically focused on the ocean over the rock
    * "sacs de securite" is focused on the small white sandals
    * "lunettes de soleil" : lunettes over face of woman (not on!), other two
      make no sense
* 1
    * far less hotspots than 0
    * un is hotspot on woman's face
    * vieil is light blue on woman's face and spot on upper right leg
    * homme is hotspot on towel on the ground
    * t-shirt is on woman's hand
    * rouge is on towel
    * bord is light focused on water
    * eau (water) is hotspot on upper right corner
    * rocher same as rem 0
    * est assis sur barely have any attention on anything
* 2
    * two hotspots
    * un homme age  all have light blue attention on the woman's face
    * un has hotspot (red) on the woman's hand on the rock
    * chapeau (hat) is a red hotspot on the woman's face
    * de same as first 3
    * sauvetage (rescue) dark blue over the woman and bit lighter on the water
    * et yellow on the woman's face
    * chapaue same as first three
    * natation two light blue on the water, dark blue over the woman
    * sur same as f.t.
    * bateau (boat) two lighter blue spots on the water
* 3
    * une femme only dark blue attention on the entire woman
    * àgèe dark blue attention on the entire woman with light blue/yellow
      hotspot on her feet
    * en: two darkblue on the woman, one lighter blue on the towel
    * robe: two light blue: woman's face and feet
    * rose: red hotspot on the blue towel under the woman
    * assise: red hotspot on the blue towel under the woman (same as rose)
    * rocher: same as always
    * dans l' eau: on the water with eau one light blue spot in the top right
      corner
* 4
    * une femme àgrèe robe en barely any attention some small spots on/next to the
      woman
    * rose: light blue on bottom half of bikini
    * est: blue on towel woman is lying on
    * assise: blue on towel woman is lying on and under her feet
    * sur: slightest attention on sandals 
    * un: light blue on her sandals
    * rocher: red hotspot in bottom right corne
    * avec: blue under her blue towel under her arm
    * des: no attention
    * fleurs (flowers): barly attention over woman's sandals and bottom right
      corner
    * et: barest attention to the bottom left corner
    * des: barest attention to the sandals and bottom left corner
    * vètements (clothes): same as fleurs but no corner

 


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
* 0:
    * un homme is on boy's face
    * une hotspot on boys legs
    * attention very similar to 1, only slightly different values (most likely
      due to lower max)
* 1:
    * un is hotspot on boy's face
    * homme same spot light blue
    * avec is beneath scateboard and slightly on boy
    * chemise very few attention on boy
    * most of the words have attention on the boy
    * assis is on the ground  (seated)
    * banc is on the ground around the right side of the skateboard
    * park is on ground and door
* 2
    * un is hotspot on boy's face 
    * homem is lightblue spot on the left of the boy's face
    * tres agè both on the boy in light blue
    * avec light blue left of the boys face
    * un lightblue on the boy
    * t-shirt: boy's shoulder on the right in light blue
    * blanc: yellow on boy's upper half (white)
    * un lightblue on the boy
    * jean: same as t-shirt with smaller value
    * rest same as before
* 3
    * un blue attention on the boy
    * très dark blue on the boy
    * jeneu bleu over the boy's head
    * garçon: dark blue on the boy's head
    * en: red hotspot on the bottom left edge
    * costume: light blue to the boys's left, blue on the boy
    * camouflage: light blue on the bottom left edge (same spot as en), dark
      blue on the boy
    * banc dans un parc: as before
    * est: light blue on the left side of the doorstep
    * assis: left side of the ground in dark blue
    * sur: dark blue on the door edge

* 4
    * un: red hotspot on boy's chest
    * très (very): blue attention on left door side
    * jeune (young): blue attention on left door side, left door frame and
      under the boy's feet
    * garçon: dark blue attention directly over the boy's head
    * est: dark blue over the boy's head and right of the skateboard
    * assis: dark blue/blue right of the skateboard
    * sur: blue over the boy's head on the left dark blue over the boy's head on the right
    * un: blue on the skateboard
    * banc: dark blue on the left door side and on the right edge (bottom)
    * devant (in front of): top of left door side in blue
    * un: dark blue on the boy
    * mur (wall) : bottom spot on the door
    * recouvert (covered): same as devant, but spot on door is brighter
    * de: dark blue over the boy, the door and the left edge of the wall and
      left side of bottom
    * graffitis: blue on the left side of the door



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
* differences in heatmaps is once again mostly for differences in given
  attention, only a few spots of where attention is given change
* 0:
    * deux is focused on a fissure in the ground instead of the two people and
      is only red hotspot all others are at best light blue
    * chiens is focused on the two people but labels them as dogs
    * neige (Schnee) is focussed on various parts of the sand
    * hotspots change per word
    * courent is focused on one spot on the ground (plants)
* 1: 
    * deux is focused on the two people
    * chiens too
    * se battent focused first on the people than on the ground to the lower
      right
    * plage (beach) is focused directly on the gronud beneath the two
* 2:
    * deux personnes is on the two people but no longer a hotspot
    * font is light blue on one spot of the plants at the bottom
    * du has nearly no visual attention
    * ski is hotspot on second person
    * neige has light blue attention on the second person and the top half of
      the image (dark blue)
* 3:
    * deux has hotspot on left edge of image (nothing there)
    * personnes has one person in light blue/yellow, one rift in light blue 
    * marchant is light blue on persons
    * dans has several dark blue spots on the image
    * la has hotspot (red) on right side of image ; just sand there
    * neige has light blue/yellow spot on left edge and darker light blue
      beneath the two persons (neige=snow)
* 4
    * deux has hotspot on the water
    * personnes has light blue on the people, but lighter blue on the birds to
      their left
    * marchant light blue on the same birds as before and lighter blue on
      a bird to the people's right
    * sur has various lighter blue spots on the image (birds left, bird right,
      beneath people, right top on the water
    * la has two red hotspots: both edges with no adressed content
    * plage has two light blue spots: beneath the people on their right, and
      same spot as one of la hotspots and darker blue spots on the beach
* 6
    * deux has hotspot on the right edge on end water on the sand (right side
      of image), light blue spot on the people, dark blue on the rinnsal from
      water to sand, part of the sand on the right and bottom right corner
    * personnes has light blue on the people and next to the bird on the right,
      blue on the bird to the left
      dark blue on the beginning of the water (two spots)
    * marchant: red hotspot on the people, blue on the bird on the right, blue on
      the bird to the left, dark blue on the beginning of the water (two spots)
    * sur: yellow spot beneath the people to the right, light blue on the birds
      to their left, dark blue on the bird to their right
    * la: light blue on the hotspot of deux, blue between the people and the
      bird to the right, dark blue on the plants beneath the birds to the left
    * plage (beach): blue on the left edge on the sand beneath the water and
      between the people and the bird to the right, dark blue on the bird to
      the left, on the sand beneath the water right of the rinnsal, and in the
      light blue spot of la


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
* both rem 0 and rem 20 have the most hotspots (5)
* 0:
    * un is hotspot ("red") focused on girls face
    * homme is just yellow and mostly focused on girls face
    * en focuses on wall right of girl
    * veste even more so
    * rouge even more so (at least wall is red)
    * joue on bottom to the left of girl
    * guitarre is last yellow spot, same spot as jouent, but attention goes up
      to half of image and the to girl's face
* 1 
    * un focused on girl's face
    * homme is on the background to the right of the girl
    * costume is on her neck (yellow)
    * joue same spot as costume, but less intensity
    * guitarre is light blue, same spot as jouent, but attention goes up
      to half of image and the to girl's face
* 2:
    * un focuses to the right of the girl's face on the background
    * femme light blue/yellow on the girl's face
    * en blue/yellow on the girl's face and little attention left to the stick
    * robe same es en
    * de hotspot in top right corner
    * colour on the girl's clothed neck
    * vive light blue on the girl's face
    * joue de la guitare: same as 1 and 0
* 3
    * une light blue on the right of the girl's face on the background
    * jeune light blue over the girl's head
    * fille: hotspot yellow-red over the girl's head (same location as jeune)
    * en : yellow same spot as last two
    * robe: light blue on the stick and the girl's neck
    * rouge: right edge of the image (on red background)
    * tient (holds) same hotspot as en
    * une: yellow on top down to girl's head
    * balancoire (swing): light blue on the top edge of the image over the stick
* 4
    * une blue next to the head of the girl (right) and right of her right arm
    * jeune dark blue on the girl's head and neck and next to the stick on the
      left
    * fille same as jeune but without the head
    * joue light blue over the girl's head
    * sur dark blue on the girl's head, right edge and left of her stick on top
      and bottom
    * un; light blue above the hand holding the stick on the stick
    * terrain: dark blue left to the stick
    * de: red hotspot on the bottom on the left side of the girl 
    * jeux (games): light blue left of the stick on the bottom
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
        * deux is focussed on face of the woman and on her hands -> seen as
          different entities
        * hommes is less focussed on faces, more on her hands and upper arm
        * travaillant is focused on face, hand and paper on the desk
        * focus switches to picture/paper on the table -> only hotspot in all
          words and is translated as chairs
        * heatmaps reflect this
            * center spots and top right quarter are generally colored warm
            (except rem 0 - no right top quarter), though to varying
              degrees (hotspots,  slightly above 0, ...)
            * all others depend on points written above
            * up untit rem 12 the center right spots are also given similar
              amounts of attention
    * 1:
        * un homme is focused on neck of woman
        * train on background to her right
        * manger (eats) on the korb on her right
        * livre barely any attention to various parts
        * restraurant gives few attentions to background, part of table on korb
        * no connection attention to sentence for more than the first two words
    * 2: 
        * most visual att. is focused on the woman
        * un on woman's face and light blue (more att.) on the right background
        * homme is on woman and background
        -> translation more routed in linguistic information
        * age is focused on woman's face (red hotspot)
        * moyen has hotspot on part of the window
        * travaillant is light blue on the womans face
        * un is on woman's hands
        * projet is on woman's face (project), hotspot and light blue on same
          spot of window again
    * 3:
        * des hat hotspot on window
        * chefs has light blue on the woman's hands, darker blue on her face
        * chefs has light blue on the woman's face and the edge of the korb
        * preparant has dark blue on the woman's hands
        * la has hotspot next to the  woman's hands
        * nourriture has light blue on face and right of hands
        * restaurant has dark blue on the window and beneath the woman's hands
    * 4
        * image has blue spots all over the image but no translation image
          connection
        * son has hotspots on the woman's hands (his)
        * travail (work) has blue on the woman's hands but more on the window
          in the background
    * 6
        * un has red hotspot on the woman's hands
        * rest of the sentence has light blue spots on various parts of the
          woman and the window
        * again no connection image attention translation

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
