# inizializzazione della collezione di documenti

documents = {
    1: "Brutus killed Caesar",
    2: "Caesar was killed by Brutus",
    3: "Rome was a powerful republic",
    4: "Brutus and Cassius planned against Caesar",
    5: "Cleopatra met Caesar in Egypt"
}

print("Collection of documents:\n")

for doc_id, text in documents.items():
    print(f"Doc {doc_id}: {text}")

# Tokenizzazione semplice : lower + split su spazio

tokenized_doc = {}

for doc_id, text in documents.items():
    tokens = text.lower().split()
    tokenized_doc[doc_id] = tokens

print("Tokenized documents:\n")

for doc_id, tokens in tokenized_doc.items():
    print(f"Doc {doc_id}: {tokens}")

# costruzione del vocabolario

vocabulary = sorted(set(
    token
    for tokens in tokenized_doc.values()
    for token in tokens
))

print("Vocabulary:\n")
print(vocabulary)
print(f"\nNumber of distinct terms: {len(vocabulary)}")

# Index

print("Vocabulary with index:\n")

for i,term in enumerate(vocabulary):
    print(f"{i:2d} -> {term}")

# Costruzione della term-doc incidence matrix

incidence_matrix = {}

for term in vocabulary:
    row=[]
    for doc_id in documents:
        row.append(1 if term in tokenized_doc[doc_id] else 0)
    incidence_matrix[term] = row

print("Term-doc incidence matrix:\n")

header = "term".ljust(15)+"".join([f"D{doc_id}".rjust(5) for doc_id in documents])
print(header)
print("-"*len(header))

for term,row in incidence_matrix.items():
    row_str = "".join([str(value).rjust(5) for value in row])
    print(term.ljust(15)+row_str)

# Esempio di query booleana: brutus AND caesar

brutus_vector = incidence_matrix["brutus"]
caesar_vector = incidence_matrix["caesar"]

and_result = [b & c for b,c in zip(brutus_vector,caesar_vector)]

print("brutus   ->",brutus_vector)
print("caesar   ->",caesar_vector)
print("AND      ->",and_result)

matching_docs = [doc_id for doc_id,value in zip(documents.keys(),and_result) if value == 1]

print("Documents matching 'brutus AND caesar':", matching_docs,"\n")

# Piccolo esempio con AND, OR e NOT

brutus_vector = incidence_matrix["brutus"]
caesar_vector = incidence_matrix["caesar"]
cleopatra_vector = incidence_matrix["cleopatra"]

not_cleopatra_vector = [1 - x for x in cleopatra_vector]

query_result = [b & c & nc for b, c, nc in zip(brutus_vector, caesar_vector, not_cleopatra_vector)]
print("esempio con AND e NOT\n")
print("brutus          ->", brutus_vector)
print("caesar          ->", caesar_vector)
print("NOT cleopatra   ->", not_cleopatra_vector)
print("final result    ->", query_result)

matching_docs = [doc_id for doc_id, value in zip(documents.keys(), query_result) if value == 1]

print("\nDocuments matching 'brutus AND caesar AND NOT cleopatra':", matching_docs)

## Prova con caesar OR brutus

or_query_result = [a or b for a,b in zip(brutus_vector,caesar_vector)]
print("esempio con OR\n")
print("brutus          ->", brutus_vector)
print("caesar          ->", caesar_vector)
print("final result     ->", or_query_result)

matching_docs_or = [doc_id for doc_id,value in zip(documents.keys(), or_query_result) if value == 1]

print("\nDocuments matching 'caesar OR brutus':", matching_docs_or)

# Inverted Index

## Costruzione della coppia (term,docID)

terms_doc_pair = []

for doc_id, tokens in tokenized_doc.items():
    for token in tokens:
        terms_doc_pair.append((token,doc_id))

print("Term-doc pair:\n")
print(terms_doc_pair)

## Ordiniamo prima per token poi per doc_id

# Ordiniamo prima per termine, poi per docID

terms_doc_pairs = sorted(set(terms_doc_pair))

print("Sorted unique term-doc pairs:\n")
print(terms_doc_pairs)
print("\n")

## Raggruppiamo le coppie per costruire l'inverted index

inverted_index = {}

for term, doc_id in terms_doc_pairs:
    if term not in inverted_index:
        inverted_index[term] = []
    inverted_index[term].append(doc_id)

print("Inverted index:\n")

for term, postings in inverted_index.items():
    print(f"{term:15s} -> {postings}")

## Aggiungiamo anche la document frequency (df): il numero di documenti in cui compare un termine

document_frequency = {}

for term, postings in inverted_index.items():
    document_frequency[term] = len(postings)

print("Document frequency:\n")

for term, df in document_frequency.items():
    print(f"{term:15s} -> df = {df}")
print("\n")
## Visualizziamo alcune postings lists di interesse

