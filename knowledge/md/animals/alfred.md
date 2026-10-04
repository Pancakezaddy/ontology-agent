# Alfred

- **IRI:** `https://example.org/ontology/pets#Alfred`
- **Types:** [Cat](../vocab/species-and-breeds.md#cat)

Ten-year-old male orange cat. Overtly affectionate to the point that a person needs a protocol to stop demanded pets. If given a lot of affection and stopped before he is ready, he claws and bites, heavies his body, resists moving, and desperately claws at the person. Proper protocol: gently unhook claws from fabrics and launch via midbody firmly; he enjoys being launched and the hunt of despair, so this typically takes 3–5 times. Alternative: firmly but lightly push him off, settle his body, and say dude stay enough of this.

## Facts

| Property | Value |
| --- | --- |
| `hasCoatColor` | Orange |
| `hasSex` | Male |
| `hasAgeInYears` | 10 |
| `hasTemperament` | OvertlyAffectionate, DemandingOfPets |
| `solicitsAffectionUsing` | Vocalizing, Nudging, Pawing, GentleBiting, SittingClose, Clawing, Circling, OccupyingLap, Following, DirectGaze, SlowBlink, Leaning, HeavyingBody, ResistingDisplacement, DesperateClawing |
| `prefersAffectionVia` | GettingOnTheirLevel, OccupyingLap, PreferredSpotScratch |
| `escalatesWhenAffectionWithdrawnEarly` | Clawing, GentleBiting, HeavyingBody, ResistingDisplacement, DesperateClawing |
| `stopsDemandingAttentionVia` | MidbodyLaunchProtocol, VerbalSettleProtocol |
| `hasCessationRepetitionsMin` / `Max` | 3 / 5 |
| `enjoysPlayActivity` | BeingLaunched, HuntOfDespair |

Protocols are defined in [relations](../vocab/relations.md).

## Anti-bids

**Affection withdrawn early** (`pets:AffectionWithdrawnEarly`). If you gave a lot of pets and stop before he is ready, he claws, bites, heavies his body, resists moving, and desperately claws. That is protest, not a request to continue the same way.

**Do:** [MidbodyLaunchProtocol](../vocab/relations.md) 3–5 times, or [VerbalSettleProtocol](../vocab/relations.md) (“dude stay enough of this”). Those are his only asserted recovery paths — not generic space/treat/quiet-sit.

**Overstimulation bite** (`pets:OverstimulationBite`) is a warning that means stop. Household warnings (tail, ears, freeze, walk away, growl/hiss) also apply.
