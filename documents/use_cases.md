
# Sense Disambiguator Use Cases [Updated Aug 14]


1. Use Case 1: A context sensitive word sense parser. 
 
* Input: A lexical word: e.g. ‘head’ + a particular context. 
* Output: surface: head, sense: 1, vectors: {leader:1, ear:1}, examples: "this is an example sentence using head."

## PLEASE NOTE! This is my primary use case. The use cases below are not currently implemented. They are goals for a future point. I will leave them in the documentation for such a time.


2. Use Case 2: Reverse indexed word sense search within a particular context.

* Input: A particular word sense: heada 
* Output: A list of sentences that use that word in that particular sense. E.g. [“He banged his head on the ceiling.”, “Her head circumference measured fifty centimeters.” ]


3. Use Case 3: A context sensitive word sense thesaurus. 
  
* Input: A particular word sense: heada
* Output: The most similar words that have a different lemma, given a particular context.


4. Use Case 4: A semantic valence scorer. [stretch goal/brainstorming] 

* Input: A particular lexical word that is present in the text, e.g. ‘head’ 
* Output: A score indicating the semantic impact the word has in the text. (how do I do this?)


Narrative Discussion: I want to do a project that is syntactic in nature. To me, this is an area that is quite rich for the exploring, and coming right off the heels of 503, I would love to apply some of that knowledge in a computational context. I think that an interesting project would center around the identification and classification of diverse meanings that are hidden within a single token. An example of this would be head, which could be categorized on several different levels. For example head1 would be a noun which means the part of the body above the neck, whereas head2 would be a verb which means ‘go in a particular direction’. However, it is certainly more complicated than that, for we also have cases like head1a which might be seen in the case of ‘head of the village’, while this meaning is presumably a derivative of head1 it is at the very least expressed in figurative terms. This I think is a question that requires syntactic usage because a word is generally known by its context–which is to say how do n+-x influence our interpretation of n. 


This investigation was inspired in part by my internship work relating to Indonesian. Recently I created vectors for every type based on every other word that coincided with that word as defined by sentence boundaries (the entire corpus is generated from single sentence length documents). An example of this is the word ‘kepala’ which translates via Google Translate as ‘head’. Below is an abstract of all the words that coincide 25 times or greater. Translations provided beneath. 


kepala
Counter({'daerah': 164, 'desa': 152, 'dinas': 141, 'negara': 113, 'korban': 79, 'sekolah': 78, 'sakit': 74, 'kota': 71, 'luka': 67, 'mengalami': 64, 'orang': 62, 'memiliki': 60, 'masyarakat': 55, 'kantor': 54, 'kabupaten': 51, 'rumah': 51, 'langsung': 46, 'wakil': 45, 'badan': 44, 'anak': 42, 'tangan': 41, 'wilayah': 41, 'presiden': 40, 'calon': 38, 'indonesia': 36, 'salah': 35, 'warga': 35, 'keluarga': 35, 'keras': 35, 'posisi': 34, 'bidang': 33, 'suku': 33, 'tubuh': 32, 'humas': 30, 'staf': 30, 'pemerintahan': 29, 'biro': 29, 'menjabat': 29, 'pemerintah': 28, 'tim': 27, 'mantan': 27, 'gubernur': 27, 'pelaku': 26, 'guru': 26, 'tugas': 26, 'provinsi': 26, 'kaki': 25, 'kondisi': 25, 'hukum': 25,


head
Counter({'area': 164, 'village': 152, 'service': 141, 'country': 113, 'victim': 79, 'school': 78, 'sick': 74, 'city': 71 , 'injury': 67, 'experienced': 64, 'person': 62, 'own': 60, 'community': 55, 'office': 54, 'district': 51, 'home': 51, ' direct': 46, 'deputy': 45, 'body': 44, 'child': 42, 'hand': 41, 'region': 41, 'president': 40, 'candidate': 38, 'Indonesia' :36, 'wrong': 35, 'citizen': 35, 'family': 35, 'hard': 35, 'position': 34, 'field': 33, 'tribe': 33, 'body': 32 , 'public relations': 30, 'staff': 30, 'government': 29, 'bureau': 29, 'in office': 29, 'government': 28, 'team': 27, 'former': 27, ' governor': 27, 'perpetrator': 26, 'teacher': 26, 'duty': 26, 'province': 26, 'leg': 25, 'condition': 25, 'law': 25,


Now the words of coincidence are clearly informing the meaning of the target word, one of the problems with the data is that multiple meanings are hidden beneath the same expression ‘kepala’. As an example, I would like a system that is able to differentiate between ‘kepala1’ and ‘kepala2’--or identify that a word such as ‘jam’, which translates to time, which may (I don’t know enough about Indonesian) not merit a subscriptable differentiation. 


Unless guided otherwise, I plan on building this in English, and then after the fact I might see if I can apply similar methods in a different language. I think the reason is obvious. While testing the model, I need a native speaker to verify whether or not the model is accurately identifying subscriptable differences. For the purposes of the project, I think it is best if that native speaker is me.
