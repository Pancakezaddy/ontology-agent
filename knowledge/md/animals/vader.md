# Vader

- **IRI:** `https://example.org/ontology/pets#Vader`
- **Types:** [Dog](../vocab/species-and-breeds.md#dog), [Flat-Coated Retriever](../vocab/species-and-breeds.md#flat-coated-retriever)

Five-year-old Flat-Coated Retriever. Fun, loving, and energetic. Loves people immediately. Sketched out by large vehicles. Nervous around other dogs: unsure how to act or how they will react; cautious until comfortable, still observantly anxious. Loves walks and running around the backyard. Loves being called a handsome boy. Loves lying in the backyard getting belly rubs. Lives for treats and wet food. Prefers to be fed around 6pm and will bark endlessly if food is not getting ready then. Not aggressive. Unaware of how large he is. Brings toys (favorite: short round Halloween cat) when he wants to go outside.

## Facts

| Property | Value |
| --- | --- |
| `hasAgeInYears` | 5 |
| `hasTemperament` | Fun, Loving, Energetic, LovesPeopleImmediately, NotAggressive, UnawareOfOwnSize, NervousAroundOtherDogs, SketchedOutByLargeVehicles |
| `isNervousAround` | LargeVehicles, OtherDogs |
| `hasMaximumWarmUpHours` | 0 (loves people immediately) |
| `hasPreferredFeedingHour` | 18 (6pm) |
| `hasFavoredTreat` | HouseholdTreats |
| `hasFavoredFood` | HouseholdWetFood |
| `hasPrimaryMotivation` | HouseholdTreats, HouseholdWetFood |
| `requestsMealUsing` | Vocalizing |
| `requestsGoingOutsideUsing` | BringingToyToGoOutside |
| `hasFavoriteToy` | HalloweenCatToy (short, round Halloween cat) |
| `enjoysPlayActivity` | Walking, BackyardRunning, BackyardBellyRubs |
| `solicitsAffectionUsing` | Vocalizing, Nudging, Pawing, Following, OccupyingLap, PresentingBelly, SittingClose |
| `prefersAffectionVia` | GettingOnTheirLevel, PreferredSpotScratch, OfferingTreat, OccupyingLap, Leaning, CalledHandsomeBoy, VigorousBellyRub |
| `hasAntiBid` | ReachingForFoodMidMeal, CatsNearFood, BeingPickedUp |
| `showsWarning` | GrowlHiss (cats near food); also household warnings |
| `recoversVia` | GivingSpace, OfferingTreatAfterProtest, QuietSitNoReach |
| no-go body regions | none asserted |

See [play](../vocab/play.md), [affection](../vocab/affection.md), [food](../vocab/food.md), [antibids](../vocab/antibids.md).

## Anti-bids / aversions

Not affection invitations: he is sketched out by **large vehicles** and **nervous around other dogs** (caution until comfortable). Do not treat dinner barking at 6pm as a petting bid — it is a **meal request**.

**Reaching for food mid-meal** (`pets:ReachingForFoodMidMeal`). Do not put a hand toward his food or treats while he is eating.

**Cats near food** (`pets:CatsNearFood`). He **growls** if cats go near his food.

**Being picked up** (`pets:BeingPickedUp`). Do not pick him up. No exceptions asserted.

After a protest: give space, offer a treat, or sit quietly without reaching.