terms_to_inspect = ["brutus", "caesar", "cleopatra", "republic"]

for term in terms_to_inspect:
    print(f"{term:15s} -> postings = {inverted_index[term]}, df = {document_frequency[term]}")

def intersect(postings1, postings2):
    """
    Restituisce l'intersezione tra due postings lists ordinate.
    """
    answer = []
    i = 0
    j = 0

    while i < len(postings1) and j < len(postings2):
        if postings1[i] == postings2[j]:
            answer.append(postings1[i])
            i += 1
            j += 1
        elif postings1[i] < postings2[j]:
            i += 1
        else:
            j += 1

    return answer

## Riproviamo la wuery brutus AND caesar

postings_brutus = inverted_index["brutus"]
postings_caesar = inverted_index["caesar"]

result = intersect(postings_brutus, postings_caesar)

print("brutus ->", postings_brutus)
print("caesar ->", postings_caesar)
print("\nResult of 'brutus AND caesar' ->", result)

matching_docs = intersect(inverted_index["brutus"], inverted_index["caesar"])

print("Documents matching 'brutus AND caesar':\n")

for doc_id in matching_docs:
    print(f"Doc {doc_id}: {documents[doc_id]}")

## Esempio di AND tra più termini

query_terms = ["brutus", "caesar", "cassius"]

current_result = inverted_index[query_terms[0]]

for term in query_terms[1:]:
    current_result = intersect(current_result, inverted_index[term])

print(f"\nResult of {' AND '.join(query_terms)} -> {current_result}")

for doc_id in current_result:
    print(f"Doc {doc_id}: {documents[doc_id]}")

## Mostriamo chiaramente df e ordine di esecuzione

query_terms = ["caesar", "brutus", "cassius"]

print("Document frequencies:")
for term in query_terms:
    print(f"{term:10s} -> {document_frequency[term]}")

ordered_terms = sorted(query_terms, key=lambda term: document_frequency[term])

print("\nRecommended processing order:")
print(ordered_terms)

### Costruzione del positional index. Per ogni termine salviamo, per ogni documento, tutte le posizioni in cui compare

positional_index = {}

for doc_id, tokens in tokenized_doc.items():
    for position, token in enumerate(tokens):
        if token not in positional_index:
            positional_index[token] = {}
        if doc_id not in positional_index[token]:
            positional_index[token][doc_id] = []
        positional_index[token][doc_id].append(position)

print("Example positional postings:\n")

for term in ["brutus", "killed", "caesar", "cleopatra"]:
    if term in positional_index:
        print(f"{term:12s} -> {positional_index[term]}")

### Ispezioniamo i token con posizione per ogni documento

for doc_id, tokens in tokenized_doc.items():
    indexed_tokens = list(enumerate(tokens))
    print(f"Doc {doc_id}: {indexed_tokens}")

def phrase_query_two_terms(term1, term2, positional_index):
    """
    Restituisce i docID che contengono la frase esatta 'term1 term2'.
    """
    result = []

    postings1 = positional_index.get(term1, {})
    postings2 = positional_index.get(term2, {})

    common_docs = sorted(set(postings1.keys()) & set(postings2.keys()))
    if not common_docs:
            result.append("No document for this phrase query")
    for doc_id in common_docs:
        positions1 = postings1[doc_id]
        positions2 = postings2[doc_id]

        positions2_set = set(positions2)

        for pos in positions1:
            if pos + 1 in positions2_set:
                result.append(doc_id)
                break
        

    return result

### Proviamo alcune phrase query

test_phrases = [
    ("brutus", "spolied"),
    ("killed", "caesar"),
    ("caesar", "was"),
    ("in", "egypt")
]

for term1, term2 in test_phrases:
    result = phrase_query_two_terms(term1, term2, positional_index)
    print(f'"{term1} {term2}" -> {result}')

def proximity_query_two_terms(term1, term2, k, positional_index):
    """
    Restituisce i docID in cui term1 e term2 compaiono entro distanza k.
    Implementazione semplice e leggibile, non ancora ottimizzata.
    """
    result = []

    postings1 = positional_index.get(term1, {})
    postings2 = positional_index.get(term2, {})

    common_docs = sorted(set(postings1.keys()) & set(postings2.keys()))

    for doc_id in common_docs:
        positions1 = postings1[doc_id]
        positions2 = postings2[doc_id]

        found = False
        for p1 in positions1:
            for p2 in positions2:
                if abs(p1 - p2) <= k:
                    found = True
                    break
            if found:
                result.append(doc_id)
                break

    return result

print("Proximity query examples:\n")

examples = [
    ("brutus", "caesar", 1),
    ("brutus", "caesar", 2),
    ("caesar", "egypt", 2)
]

for term1, term2, k in examples:
    result = proximity_query_two_terms(term1, term2, k, positional_index)
    print(f'{term1} within {k} words of {term2} -> {result}')