# Anti-bids

**AntiBid** `pets:AntiBid` — a cue that means **do not start contact**, **stop contact**, or the animal is **protesting**. Distinct from an affection bid (`AttentionForAffectionMethod`).

**hasAntiBid** links an animal to the anti-bids that matter for them.

**WarningSignal** — pause contact. Household-wide unless an animal page says otherwise: tail lash/thump, ears back, freeze, walk/hop away, growl/hiss/honk, bite from overstimulation.

**RecoveryMethod** (`recoversVia`) — default reset after a protest: give space, offer a treat, quiet sit with no reaching. **Alfred** uses only [MidbodyLaunchProtocol](relations.md) and [VerbalSettleProtocol](relations.md), not those three.

**pickupPermittedWhen** — exceptions to `BeingPickedUp`. Rabbits: `VetEmergency`. Jules also: `SkilledSupportedRabbitHandling`. Vader: none.

| Anti-bid | IRI | Who | Meaning | Do instead |
| --- | --- | --- | --- | --- |
| Uninvited touch | `pets:UninvitedTouch` | [Q](../animals/q.md), [Jules](../animals/jules.md) | Touch they did not invite | Wait for a bid (Q: flop or loaf + gaze + chitter) |
| Approaching during warm-up | `pets:ApproachingDuringWarmUp` | [Salem](../animals/salem.md) | Pushing contact before ~6 hours | Wait, or shake Temptations tub |
| Forced approach while shy | `pets:ForcedApproachWhileShy` | [Stevie](../animals/stevie.md) | Fast or forced contact with strangers | Quiet approach, fleece handy, let her come |
| Crowding while distant | `pets:CrowdingWhileDistant` | [Lilo](../animals/lilo.md) | Closing in while she sits apart | Stay back until head bonk |
| Affection withdrawn early | `pets:AffectionWithdrawnEarly` | [Alfred](../animals/alfred.md) | Stopping lots of pets before he is ready | Midbody launch 3–5× or verbal settle protocol |
| Food blocking of cagemate | `pets:FoodBlockingOfCagemate` | [Jules](../animals/jules.md) toward [Q](../animals/q.md) | Blocks Q’s food / steals treats | Manage feeding; Q may be upset |
| Reaching for food mid-meal | `pets:ReachingForFoodMidMeal` | [Vader](../animals/vader.md) | Hand toward his bowl while he eats | Leave the bowl alone until he is done |
| Cats near food | `pets:CatsNearFood` | [Vader](../animals/vader.md) | Cats at his food; he growls | Keep cats off his food |
| Being picked up | `pets:BeingPickedUp` | Vader; Q; Jules (narrow exceptions) | Lifting off the ground | Do not pick up; rabbits only vet emergency (Jules: also skilled full support) |
| Being scruffed | `pets:BeingScruffed` | [Q](../animals/q.md), [Jules](../animals/jules.md) | Scruff hold | Never except vet emergency |
| Ventral belly touch | `pets:VentralBellyTouch` | [Jules](../animals/jules.md) | Uninvited or full-belly handling | Invited side-belly kneading only while feet are out |
| Feet tucked means stop | `pets:FeetTuckedMeansStop` | [Jules](../animals/jules.md) | Tucking feet in during pets | Stop; feet sticking out means continue |

Stevie and Lilo: **no-go body regions unknown** — do not invent them.

Alfred’s **escalation behaviors** (claw, bite, heavy body, desperate clawing) are how the anti-bid shows up, not invitations to continue. Protocols: [relations](relations.md).
