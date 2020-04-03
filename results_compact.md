# complete model: maximum image attention (top 15)

* generally one hotspot per image (one hotspot on the heatmap, can be several
  in the per-word images)
* generally not related to the translated word
* first research question: how do translations change in case of word ablations
  and foil words

## impressions for k ablations

* overall: image captioning works reasonably well - content of image is
  represented, but it is generally not a translation of the english caption
* maximum image attention rises with the number of remaining words
* attention patterns may remain the same (heatmaps) while the assigned
  attention rises
* per-word image attentions are different for each model
    * hardly any two models assign visual attention to the same image area for
      the same word
    * instead, they assign attention to the same area for different words
    * no clear relation between translated word and visual attention
    * especially the models utilizing many words assign visual attention to
      unimportant parts of the image in combination to the massive extent of
      assigned attention
* image captioning generally assigns very little attention to specific areas of
  the image, instead many pixels receive little attentions
    * many more parts "matter" to the image captioning models
    * models with more words tend to pick a "hotspot" and assign most of their
      attention there
    * or (mostly for the complete models) many different areas are given
      a great amount of attention - due to the coloring of the heatmap and the
      immense differences in value I cannot tell if these models assign no
      attention to the other areas or if the assigned amount of attention is
      very little
    * models generally pick the same spots to assign attention to *if* they
      manage to translate the source sentence with the same context
    * the closer the translations are the closer are the image attention
      patterns (e. g. index 252 or index 138 (grows higher in visual attention
      with slightly changing hot areas), index 245 is almost a perfect example
      of this behaviour, index 30 shows this too, but with rem3 and rem4 out of
      order)
    * *but* this is not exclusive: index 140 shows that the image attention can
      follow this pattern _without_ similar translations: the first half of the
      sentence is the same, the image attention patterns are similar, *but* the
      second half is quite different for each model
        * index 706 has quite the similar translations between models, but very
          different per-word image attentions for each model
        * index 869 has different translations (though the last 3-4 are quite
          similar), but a similar image attention to index 245
        * index 546 also has similar attention per-word but not quite similar
          transaltions (share subject but not much else)
    * if the translation changes drastically the similarity between the
      heatmaps of image attention and the per-word attention greatly decreases
      (e.g. index 655 to a lesser extent, index 678 shows these changes
      drastically, index 829 too, also index 946 and index 996, index 39 is
      textbook example of this, index 948 to a degree)
* more words do not necessarily result in a translation and can even be harmful
* textual attention is generally word-to-word if the translation is correct
    * if there is only one word the attention of the first <unk> token is
      generally on the first translated french word
    * if there are no words <eos> is generally attended to for all translated
      words
    * if the translation is utter non-sense there is no pattern to the textual
      attention either
* if the translation is incorrect there are words with little to no attentions
  to any french words
* some models have obviously learned to ignore the information given to them by
  the words, at least in critical circumstances - I have not looked at the
  entire dataset
* noteable influence on those images with the highest image attention of the
  complete model
* while it is not clear _why_ the complete model chooses to apply so much
  attention to the image, it *is* clear that removing words from the source
  sentence drastically hurts model performance
* also proves that the model is not capable of utilizing the image to overcome
  the missing information in the source sentence
* yet overall model performance does *not* drastically decrease -> *edge*
  cases!
* introducing foil words does not always "throw the model off"
* there are cases in which the respective model can successfully extract the
  missing information from the image and discard the wrong source sentence
  information
* _but_ there are also cases in which the foil word results in utterly absurd
  translations
* mostly these are cases, in which the complete model struggles to translate
  the source sentence into French successfully
    * it is unclear, if the models fail to utilize the image attention or if
      the image attention is the reason the models fail _in the first place_
      - we are looking at the maximum image attentions!
* working indices:
    * 252
    * 138 (except for image captioning)
    * 245
    * 706
* somewhat working indices (need about k=6 to get translation close to source)
    * 655 (k < 6 is nonsense)
    * 678 (k < 6 is nonsense)
    * 140 (k < 6 is not close to image)
    * 829 (k < 6 is not close to image; k < 3 is nonsense)
    * 869 (k < 12 does not get content right)
    * 30 (k < 4 is wrong)
    * 546 (k < 12 is utterly wrong, k < 3 does not even get "girl" right)
    * 946 (k < 3 has nothing to do with image, entire sentence (k=20) is needed to get
      translation right)
    * 996 (k < 6 no overlap with image)
* not working at all: index 39 and index 948
    * all ablations and complete model seem to compete who can produce the most
      unrelated translation
* conclusion:
    * ablations hurt performance greatly for *high image attentions*
    * the model is not capable of extracting the missing information from the
      image
    * some indices show that textual is discarded (no overlap between remaining
      words and translation)
    * only 1/3 of the sentences are somewhat correctly translated by the
      ablated models - most of the time that is at least 2/3 of the complete sentence
      and only once it is 50%
    * 14/15 models are somewhat correct translated by the models utilizing the
      first 6 words - most of the time the most relevant information is given
      in these 6 words, e. g.
        * index 996 and 946, 869, 829
        * who or what (+description (e.g. "bikini")) + verb
    * only exception is index 39: sentence only has 5 words, but all models
      fail

## impressions for foil words - TODO

* maximum image attention can be the same as for complete, but in most cases it
  is a bit smaller (0.12 to 0.20 or even 0.12 - 0.40 (foil word spoils
  translation)
* generally the most damaging replacement are NNs while all others hurt overall
  performance less
    * careful: NNs are also the biggest pos-tag group (e.g. PRP is *much*
      smaller - less impact by default)
* again looking at the images with the highest image attention
* opposite to above results: the more fragile indices are the most robust now
    * fits though: the high percentage of textual information is needed to
      translate correctly
    * question is though: does this mean the models extract knowledge from
      "unfoiled" rest of sentence or does this mean models extract foiled
      information from image?
* foil words with next to no effect:
    * index 138
    * index 655
    * index 678
    * 245
* interestingly, textual attention takes a dive for index 678 while image
  attention rises (replacement of nn), *but* this does not apply for all nn
  replacement (correlation more likely than causality)
* index 245 and 138 are thus resistent to both foil words and word ablations ->
  very easy?
* foil words instances with effect
    * index 140
    * index 706
    * index 829
* no effect: index 252
* index 30 and index 546 deal with foil words well except for NN replacement
* foil words turn translation into nonsense for index 948, yet grammatically
  better than complete model
    * but image attention is entirely contrary to other indices: many random
      replacement assign a higher max. im. attention than the complete model
* index 996 fails only if PRP is replaced - prp models worse than the others?
* index 39 is just as bad for foil words
* index 706 is especially weak to vp, but it only matters for the image attention,
  translation is correct or wrong (cars replaced with cartoon results in
  translation "garbage")
* index 254 suffers from replacing of all kind
* index 948 achieves *better* results with foil words - considering the textual
  attention I am tempted to view this as a mere coincidence
* jj replacement results in wrong translations due to model training: original
  sentences are translated to nonsense by the jj replaced model
* if the complete model fails to translate the sentence, the replaced data
  models fail
    * index 948 is utter nonsense and index 39 too
    * index 39 shows very high max. image attentions (only nn is smaller than
      complete), yet translations are nonsense
    * index 17 is also utter nonsense, but has lower max image attention than
      complete model 
        * no causality between these two behaviours visible

* as of right now, it does not appear that the models learn to extract the
  missing attention from the image, but draw it from the source sentence and
  word probabilities
