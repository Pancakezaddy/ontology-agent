# Markdown ontology

IRI base: `https://example.org/ontology/pets#`  
Prefix: `pets`

This tree is the **canonical readable** form of the household ontology. Turtle remains at [`../ontologies/household-pets.ttl`](../ontologies/household-pets.ttl) for OWL tooling.

Housing footnote: everyone shares the household except Q and Jules, who have their own room. Ages and sex are recorded only when asserted.

## Layout

| Path | Contents |
| --- | --- |
| [INDEX.md](INDEX.md) | Term map and links |
| [animals/](animals/) | One page per named pet |
| [vocab/](vocab/) | Classes, properties, bids, anti-bids, food, play, places |

When facts change, edit the relevant markdown page, then the matching axioms in the Turtle file, then `knowledge/terms.jsonl`.
