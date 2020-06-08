## General Topics

### Map Update

* PT#24 - Paris
	* Need to place the dept store icon outside the circle on the map because it is covered up by a store during gameplay.
* PT#28 Katsushika and Sumida.
	* Colors too close. Hard to tell difference (across the water) in low light.
	* Perhaps use a different pattern.
* PT#30-32 - station kanji too big
* PT#42 - Need to fix map to clarify adjacent wards. Example, Ota and Koto.
* PT#43 - Sangenjaya
	* Perhaps use Kichijoji (note: it's off the map in Mushashino)
	* Futakotamagawa instead of Todoroki
* PT#48 added station and connection in Setagaya
* PT#48 Using icons to mark dept store locations
	* they get covered when store is placed on
	* needed to make bigger
	* also added small icon outside that wouldn't be covered
* PT#45 contrast between Sumida and Katsushika could be improved.
	* Changing Katsushika to Green would fix this problem.

### Using Github to manage the project

* issue tracking

### Writing the rules

* Terminology
	* PT#30-32 - Lure -> Move (Advertise)
* phrasing
	* track: (#54) I: for the double track description: "2 connect segments of track as long as least one touches the card played"  "city of origin"
	* Move: (#54) I: Move action says "Move ... from their ward", but a single customer can be picked up and dropped off at a store in the same ward. Clarify rule description

### Strategy Guide

* cf Chess openings
	* Adachi Gambit
* General heuristics:
	* don't commit to a part of the map too early.
	* Consider mentioning to new players not to overcommit to a single area (especially early in the game).
	* Noted that first move is commonly Build + Expand

### What is Fun?

* What is fun?
	* GOOD: Game has multiple viable strategies that work
	* GOOD: Decision when to transition to gaining VPs from building economy
	* Big moves across board
	* move customers along a long track
	* Fun to build dept stores and connections
	* getting multiple customers
	* having to give customers to other players - not being able to avoid
	* PT#22 Station names & story; Fun luring lots of customers!
* what is the least fun?
	* What is slowing the game down?
	* PT#25 Not knowing where to build track at start of game
		* How could this be marked on the map?
	* PT#18 running out of track (spent earlier)
	* what is the worst set of cards to draw?
		* what can the player do? can it be improved?

### Usability improvements

* PT#22 - Easter egg colors, not good for colorblind?
* Adding customer counts
	* PT#24 - How many of each customer type are in the bag?
	* Info added to player screen for PT#52
* Adding card counts on cards and map
* Moving stations slightly on map to make it easier to determine which ward they belong to
* PT#27 - The stores could have stickers on both sides so that it is easier to sort them at the beginning of the game.
* Dept store symbol - conversion from old symbol
* Need to ensure that dept store upgrade symbol is visible when covered with a store
* Reduce contrast of ward boundaries to make the rail connections easier to see.
* todo: adding index in corner so cards can be splayed
	* initially wanted to have Japanese vertially and Romanized horiz, but that looks heavy and runs into issues with the "safe area" of the card
	* but just english vertically works well

## Playtesting

### Playtests

Development playtests

2 kinds:

* stable ruleset tests with new players
* testing rule changes
	* often with existing players, but can use new players for this as well

### Playtest notes

* write summary of rules being tested
* two good, two bad. free form
* ask each player

### Playtest Group

Looking at the timeline graph, you can see the importance of having a good (perhaps “tolerant“ is a better word) playtest group available to run your designs through. It’s also incredibly beneficial if they understand game design principles, because the feedback they give can be much more focused and actionable.

TODO: "tolerant" Adam : "Playtesting is a marathon. Also, too easy to get stuck on an old version, good to be able to see things with fresh eyes."

In my case, I was fortunate to have some amazing game designers/playtesters willing to suffer through the initial prototypes during the initial design phase. So before getting too deep into this, I need to thank Adam (blinks), Jeff (americanjeff), Sverre (SRabbelier), Adrian and Joshua (eflat) for the time they invested in this design. Adam in particular provides consistently useful feedback and produces wonderful games that I hope will one day be more broadly available.

## Unsorted

### The first complete version

* PT#7
	* need to take Income as a separate action -  no automatic card draw
* game has settled to the 5 core actions: Build, Upgrade, Expand, Move, Income
* pay matching card for build, upgrade and move.
* pay any card for expand track
* pay any 3 cards for double-expand track


### Actions

* PT#7
	* Experimented with allowing the same action twice.
	* It allowed Adrian to take 2 customer actions to get multiple customers (which felt like a big move), but otherwise it probably isn't worthwhile.
* PT#50: Why not allow the same action twice?
	* 2 scoring actions at end of game.
	* can be big, and emphasizes the random customer placement

### Scoring

* handling ties: removing type you have the most of
* set collection

### Store upgrades

* reduce to 2
* limit region on map (partially covered in 1st week)

### Income action

* PT#7
	* Having to take an action for income didn't feel bad. And it made income from track more exciting.
* how bad do Income actions feel during the beginning of the game?
* is that a problem? (can't just give players everything or else there is no game)

### Move notes

* PT#13 - tested Bypass during Lure
	* rarely applies; hard to remember to do it
* PT#42 - Would like to be able to pick up customers along the way

### The game timer

* number of customers
* 1 minute per turn = 60 customers for an hour
* range from 40-80. Settled on 60. Reduced to 52
* 60 customers is divisible by 2,3,4,5
* sometimes players forget to place a customer. if the game is expected to give everyone the same number of turns, then players feel bad when this mistake is revealed at the end of the game (and some players get extra turns).



### Track

* PT#28 - Patchwork track, because it's easy to place.

## Alternate Maps: Paris, Hong Kong, London

### Paris

* PT#24
	* Need to place the dept store icon outside the circle on the map because it is covered up by a store during gameplay.

* PT#26

### London

* created London map, but didn't test until later
* PT#47 testing London
	* Map too connected with too many close dept stores.
	* Too many customers arriving in Westminster.
		* Yet too easy to avoid other player's dept stores.
	* Having Westminster be too large upsets the balance of the game.
	* Some of the stations on the map are too close together.
* Rework the London map to use the pre-1965 metropolitan boroughs.
	* They were much smaller and covered just the central core of London (which is all we care about.
	* The board could them zoom in on the core of London and still have about 20 regions. This would allow more interesting stations to be included and they wouldn't be too close together.

## Expansions

* focus on the core game - move other interesting ideas into expansions

### Hachiko

* PT#16
	* Shibuya + 4 neutral track
	* HAchiko placed in random location
	* Reunite Action: Move Hachiko to Shibuya, taking customers (as with Lure) and give income to anyone who owns track Hachiko uses (incl player who took action).
	* Hachiko. Not a negative, but not a core part of the game. Works as an expansion.
	* Hachiko was used a lot in the start of the game because he was in the same location as customers.
		* Got stuck in Taito with no customers, so no one wanted to move. Stayed there until end of game.
	* Moving Hachiko gives income to everyone (if track used)
		* With Hachiko, there can be 2 income actions in the same turn, so we need to address this in the rules: Do income actions end your turn, or do you need to set the new cards aside until the end of your turn?
		* Income on your turn. You should draw the cards and set them aside until your turn ends. This should be made consistent with the normal Income action.
* PT#17
	* remove neutral track around Shibuya
	* place Hachiko with customer placement
	* Move with Hachiko doesn't cost a card
* PT#18 Hachiko was fun

### Chairman

* PT#19
	* If Chairman is in your pool, then you can place wherever you want at start of turn.
	* Chairman moves with other customers in that ward.
	* Matches any department store (replaces customer that would have gone there)
	* Ward with your Chairman is wild for you.
	* Action: You can move your chairman to a neighboring space
* Chairman: goal is to increase wildcard opportunities
* Chairman in same location as your dept store is dangerous: you don't get an extra wildcard and everyone else can use it to skip your dept store. 
* Spending an action to move the Chairman might be too expensive. make it free
* Can skip any store?
* PT#21
	* Move once/turn for free
	* Chairman is great. Chaiman not needing action is good.

### Kaiju

* PT#20 first version - destroy things. didn't feel good
	* Destroyed customers are removed from game
	* Destroyed stores and track are returned to player
	* Game goes on longer than expected because we build fewer dept stores and thus have fewer bursts of customers arriving.
		* We only built 3 dept stores instead of the expected 4-5,
		* so we had 4-8 fewer customers arrive and 2-4 extra turns/player.
	* It's odd to allow Lure actions to pass through the location where the Kaiju is located.
* change to scaring and blocking, which matches the theme and doesn't break the core building elements of the game.
* PT#21
	* Kaiju used to good effect near endgame to herd customers in prep for a Lure action. Good because endgame can sometimes be Lure + no other good action.
	* Kaiju great at the right moment
* PT#23 Player gets to move Kaiju for free is their customer lands on the Kaiju spot.
	* Kaiju moving when customer lands there was interested because it added more "random" movement.

### Thief

* Thief customers that match a good and cancel out a matching customer in scoring: 4 thieves: 1/each type
* PT#24 - tested with Paris map
	* Thief added an interesting decision to the game.
	* -1VP penalty for thief is too high.
		* Benefit of thief is being able to skip a store during Move.
		* Perhaps player with most thieves at end of game loses 1pt?
* PT#33 - tested Thief (-1/2 VP)
	* Felt good to pay thief for dept store upgrade
* when drawing, if Thief drawn, draw another customer into that spot
	* important to maintain timing
	* when drawing 2, draw until 2 non-thief

### Empress

* Empress is placed randomly on board. Location is a wildcard for everyone. Player can move once/turn for free.
* PT#23 Empress works well. Similar to Chairman.
* Can be used for new players? To make it easier?

### Flash Mob

* Customer token that immediately draws <n> customers into that location: 4 mobs: 2/3/3/4
* PT#24
	* Possibly have a larger number of small Flash Mobs

### Other expansion ideas

* Extra action
	* PT#42 - Maybe skip next turn for an extra action. Maybe pay a customer for an extra action. Sacrifice something for extra boost.

# --------------------------
# ---------- LAST ----------
# --------------------------

### Move Bypass

* Pay card to skip stores in that ward when moving
* PT#12 - Pay to bypass - not used
* PT#13 - I had the opportunity to use Bypass on Nerima when I had 3 Nerima cards in hand. And I forgot. The rule is not used often enough to be remembers, so it doesn't appear to worth the extra rules weight.

### The player screen

* why? pros/cons
* PT#13 - Game can be long for people who suffer from AP.
* Need to hide customers behind a screen to help reduce AP tendencies.

### Income

* PT#14 - You gain an income action whenever you give another player a customer during Lure

### Stores - Limiting

* PT#10 - 1 store per type (5 total)
* PT#11 - continuing 1 store/type; 2 dept stores
* PT#12
	* More stores per player: 7/6/5 for 2/3/4-player
	* Game is low scoring. It would be nice to add more customers (= scoring potential) without making the game much longer.
* PT#13
	* The economy/income curve in Shinjuku is supposed to be that you draw 5 cards for income, but those 5 cards are worth more later in the game (when you have more stations) than at the beginning.
	*This extra value comes in the form of being more likely to get a card where you have a station (because it becomes a wildcard).
	* Fewer stations mean fewer wildcards, so late game income currently isn't significantly better than early game income. (edited)
	* I'm adding 1 more station for the 4 player game. So that means 8/7/6 stations for a 2/3/4-player game.
* PT#14 - add more station: 8/7/6 for 2/3/4-player

### Stores - Moving

* PT#11
	* 1 player build all their stores and couldn't upgrade (not placed on upgrade spaces)
	* maybe allow moving stores?
* PT#12 - Build store allows you to move an existing store
* PT#15 - Being able to move stores serves as an interesting "attack" during late game when you have a lot of wildcards. Play a card to move a store, then play a card to lure customers.
* If there's a need to reduce the frequency of this, then the cost to move a store can be increased to 2 cards: one for the store's current location and then another for it's new location.

### Wildcards

* already have from stores
* PT#13
	* *More wildcards*: Most of the proposed ways (i.e., doubles, or 3 different cards) to add more wildcards do not follow the desired income curve: they're just as likely early game as near the end.
	* Wildcards need to be based on the player's stores (or track) for them to feel like income.
	* And so that they become more likely as the game progresses.
	* Thus, *half-wildcards*. These are cards for wards that you have a direct connection to from any of your stations. There must be rail on the connection, but it can be any player's rail.
	* Two half-wildcards can be played as a wildcard.
* from 5 cards
	* PT#15 - never used. remove from game
* from 3 cards
	* PT#18 - No "emergency wild" is still painful. The 5-card wards aren't obviously good to new players.
* PT#21
	* Having 3 cards = wild makes the "3-cards to build 2 track" action feel more expensive since those cards now have another possible use.
	* On first turn, you can always get a customer: 3 cards for wild to place store by customer.
* PT#54
	* the flexibility of the 3 card wild means that you move more slowly (because you're spending more cards and need to take more Income)
	* what about mathching color?

### First Blind Playtests

* PT#18
	* ran out of track
	* perhaps have a starter variant (fewer customers) for first time
	* strategy guide needed
* PT#22
* Unclear how luring works, starts a bit slow
	* maybe get 2 stores free? or start with 5 customers on board?
* Things to clarify in rules:
	* Who starts?
	* Can I lure where there is no track?
	* How many tracks per connector?
	* How many customers lured per store during lure? 1? all?
	* "up to 5 for income" -> draw until you have 5
	* Final scoring: what if two types have same #? e.g., 4x 4⭒ 3o 3∆. pick one?
* Create "quickstart guide" with a brief overview of the rules.

### Adjusting track

* PT#11 - 15/12/9 track for 2/3/4 player
* PT#14 - Slightly more track: 16/13/10 for 2/3/4-player
* Require track to be connected
	* PT#16 Shinjuku and Yoyogi are not the same station, so you cannot connect through them.
	* Also issue with Hachiko expansion
	* Should players be allowed to connect through neutral track?
* PT#17 - allow track to be placed anywhere
	* motivated by neutral track in Hachiko expansion
	* deviates from desire to build a connected network, but better for game
* PT#26 - There were times I wanted to build track during the game but had no cards.
Track: The 1-card cost rule has been around for a while and may no longer be necessary:
* It was originally added before you were allowed to drop cards before income, so it was a way to get rid of unwanted cards in your hand.
* Having a track cost a card has sometimes been confusing for new players because they wonder if it matters which card they use (as it does for store building). And maybe they want to hoard cards because they don't know which ones they're going to need later.
* Having to spend an action to build track is already a significant cost
* Track is limited, so there is already negative pressure to spend too much
* Removing the card cost here also reduces the "feel-bad" for starting a turn with 0 cards, since you can place track and then draw Income.
* The 3-card for 2-track cost is also a rule oddity. Esp now that 3-cards = wildcard. There have been times where I needed to spend a wildcard + 2 other cards to get a double-track.
	* Making double-track cost a wildcard is simpler
	* This also makes wildcards more useful.
* Track building rule can be simplified to:
	* Build a single track by taking the Expand action.
	* Optionally spend a wildcard on this action to build a double track.

### 5 players

* PT#9 - 5 players - game felt too short because not enough turns per player
* PT#25 - Last player feels cheated since all the good spots are already taken
	* more of an issue with higher player count
* PT#28 - felt too long. decided to remove support here

### Theme

* PT#28 People keep saying "o" customers - not good theme
* Need to add proper customer types

### Drawing customers

* PT#13 propose burst of customers when dept or store is built
* PT#14 drawing additional customer when store is built
	* BAD Adding 1 customer for each store was a bit tedious. Esp. during the early game.
	* Feel bad: too many customers arrived early in the game, so if you didn't build a lot of stores early you got left out. Hard to recover.
* PT#15 Game could have ended a few turns early, so the game needs to consume more customers. Increase the number of customers that arrive in the burst.
	* Can allow more dept stores in 2-player to get more bursts
* having a burst of customers when a dept store is built
	* PT#15 Place a burst of customers when a dept store is built. Burst = 4/3/2 customers for 2/3/4-player
		* Burst of customers worked well and felt good.
		* It wasn't as tedious as adding customers after each regular store.
	* PT#16 When a department store is built, it triggers a burst of new customers:
		* 4/4/3 customers for 2/3/4-player game.
	* PT#16 Note: we initially forgot to have the burst of customers after dept stores were built. We fixed that when the 3rd dept store was built (by having a very large burst)
	* PT#24 easy to forget because it is rare
* drawing multiple after trigger
	* PT#25 - Draw 2 customers per turn after 2nd dept store is built; 3 per turn after 4th; ...
	* PT#26 - draw 2 after 2nd dept store
	* PT#27 - draw 2 customers after 3rd dept store
* Ramping up the number of customers drawn feels good and is easy to remember.
* same location vs diff location
* Liked having 2 customers drawn into same space.
	* Overall comment: Clumping customers is good

### Upgrading Dept store payment

* PT#9 how to make dept store upgrades more significant and more obvious to players that they are necessary, without making them too easy
	* perhaps require a min # track connections around station before it can be upgraded
	* don't want first turn to be build store, upgrade store
	* want a "story" around the dept store, where players have to work to get there
* PT#10 - dept store is 1st upgrade
	* pay 1 customer to upgrade to dept store
	* spend customers removed from game since there are an exact number for equal number of turns
	* but we missed placing a few, which messed this up (and felt bad)
* PT#11 - Put paid customer back into bag/cup so it gets drawn again later
* PT#12 - Dept store costs 1 matching card + 1 matching customer
* PT#26 - odd to RFG the customer, add to bag?
* PT#28 - After last customer is drawn, if another dept store is built, is the customer added to the bag?
	* Does this customer get drawn next turn?
	* Does that restart the endgame?
	* Probably better to just have the customer removed from game to avoid this problem.
	* need to clarify
* PT#33 - test: customer paid is removed from game
* "sacrifice" a customer
	* Upgrading - "sacrifice" a customer sounds like it involves a bloodletting ritual in the basement. 

### Blind playtests

* PT#30-32 unexpected. asked to borrow a copy
	* I had demo'ed the game. I had rules printed. I had quickstart
* get set of plays
	* got feedback about number of customers to include for the timing to feel right
* timing - removed 8 customers and 2-player felt right
* track felt tight 
* last round 2nd action not useful
	* sometimes it is
* final turn is just Moving to get customers

### Scoring

* PT#8
	* endgame scoring: drop type you have the most of
	* Scoring felt good and forced players to worry about the kind of customers they were luring.
* PT#33 updated customer icons
	* made some double value
	* note about exploring design space
		* we already had thieves (-1 or -1/2 pts)
* double value customers
* PT#33 remove type with most points or most tokens
	* removing most tokens is more interesting
	* mini puzzle at end of game - feels good
	* PT#41 - Player avoided taking another customer because it would hurt her score
	* But she needed to be careful not to reveal this, or else she could be attacked
		* And that's not how the game should feel

Tiebreaking

* PT#16 - Need to either (a) be OK with ties, or (b) have a tie-breaker that strictly orders all of the players (for example turn order).
* PT#28 - Tie at end of game. How to resolve?
	* After removing most common cust type: compare total # of customers
	* User player #
	* Player order from end of game
	* # of pieces remaining (the player that used fewer wins), but this can still be a tie
* PT#29 tiebreaking
	* For resolving ties, look at Knizia's _The Quest for El Dorado_.
	* Have a component that players can acquire that has a strict ranking. In _El Dorado_ these are the dividers between map sections.
	* The ranking of the component should be related to the difficulty in acquiring it. In _El Dorado_, more difficult barriers were worth more for the tie-breaking.
	* For _Shinjuku_, this could be the dept stores. Each of the 12 stores could have a ranking with the better locations being worth less for tie-breaking.

## Gencon playtests

## Speeding things up

Comments:
* PT#38 Holly: Starts slow, but once it gets going it's fun
* PT#40 Slow buildup until first dept store is build.

### More wildcards

* PT#43 & PT#44 - play with Princess expansion to give more wildcards
	* make game start easier
	* PT#43 - One player forgot stores were wild. Was relying on Princess for wilds.
		* Does using the Princess Mod distract from the core wildcard mechanism (stores) for the first game?

### The final round

* PT#34 - Is there an advantage to being the player that triggers the last turn?
	* Not that we've noticed in playtests so far.
* Does the final player have an advantage? None that I can detect, but some players feel this might be an advantage.
* how to address?
* have a final round that gives a psychological break between the main game and the final turn. Each player get a final turn = feels fair.
* At gencon, on player didn't have any cards for final round. felt bad.
* If players aren't paying attention (or if someone else is drawing customers for them), then they may not realize that the game is nearing the end.
* Therefore, grant everyone a free Income action at the start of the Final Round
* But last turn is usually a single Move action. If you have 1 wildcard, then you can do this. If you want another action than 2 wildcards let you do anything you want.
* Income triggered during Final Round is not valuable once you've taken your last turn.
* PT#53 - Why not just remove card draws and Income entirely for the Final Round - you can take any 2 (different) actions you want. 
* later, why have cards in final round

#### Discarding before drawing

* PT#14 - Clarify: you may discard when taking the free Income action.
* Noted how long players took to decide discard in PT#45
* PT#25 and PT#46. didn't seem to help in 25, but the game changed
* PT#25
	* Removing the discard before the free income action sped things up a bit, but also removed the ability to churn through cards to get a wildcard.
	* Overall, this change didn't really help much and is not worth keeping (since it slightly complicates the description of the Income action).
* PT#46: Removing discard from Income felt very good. Update rules to include.
* Seems like the right thing, because players can increase the change of drawing a wildcard.
* but in playtests with new players, it takes time
* experienced players have a heuristic: keep wilds, and then keep other cards that you might use. discard others and draw.
* new players: look at each card. where is this on the map. should I keep it? maybe not, discard and then draw.
* with 3 cards as wild, less of a need to churn for single wildcards
* if you have 5 cards, probably bad to discard vs. drawing to 6
* speeds up game significantly
* removes decision for new players

## Simplifying game setup

### Seeding at the start

* customers
	* PT#7 - seed 3 customers (2-player) and place store anywhere on map
	* PT#8 - seed 2 customers (3-player)
	* PT#9 seed 1 customers (5-player)
		* setup - place customers and then choose location in reverse player order
	* PT#10 seeding customers: 1 cust / player at start
* stores
	* PT#7 - seed 3 customers (2-player) and place store anywhere on map
	* PT#8 - place store anywhere on map
	* PT#9 - place 1st store anywhere on map
	* PT#10 - no free store placement at start

### Setup

* PT#10 - first 1/2 get 1 action per turn
* PT#11 - removed special startup phase
* PT#27 - Only 1 action on first turn for first n/2 players - not necessary
	* was attempting to address balance issues
* PT#27 - sticker both sides of stores to help players quickly remote
* PT#48 - let all player counts start with all 8 stores
	* no need to double-side each store
* let all player counts start with 3 dept store
	* expensive enough that most players won't go to 3 except for 2-player

* Rule for determining first player doesn't work if everyone is in Tokyo.
	* Change to last in Shinjuku station.
	* Although that won't work if people play in Shinjuku station.

### Track

* track - can't be the same for all player counts
* PT#8 - 15 track
* PT#10 - 15 track/player
	* need to reduce track based on number of players
* PT#48 - neutral track
	* give each player same number of track and then use neutral track
* PT#49 - what about less track, but you can move it
	* breaks the story of track - no longer limited
	* you can pull away track that other players are using
		* moved track could be replaced with neutral track

## Randomness and Grouping

## Randomness

* PT#43 - During early game: "Random customer placement - hard to plan"
* PT#44 - In this game, **lots** of customers arrived on the east side (around Edogawa), fewer on the west/south side (Ota/Setagaya). Odd random occurrence.
* PT#53 - Once network is built, random where the customer arrives
* too much randomness. get lucky if a bunch of customers land next to your store

### Making the endgame more interesting

* PT#50 - send double customers to different location
	* not a problem with card drawing, but adds more single customers rather than groups
	* Smaller clumps. Didn't have a clump of 4 and only as clumps of 3
	* Fewer big gunshot moments.

### Updating Move, increase grouping

* problem
	* single customers are often not worth picking up
	* would rather move a group
* considered:
	* must move 2 customers, to force larger moves.
		* But this leaves single customers stranded
	* allow "walking": moves into neighboring regions
		* doesn't feel thematic - want to encourage track usage
	* PT#51 - allow "small moves"
		* move a single customer along track without visiting stores
		* skipping stores feel odd. doesn't match the theme
		* possibly degenerate for 2-player game (go back and forth)
		* not powerful enough to spend a move.
			* should a more powerful version be tested.
			* perhaps allowing extracting a customer from a group?
* must cross track if possible
	* to avoid "turtle" moves - pick up 1 customer and drop rest off in start location
* add more customers to game
	* increase number that come out
	* How many customers would be needed to start the game with 2 customer draws
	* How would that affect the game timer/timing?

### Scoring, part X

* discarding customers feels bad ("Knizia" scoring)
* during playtests, players would sometimes forget this and then be sad
	* PT#44
* it also makes many customers on the map useless to you
* what about set collection? 4,3,2
* endgame bonus of 6/4/2 (or 8/5/3) for sets of 4/3/2
	* prob too much of a bonus given the average score in games
	* maybe bonus of 3/2/1 is good enough
* more complex scoring, can no longer be calculated in head

### More Customers

* PT#8
	* adjust customer count so each player has the same number of turns (from 45 -> 60)
* PT#10
	* placing customer at the end (vs beginning)
		* try not to distract player from their planned actions
		* but we forget
* PT#11
	* removed 1 customer type, thus only 48 customers because of component limits
* PT#12
	* 48 customers
	* New Action: Summon: discard N cards to place N random customers
		* Summon not very useful. Not a satisfying action to do. Would rather do things that work toward VPs.
	* Game is low scoring. It would be nice to add more customers (= scoring potential) without making the game much longer.
* PT#13 - 60 customers
* PT#25 - tried 80 customers - too many
	* game too long even with increased customer draw
* Perhaps try having more customers but arrive more often
* Have a customer that draws extras customers.
	* There is an expansion for that. Should it be brought into core.
* How many customers would be needed to start the game with 2 customer draws?
	* How would that affect the game timer/timing?
* First, try doubling: # customers, # of customers drawn each turn
* Also try:
	* drawing # of customers = # of dept stores + 1
	* reducing the customer count (to ~80?)


## List of things to playtest

* final round
	* ignore cards - players can take any 2 different actions
	* PT#25 Alternate end conditions? E.g., after last customer, then keep going around until no one can take a Move action
		* removes need to act on "sure thing" customers
* dept store upgrade
	* spend 2 matching cards to upgrade to dept store
	* place customers from dept store upgrade back in bag
		* ignore customers for final round
	* upgrading without paying a customer
		* spend 2 matching cards to upgrade to dept store
		* can upgrade during your move when that store gains a customer
			* pay a card
* move
	* allowing move to stop at any point
	* must use track if there are 2 or more customers
* customers
	* doubling customers
		* drawn into different locations
		* drawn into same location

## Other notes


Rough edges vs Texture


===== cut ======

Of course, there can sometimes be an antagonistic relationship between the designer and developer/publisher, and designers can be surprised by the development changes made to their original design. Even Richard Garfield was surprised to have Hasbro make a number of significant changes to his reboot of RoboRally in 2016 (see [this thread](https://www.boardgamegeek.com/thread/1692639/robo-rally-2016-design-notes)). But if you have a good working relationship with the publisher, then this shouldn't be a problem.

====== vv ======

Quote: “Remember: when people tell you something’s wrong or doesn’t work for them, they are almost always right. When they tell you exactly what they think is wrong and how to fix it, they are almost always wrong.” Neil Gaimon

====== mmmm ====


======= gg =======

