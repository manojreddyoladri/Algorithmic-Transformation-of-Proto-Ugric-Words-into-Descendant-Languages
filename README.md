# Algorithmic-Transformation-of-Proto-Ugric-Words-into-Descendant-Languages

Implemented a regular sound change algorithm for Sumerian-Ugric protowords based on the set of sixteen rules given in Table 3 of the Appendix of
the Etymological Dictionary of the Sumerian Language. The algorithm takes input a Proto-Ugric word and apply the rules to generate Hungarian, Khanty, Mansi, and Sumerian words. Generates all possible words in case of an ambiguity.

Table 3 only describes regular sound changes for consonants. Regular sound changes for vowels are considered secondary. For simplicity of
implementation, we assumed that a vowel does not change to another vowel, but second vowel may be omitted in a CVCV type protoword. We also assumed that all protowords have the form CVCV or CVC.
 
We tested our algorithm on the following hypothetical protowords: ket, kin, kota, l’uk, mene, muna, pede, pele, puw, śije, śoli, wul

You can find the structured output of our algorithm at Output.png. It shows the descendant languages equivalent of the above words.

