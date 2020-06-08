# Playtest #1

* testing:
	* Initial test of basic concept
	* It is necessary to seed the board with customers? Try without seeding.

* components:
	* 18"x20" board with Map of Tokyo
	* 54 cards: 48 Ward cards + 6 wild cards
	* Poker chips for money
	* 20 stores per player (4 of each type)
	* 20 track per player
	* 3 dept stores per player
	* 25 citizen tokens:
		* 5 ◯, 5 ⤫, 5 △, 5 ▢, 5 ⭒

* setup
	* Deal 3 cards to each player
	* Start with 25yen each

* turns:
	* At start of turn, randomly place a citizen on the map. Draw a card to determine the location.
	* Each turn choose an action:
		* Pay 5yen + card, build a store in that ward or next to any of your track
			* Stores can be built on top of other players stores
		* Pay 5yen + card, upgrade an existing store
		* Pay 1yen + card to build 1 track that expands from shop or your track
	* After taking your action, you may optionally resolve the customers in a single ward.
		* You must be able to match all customers in that ward with a shop.
	* At end of turn, draw 1 card

* Final turn
	* When last customer is placed, everyone takes one additional turn.

* actions
	* Upgrading stores
		* Cost 5yen for each upgrade: 1-store -> 2-store -> 3-store -> dept store

			* 1-store can satisfy 1 customer of that type
			* 2-store can satisfy 2 customer of that type
			* 3-store can satisfy 3 customer of that type
			* dept store can satisfy 2 customers of any type, except for the type of the 3-store that it was upgraded from.

* When Resolving customers

	* Each segment of track used pays the owner of that segment 1yen.
	* Each station with a store that resolves a customer pays 5yen to the owner of each store in that station for each customer resolved.
	* Customers must go to the largest store that has the item they want.
		* If they can't reach that store, then they cannot be resolved.
		* If multiple stores are the same size, then the player may choose which one they go to.
	* Customers cannot pass through a store of the matching resource on their way to get to a larger store.
 

First move in game needs to be building a shop, which is restricted by the 3 cards in the player's hand.

1yen and 5yen are a little odd since they correspond to $0.01 and $0.05. But charging 100yen and 500yen (and bumping up the coin values) makes the numbers unwieldly.

How to upgrade to a dept store when there are multiple players with stores in that location?

* Player must remove one of their shops to upgrade?

Who should claim the customer, the store owner or the person taking the customer action?

What if you lose all your money? Pass? How do you get back into the game?

Interesting decisions to be made with "cold war" at top of board: 3 ▢ shops + dept store. Worth 10 vs. 15 (diff of 5) to determine better move.

Shuffled cards once during game.

* next:
	* track costs 2yen and pays out 1yen when used
	* stores cost 10yen and pays out 5yen when customers visit

# Playtest #2

* Testing:
	* Change cost for track and shops: track cost 2, pays 1; shops cost 10, pay 5
	* Increase citizens to 40 (8 x 5 resources)
	* 40 citizen tokens:
		* 8 ◯, 8 ⤫, 8 △, 8 ▢, 8 ⭒

Allow passing? If players want to pass, it means something is broken.

Clarify: can't build on existing tracks

Shuffled cards once during game.

* next:
	* vary the resource distribution
	* reduce the shop/track tokens for each player.

# Playtest #3

* Testing:
	* Fewer shops/dept stores per player
		* 15 stores per player (3 of each type)
		* 15 track per player
	* Different number of citizens for each resource
		* 40 citizen tokens:
			* 10 ◯, 9 ⤫, 8 △, 7 ▢, 6 ⭒

Need to build on first turn. Players can run out of money if they build 2 shops and some track. Then they have to wait until a customer happens by.

Take a loan when short of money: borrow 10 and then pay 1 per turn until it's paid off.

* next:
	* more players.

# Playtest #4

* Testing:
	* More players
	* Explore endgame scoring

Wild cards are time consuming:

* Need to mark the 3 regions that correspond to each wild card
* They are nice when you have them in your hand, but take took long when used to place customers

For scoring, use set collection for customers

Suggestion: Allow 2 tracks to be placed with the same action, but make it expensive: e.g., 20yen

Raise cost for dept stores to 20yen

Bad situation: when dept store is separated from rest of board since that dominates all resources that only have 1-stores on the board.

Should dept stores only provide 1 of each resource (and leave the original shops on the board).

Score rails based on the shops in the stations it is connected to. Similar to Brass. But in Brass, rails don't pay out during the game so they need the endgame bonus. Not sure its needed here.

* next:
	* Test with more players
	* Remove wildcards
	* Allow purchasing multiple tracks with one action

# Playtest #5

* Testing:
	* Having explicit starting locations
		* 6 starting position cards: Ikebukuro, Ueno, Tokyo, Shimbashi, Akihabara, Ebisu (each 2 away from Shinjuku)
	* Explore endgame scoring
	* Resolving Customers: Must go to highest shop that is connected to that customer's starting location (without passing through matching shops)

* loans
	* You may take a loan for (for 10yen) before taking your action.
* dept store upgrading
	* must be a 3-shop stack
	* player must have at least one shop in that stack
	* Cost: ¥20 + 1 card + remove 1 shop from stack
	* Department stores count as 1 of every kind of resource
* Building rail
	* Requirements: must be connected to a station where you have a shop or where you are connected
	* Cost: 1 card (any card) +
		* 2yen for 1st segment placed this turn
		* 16yen for 2nd segment
		* 128yen for 3rd segment


Scoring: Consider the following possible scoring (including all is too cumbersome):

* 1vp for every 10円 (or ¥10)
* 1vp for each of your 1-shop
* 3vp for each player in a 2-shop stack
* 6vp for each player in a 3-shop stack
* 10vp for each dept store
* 1vp for each 1-shop that's part of your rail network
* 3 for each 2-shop
* 6 for each 3-shop
* 10vp for each dept store
* 1vp for each customer
* 3vp for each resource where you have the most
* 20vp if you have one of each resource

Managing money was somewhat tedious. It would be nice not to have to have lots of tiny payouts.

Loans:

* Loans don't feel good.
* What is the max number of loans one can have at a time? 3?
* Spend entire turn to take a loan? (what problem is this trying to solve?)

Sometimes didn't have any good cards in hand.

Wildcards? Perhaps 2 of a kind = wild. Problem: there are many cards that don't have doubles.

J: cards didn't matter unless they match the location of a shop to play on

A: Have 2 actions/turn. Change "resolve customers" to be an action that you must explicity take.

* next:
	* Simplify endgame scoring - only customers give VPs. Make players focus on resolving customers.
		* set collection: vp bonus for 1 of each type
	* Give 2 general actions and make resolving customers an action that the player must take
	* Restrict height in each region, so that dept stores are allowed in city center
	* Resolving customers: You don't have to resolve all the customers, but you must move them all, dropping off customers as they are matched with stores. Unmatched customers are left at the last location.
	* Remove starting locations. Allow players to place first shop anywhere.

# Playtest #6

* Testing:
	* Placing first shop anywhere as part of setup
	* Using doubles for wild card
	* 2 actions per turn
	* restricted height for stations
	* raise track to 20/player (from 15)
	* score only based on customers
	* seed at end of turn (instead of start)

* setup 
	* Each player seeds 2 customers (for 4-player)
	* place a store for free anywhere on the board.

Turns

* Each turn take 2 different actions:
	* Build a store
	* Upgrade an existing store
	* Build rail
	* Lure customers
	* Discard
* At end of turn, draw back up to 3 cards
* When last customer is placed, everyone takes one additional turn. Restricted to 1 Lure action

Player actions

* Building stores
	* Play card for ward, pay 10yen, place store on empty station.
* Upgrading stores
	* On top of one of your shops. Pay 20 for 1st upgrade, 40 for 2nd, 80 for 3rd
* Build Rail
	* For this action, the first section is free, 2nd costs 20yen, 3rd costs 100yen. 
* Lure customers
	* Play card for matching ward to lure customers.
* Discard
	* Discard any number of cards and draw back up to 3

Add action to trigger income.

Draw up to 5 cards in hand (instead of 3)

Add more cards to deck (to adjust probs and reduce shuffling)

Triangle and Square scoring encourage players to focus on a single resource type.

* Triangle score:
	* 1=1; 2=3; 3=6; 4=10;5=15;6=21; 7=28; 8=36
* Squaring score:
	* 1=1; 2=4; 3=9; 4=16; 5=25; 6=36; 7=49; 8=64

* next:
	* 5 cards / hand
	* Add more cards to deck (to ensure that there are at least 2 for each ward)
	* Fix scoring
	* Remove money

# Baseline - After Week 1

5 cards; no seeding

* **Build**: Pay a card, build a store in that ward
* **Upgrade**: Pay a card and a customer, upgrade a store to a dept store
* **Lure**: Pay a card, lure customers from that ward
* **Expand**: Pay any 1 card to build 1 track; pay 3 cards to build 2 connected track
* **Income**: draw up to 5 cards, or draw 1 card if you already have 5 cards. Taking this action ends your turn.


# Playtest 7

* testing
	* seed 3 customers (2-player) and place store anywhere on map
	* need to take Income as a separate action -  no automatic card draw

game has settled to the 5 core actions: Build, Upgrade, Expand, Move, Income

* pay matching card for build, upgrade and move.
* pay any card for expand track
* pay any 3 cards for double-expand track

Clarification: can't split track when adding 2 during the same action - the 2nd must continue from the end of the first.

Experimented with allowing the same action twice. It allowed Adrian to take 2 customer actions to get multiple customers (which felt like a big move), but otherwise it probably isn't worthwhile.

Having to take an action for income didn't feel bad. And it made income from track more exciting.

handling ties: removing type you have the most of

# Playtest 8

* testing
	* seed 2 customers (3-player) and place store anywhere on map
	* endgame scoring: drop type you have the most of
	* add 5 extra customers (45)
	* 15 track

Scoring felt good and forced players to worry about the kind of customers they were luring.

Playing cards in outlying areas felt good because they became wildcards. With only 2 stations in some of these wards, one player would be cut out.

Being able to inject stations into existing lines to prevent other players from resolving customers to their store felt good.

Played well. First candidate for final rules.

* next time:
	* possibly adjust station upgrade limits on map
	* reduce number of stores for each player
	* adjust customer count so each player has the same number of turns

# Playtest 9

* testing
	* 5-player; only 2 stores of each type per player
	* seed 1 customers (5-player) and place store anywhere on map
* continue: 15 track

5 players - game felt too short because not enough turns per player

how to make dept store upgrades more significant and more obvious to players that they are necessary, without making them too easy

* perhaps require a min # track connections around station before it can be upgraded
* don't want first turn to be build store, upgrade store
* want a "story" around the dept store, where players have to work to get there
* what if players started with only 5 stores? then no need for 1,2,3 spots on board
	* players could be stuck since they can't upgrade to 2 stores.

setup - place customers and then choose location in reverse player order

* next time:
	* dept store upgrade the 2nd upgrade - only need to mark locations that can be upgraded
	* 60 customers
	* combine build/upgrade into single action

# Playtest 10

* testing:
	* 1 store per type (5 total)
	* dept store is 1st upgrade ****
	* pay 1 customer to upgrade to dept store - how else to make more expensive?
	* seeding customers: 1 cust / player at start
	* no free store placement at start
	* first 1/2 get 1 action per turn
* continue:
	* 60 customers
	* 15 track
	* scoring drop most common

spend customers removed from game since there are an exact number for equal number of turns
* but we missed placing a few, which messed this up (and felt bad)

GOOD: Game has multiple viable strategies that work

GOOD: Decision when to transition to gaining VPs from building economy

* next:
	* placing customer at the end (vs beginning)
		* try not to distract player from their planned actions
		* but we forget
	* need to reduce track based on number of players

# Playtest 11

* testing
	* reducing number of customer types, only 48 cust because of component limitations
	* no special startup phase
	* 15/12/9 track for 2/3/4 player
* continue
	* 1 store/type; 2 dept stores

1 player build all their stores and couldn't upgrade (not placed on upgrade spaces)

* aadjusted rules to allow dept stores anywhere
* how to address this feel bad moment

too constrained. no useful actions at end of game; not enough stores or track so cant get customers

feel bad - forgot to draw customers. realize at end of game
J: maybe allow moving stores?

* next:
	* More stores per player: 7/6/5 for 2/3/4-player
	* Allow stores to be moved (you can build from your pool or from your existing stores)
	* Dept Store upgrade costs 1 matching card + 1 matching customer
	* Put paid customer back into bag/cup so it gets drawn again later
	* Summon action: discard N cards to place N customers
	* Bypass action: play a card during Lure to bypass all stations in the matching ward

# Playtest 12

* Testing:
	* More stores per player: 7/6/5 for 2/3/4-player
	* Build store allows you to move an existing store
	* New Action: Summon: discard N cards to place N random customers
	* Dept store costs 1 matching card + 1 matching customer
	* Can play a card during Lure to Bypass all stations in that ward.
* continue:
	* 48 customers

Summon not very useful. Not a satisfying action to do. Would rather do things that work toward VPs.

Game is low scoring. It would be nice to add more customers (= scoring potential) without making the game much longer.

* next
	* Try 5 cards wild
	* Different player count
	* Possibly more track
	* Use ⭒ instead of ▢ since they are easier to distinguish from ◯ at a distance.

# Playtest 13

* testing
	* First test with folding map
	* 5 cards = wildcard
	* Bypass during Lure
	* 60 customers, but short game: randomly remove 12 customers for 48
* continue
	* 15/12/9 track for 2/3/4-player
	* 7/6/5 for 2/3/4-player

Game can be long for people who suffer from AP.

Need to hide customers behind a screen to help reduce AP tendencies.

John: Is dept store in center too powerful?

I had the opportunity to use Bypass on Nerima when I had 3 Nerima cards in hand. And I forgot. The rule is not used often enough to be remembers, so it doesn't appear to worth the extra rules weight.

The economy/income curve in Shinjuku is supposed to be that you draw 5 cards for income, but those 5 cards are worth more later in the game (when you have more stations) than at the beginning.

This extra value comes in the form of being more likely to get a card where you have a station (because it becomes a wildcard).

Fewer stations mean fewer wildcards, so late game income currently isn't significantly better than early game income. (edited)

Leading to frustration at the end of the game where you need wildcards to resolve customers.

Possible solutions: add more stations or add more wildcard opportunities.

*More stations*: I'm adding 1 more station for the 4 player game. So that means 8/7/6 stations for a 2/3/4-player game. This should help a bit without removing the interesting decisions associated with having a limited number of stations.

*More wildcards*: Most of the proposed ways (i.e., doubles, or 3 different cards) to add more wildcards do not follow the desired income curve: they're just as likely early game as near the end.

Wildcards need to be based on the player's stores (or track) for them to feel like income.

And so that they become more likely as the game progresses.

Thus, *half-wildcards*. These are cards for wards that you have a direct connection to from any of your stations. There must be rail on the connection, but it can be any player's rail.

Two half-wildcards can be played as a wildcard.

Also, how to have more customers appear in the game: A burst of customers whenever a dept store is built. Or (via Adam) a new customer whenever any store is built.

* next
	* Remove Bypass

# Playtest #14

* Testing:
	* Place a new customer every time a store is built.
	* Slightly more track: 16/13/10 for 2/3/4-player
	* 1 more station: 8/7/6 for 2/3/4-player
	* You gain an income action whenever you give another player a customer during Lure
	* 5 diff cards = wildcard
* continue
	* 60 Customer tokens: 19 ◯, 16 ⤫, 14 △, 11 ⭒
	* 2 dept stores per player

Can build on existing shop? No.

At end of game:

* Adam had 3 stores and 0 track remaining
* Jeff had 2 department stores and 2 track remaining. No dept stores were built.
* Gary had 0 stores and 5 track remaining.

Higher scores without the game taking too long. Yay!

BAD: Adding 1 customer for each store was a bit tedious. Esp. during the early game.

Clarify: you may discard when taking the free Income action.

Being able to take Income when you give another player a customer during Lure didn't feel worth it. Extra rule and it didn't make giving a VP feel better. I.e., if you going to give another player a VP, then it'll be because you get a VPs as well, and getting an Income action will not make you more likely to give someone else a VP.

16 customers left on board at end of game. Some stranded (no track) others just lower prio.

Feel bad: too many customers arrived early in the game, so if you didn't build a lot of stores early you got left out. Hard to recover.

* next:
	* Draw a burst of customers when dept stores are built (instead of 1 every time a store is built).

# Playtest #15

* Testing:
	* 2 player
	* Place a burst of customers when a dept store is built. Burst = 4/3/2 customers for 2/3/4-player
	* 5 diff cards = wildcard

Burst of customers worked well and felt good. It wasn't as tedious as adding customers after each regular store.

Targetting ⭒ customers worked well as a strategy (because of their limited number).

Using 5 different cards as a wildcard has never been used in a playtest. No need to keep it as a rule.

Being able to move stores serves as an interesting "attack" during late game when you have a lot of wildcards. Play a card to move a store, then play a card to lure customers.

* If there's a need to reduce the frequency of this, then the cost to move a store can be increased to 2 cards: one for the store's current location and then another for it's new location.

Game could have ended a few turns early, so the game needs to consume more customers. Increase the number of customers that arrive in the burst.

I can bump that up to 5 or have 3 dept stores in a 2-player game.
... or both, I suppose.

This playtest was 2 player x 2 dept x 4 customers = 16 customers

Assuming that everyone builds all their dept stores:

* 4 players x 2 dept = 8 events x 3 = 24 customers
* 3 players x 2 dept = 6 events x 4 = 24 customers
* 2 players x 3 dept = 6 events x 4 = 24 customers

* next:
	* Update dept store burst to 4/4/3 for 2/3/4-player
	* Update number of dept stores to 3 in 2-player game

# Playtest #16

* Testing:
	* Hachiko Expansion:
		* Shibuya + 4 neutral track
		* Reunite Action: Move Hachiko to Shibuya, taking customers (as with Lure) and give income to anyone who owns track Hachiko uses (incl player who took action).

* continue: 
	* When a department store is built, it triggers a burst of new customers: 4/4/3 customers for 2/3/4-player game.

Shinjuku and Yoyogi are not the same station, so you cannot connect through them.

The neutral track around Shibuya (with the expansion) makes it harder for more than 1 player to build connections.

Should players be allowed to connect through neutral track?

* Yes? (but test)

Should the connection between Shinjuku and Yoyogi be described as "neutral" track?

Income on your turn. You should draw the cards and set them aside until your turn ends. This should be made consistent with the normal Income action.

Note: we initially forgot to have the burst of customers after dept stores were built. We fixed that when the 3rd dept store was built (by having a very large burst)

Tied! With the exact same set of customers.

Need to either (a) be OK with ties, or (b) have a tie-breaker that strictly orders all of the players (for example turn order).

Hachiko. Not a negative, but not a core part of the game. Works as an expansion.

Natural color of wood is hard to see against the map.

Hachiko was used a lot in the start of the game because he was in the same location as customers.

Got stuck in Taito with no customers, so no one wanted to move. Stayed there until end of game.

When Hachiko is in a location without customers, then the only benefit is the Income. But if everyone gets income, then there's less reason for you to do it (you'd rather someone else does it). And moving Hachiko with no customers possibly gives the next player a better position if Hachiko lands on a location with customers.

Should Hachiko only give Income to the player who uses Hachiko (as opposed to everyone)?

Note: With Hachiko, there can be 2 income actions in the same turn, so we need to address this in the rules: Do income actions end your turn, or do you need to set the new cards aside until the end of your turn?

* next:
	* Try Hachiko only giving Income to the player who takes the action
	* Track can be expanded through neutral connections
	* Final tie-breaker based on turn order: 1st player wins over 2nd player wins over 3rd ...
	* Taking the Income action doesn't end your turn immediately, but you don't get the new cards until the end of your turn. Any drawn cards should be set aside facedown until the your turn ends.

# Playtest #17

* Testing:
	* Place single track anywhere (to resolve placement issues around neutral track) Double track can be anywhere but the 2 segments must be connected
	* Hachiko expansion: Remove neutral track around Shibuya. Hachiko starts in Shibuya. If H is in Shibuya at the start of your turn, then you place Hachiko with your customer placement. When you Lure from a ward with Hachiko, it doesn't cost a card, but you must take Hachiko with the other customers and end the Lure in Shibuya.

Hachiko good.

Only 5 of the 8 possible dept stores were built.

Leftover stores: Gary ⤫⭒; Sverre ◯⤫⭒; none for others

Leftover track: Gary 1; none for others

* next:
	* Hachiko: Remove track around Shibuya
	* Seed more during burst

# Playtest #18

* Testing:
	* New players	
	* Hachiko Expansion without neutral track around Shibuya

Shinjuku + Tokyo -> Beast Mode!

No "emergency wild" is still painful. The 5-card wards aren't obviously good to new players.

@15 tokens left, felt too long

Player stuck with 5 cards, but no wilds @ 2 shops + dept store. Really stuck because no track in late game - spent it all in early game).

New players don't know that rail is sparse, and sad to have no actions later in game.

Comment: action to draw => ends turn is sad. Maybe draw 1 each turn?

Did not finish, but scores were normalish. Did not explain endgame scoring to players, so just used each customer = 1 VP.

Hachiko was fun.

* next:
	* Create starter game (with fewer customers) for teaching and first-time players. Easier scoring.
	* Create strategy guide for players.

# Playtest #19

* Testing Chairman expansion:
	* If Chairman is in your pool, then you can place wherever you want at start of turn.
	* Chairman moves with other customers in that ward.
	* Matches any department store (replaces customer that would have gone there)
	* Ward with your Chairman is wild for you.
	* Action: You can move your chairman to a neighboring space

Chairman: goal is to increase wildcard opportunities

Chairman in same location as your dept store is dangerous: you don't get an extra wildcard and everyone else can use it to skip your dept store.

Spending an action to move the Chairman might be too expensive.

* next:
	* Chairman: Add option to move chairman for free once per turn (no action)
	* Chairman can skip any store (not just dept stores)

# Playtest #20

* Testing Kaiju expansion
	* Play matching card to move Kaiju into a neighboring ward and destroy something.
	* Kaiju starts in water. Need wildcard to move it out.
	* Kaiju action: Play a card matching Kaiju action to (optionally) move Kaiju into neighboring ward and (optionally) destroy something in that ward.
		* Destroyed customers are removed from game
		* Destroyed stores and track are returned to player

Kaiju is an action and can only be taken once/turn.

Adam: It's odd to allow Lure actions to pass through the location where the Kaiju is located.

Adam: Instead of destroying, have the Kaiju scare customers away.

* Into a neighboring ward. Player chooses. All customers must go to the same ward.
* No infrastructure desctruction

Kaiju: Game goes on longer than expected because we build fewer dept stores and thus have fewer bursts of customers arriving. We only built 3 dept stores instead of the expected 4-5, so we had 4-8 fewer customers arrive and 2-4 extra turns/player.

Any variant/expansion that allows destruction needs to account for the fact that fewer dept stores will be built, so there will be fewer bursts from that. Otherwise the game will last a bit too long.

* next
	* Kaiju:
		* Scares customers instead of destroying things
		* Lure actions cannot pass through Kaiju location
	* What about 3 cards = wildcard?
		* PRO: Makes 5 non-wildcards (e.g., your first turn) not so bad
		* CON: Removes some incentive for building stores
		* Does it make it too easy to perform any action you want? Would that be bad?

# Playtest #21

* Testing:
	* Any 3 cards = wildcard
	* Chairman expansion: Move once/turn for free
	* Kaiju expansion: Scare customers into neighboring ward - no destruction
	* Kaiju + Chairman expansion together

On first turn, you can always get a customer: 3 cards for wild to place store by customer. Place Chairman to match remaining card in hand and play that card to Lure.

Clarification: When customer should go onto space with Kaiju, the player gets to choose which neighboring ward it goes into. ISSUE: Decision possibly affected if player sees the customer type before choosing.

3-way tied score. Tie resolved by player order (G wins). Older tie-breaking rules would have multiple rounds of tie-breaking between J and A since they both have 4+4+4+3.

Jeff: Chairman is great. Chaiman not needing action is good.

Adam: Kaiju great at the right moment

Gary: Kaiju used to good effect near endgame to herd customers in prep for a Lure action. Good because endgame can sometimes be Lure + no other good action.

Jeff: When draw customer @ Kaiju, move Kaiju

Gary: Having 3 cards = wild makes the "3-cards to build 2 track" action feel more expensive since those cards now have another possible use.

* next
	* When customer is placed at Kaiju location, then the Kaiju should move (to a location chosen by current player). Customer can then be placed in that ward. This effectively adds a random movement to the Kaiju.
	* Multiple Kaiju that act differently and battle (destroying stuff) when they are in the same location.

# Playtest #22

* Testing:
	* Blind playtest of rules

Lucy:

* POS: Luring, Story was great
* NEG: Unclear directions, Lure should be any card

John:

* POS: Station names & story; Fun luring lots of customers!
* NEG: Unclear how luring works, starts a bit slow (maybe get 2 stores free? or start with 5 customers on board?)

Megan:

* POS: Moving stores, lots of strategy!

Other notes:

Easter egg colors, not good for colorblind

Things to clarify in rules:

* Who starts?
* Can I lure where there is no track?
* How many tracks per connector?
* How many customers lured per store during lure? 1? all?
* "up to 5 for income" -> draw until you have 5
* Final scoring: what if two types have same #? e.g., 4x 4⭒ 3o 3∆. pick one?

GOOD: Looking at lure routes! neat strategy opps.

* For next playtest:
	* Update rule book to address ambiguity.
	* Create "quickstart guide" with a brief overview of the rules.

# Playtest #23

* Testing:
	* Empress expansion. Empress is placed randomly on board. Location is a wildcard for everyone. Player can move once/turn for free.
	* Kaiju: Player gets to move Kaiju for free is their customer lands on the Kaiju spot.
	* Kaiju + Empress expansion together

Kaiju moving when customer lands there was interested because it added more "random" movement.

Only 3 dept stores were built. Jeff built his near end of game.

Empress works well. Similar to Chairman.

# Playtest #24

* Testing:
	* Paris map
	* Thief expansion - Thief customers that match a good and cancel out a matching customer in scoring: 4 thieves: 1/each type
	* Flash Mob expansion - Customer token that immediately draws <n> customers into that location: 4 mobs: 2/3/3/4

Note: No need to remove customers for Flash Mob. Rules are already written this way, but I accidentally tried to do this when removing customers for the Thief.

* It might be nice (for consistency) if none of the expansions required removing customers during setup.

Paris Map:

* Need to place the dept store icon outside the circle on the map because it is covered up by a store during gameplay.

Oops! Forgot to have a burst of customers when we placed a dept store

* Corrected (after we noticed) by placing 2 customers per turn until end of game

During game, RobinS: How many of each customer type are in the bag?

* 60 customers: 18 ◯, 16 ⤫, 14 △, 12 ⭐︎
* It's in the rulebook, but should place that information on the board somewhere

Game took longer than normal - ~1h20

* And felt like it should have been over since we all had our engines and were just trying to pick up the remaining customers.
* Why?
   * We forgot to burst the dept stores
   * Possibly took more time thinking about the new map?

During endgame, we had a bunch of single customers on the map. These are less interesting since you want to Move a group.

Sverre:

* Possibly have a larger number of small Flash Mobs

Jeff:

* Thief added an interesting decision to the game.

To make endgame more interesting:

* Add more customers
* Draw them faster from the bag
* Draw 2 customers/turn once the 2nd dept store is built
   * Should both go to the same location? or separate draws for each?
* This may have to be adjusted based on number of players

Possible expansions:

* "Lock" customers so they can't be Moved
* Pick up customers along the way (perhaps by playing a card)

-1VP penalty for thief is too high. Benefit of thief is being able to skip a store during Move. Perhaps player with most thieves at end of game loses 1pt?

* For next playtest:
	* Add more customers (up to 80)
	* Accelerate the customer draws after 2nd dept store is placed
	* Also, note on board how many of each customer type

# Playtest #25

* Testing:
	* 5-player - 2 new players
	* Draw 2 customers per turn after 2nd dept store is built; 3 per turn after 4th; ...
   * This replaces having a burst of customers appear when a dept store is built
	* 80 customers: 25 ◯,  22 ⤫,  18 △, 15 ⭒
	* For the free income action (when another player uses your track), no card discard before drawing. To see if this speeds up game.

Needed to stop game early because of time. Just barely reached point where 3 customers/turn were being placed.

80 customers is too many (even with increased customer draw).

Ramping up the number of customers drawn feels good and is easy to remember.

* Having a burst of customers only after a dept store build was easy to forget.
* Need to balance the correct number and proper trigger (may change based on number of players).

Removing the discard before the free income action sped things up a bit, but also removed the ability to churn through cards to get a wildcard.

* Overall, this change didn't really help much and is not worth keeping (since it slightly complicates the description of the Income action).

Five players, but only 4 dept stores were built.

Lots of customers available, but players may have been hesitant to take them because they needed to pass through other player's stores. (I think this is kinda by-design).

Sam:

* POS: Fun to build dept stores and connections
* NEG: Not knowing where to build track at start of game

Leonard:

* NEG: Last player feels cheated since all the good spots are already taken
* NEG: Unlucky with cards
* NEG: Accelerated too fast

Sverre:

* NEG: Not sure it plays well with 5 players
 * _(perhaps because of beginning players taking longer?)_

Jeff:

* Alternate end conditions? E.g., after last customer, then keep going around until no one can take a Move action

* For next playtest:
	* Figure out best # of customers to draw
	* Reduce back to 60 customers
	* Revert back to allowing discard before free draw.

# Playtest #26

* Testing:
	* Draw 2 customers per turn after 2nd dept store is built
		* This replaces having a burst of customers appear when a dept store is built
	* Only 1 action on first turn for first n/2 players (rounded down)
	* Chairman expansion
	* Paris map

Two new players: one player playing their 1st game; another on 2nd.

Game stopped early (after about ~45 min) because of time. Startup took longer with rules explanation.

When upgrading to a dept store, it's a bit odd to remove the customer from the game. No obvious place to put it other than in the box. It would be easier to just put it back in the customer bag.

Track:

* Surprisingly little track built during game. This made it hard to Move customers to stores. Track was starting to be built near end of game, but we stopped early.
* Jeff: There were times I wanted to build track during the game but had no cards.
* New players reluctant to use other player's track?

Rule clarification: Can the Chairman be moved after taking an Income action?

* No, turn ends when Income action is taken. Otherwise, player will draw cards and then have to think a lot about their plan. We want to push this thinking so that players do it during other player's turns.

How to encourage more track building?

* Sam: Make some track a pre-req for building a store
* Jeff: Should building a single track be free (but still require an action)?

Track: The 1-card cost rule has been around for a while and may no longer be necessary:

* It was originally added before you were allowed to drop cards before income, so it was a way to get rid of unwanted cards in your hand.
* Having a track cost a card has sometimes been confusing for new players because they wonder if it matters which card they use (as it does for store building). And maybe they want to hoard cards because they don't know which ones they're going to need later.
* Having to spend an action to build track is already a significant cost
* Track is limited, so there is already negative pressure to spend too much
* Removing the card cost here also reduces the "feel-bad" for starting a turn with 0 cards, since you can place track and then draw Income.
* The 3-card for 2-track cost is also a rule oddity. Esp now that 3-cards = wildcard. There have been times where I needed to spend a wildcard + 2 other cards to get a double-track.
	* Making double-track cost a wildcard is simpler
	* This also makes wildcards more useful.

Track building rule can be simplified to:

* Build a single track by taking the Expand action.
* Optionally spend a wildcard on this action to build a double track.

For next playtest:

* For Expand Track action: building single track does not cost a card; building 2 track costs 1 wildcard
* More testing of multiple customer draw
* The customer paid when building a dept store should be placed back in the customer bag.

# Playtest #27

* Testing:
	* Draw 2 customers per turn after 3rd dept store is built
		* This replaces having a burst of customers appear when a dept store is built
	* Only 1 action on first turn for first n/2 players (rounded down)

Josh

* Board could be darker visually so that the pieces stand out
* Most fun: moving lots of customers
* Dissatisfying when there were few customers

John

* Good balance between complexity and time to play
* The stores could have stickers on both sides so that it is easier to sort them at the beginning of the game.

For next playtest:

* Drawing 2 customers after 3 dept stores are build is good.
* Limiting action for first n/2 players is not necessary.

# Playtest #28

* Testing:
	* 5 players
	* 2 new players
	* Placing both drawn customers into same location

* continue
	* Draw 2 customers per turn after 3rd dept store is built
	   * Place both customers into same location
	* Per player: 2 dept stores, 5 stores, 9 track (for 5-player game)
	* Throw the bag of customers at the next player so that they know it's their turn.

Started with 3 player AdamB, KenK, self). Restarted when more people arrived.

Patchwork track, because it's easy to place.

People keep saying "o" customers - not good theme

Feel bad - Sverre with only 2 cards. But he put himself that in that position.

Katsushika and Sumida. Colors too close. Hard to tell difference (across the water) in low light. Perhaps use a different pattern.

Slow with 5 players. Too much down time? But 2 new players.

Expansion: Hachiko would be much more powerful if it provided a new action that could earn customers.

After last customer is drawn, if another dept store is built, is the customer added to the bag?

* Does this customer get drawn next turn?
* Does that restart the endgame?
* Probably better to just have the customer removed from game to avoid this problem.

Tie at end of game. How to resolve?

* After removing most common cust type: compare total # of customers
* User player #
* Player order from end of game
* # of pieces remaining (the player that used fewer wins), but this can still be a tie

Overall comment: Clumping customers is good

Liked having 2 customers drawn into same space.

For next playtest:

* Cutomer paid for dept store is removed from game.
* Remove 5th player support from base game
* Draw customers into same location

# Playtest #29

* Testing:
	* 2 new players (1 first game, 1 second game)
	* Draw customers into same spot when drawing multiple

Josh:

* Like realistic Tokyo map with stations

Ken:

* Likes "tokening" (cf 18xx games)
   * Use tokens/stations to define line, but can be used offensively to block/tax other players
   * Really enjoyed this aspect
  
Adam:

* For resolving ties, look at Knizia's _The Quest for El Dorado_.
   * Have a component that players can acquire that has a strict ranking. In _El Dorado_ these are the dividers between map sections.
   * The ranking of the component should be related to the difficulty in acquiring it. In _El Dorado_, more difficult barriers were worth more for the tie-breaking.
   * For _Shinjuku_, this could be the dept stores. Each of the 12 stores could have a ranking with the better locations being worth less for tie-breaking.

For next playtest:

* Customer paid for dept store is removed from game.

# Playtest #30-32

* Testing:
	* Someone else teach game to new players
	* Reducing customer count by 8

(from Ken)

I changed "Lure" to advertise in my teachings and that was received really well by players. As you and I discussed, language adds a lot to the game. So when someone would say, "I am going to advertise food in Manato." It began to feel really immersive.

* 2- player | 70 mins w/ teach | Score: Ken: 22- Jonathan: 15
	* Played w/ main rules except in phase 2 placed both customers on the same location
	* Phase 2 seemed to drag on forever. Pretty clear who had won 2-3 rounds before game ended

* 3-player | 58 mins w/o teach | Score: Ben: 15, Ken: 11, Jeremy: 9
	* Played with the same ruleset as above
	* Combined Positive Notes
		* Income works really well
		* Three cards for a wild feels good, able to do what you need to. Adaptable
		* Engaging in every person turn
		* Great length and quick turns are nice
		* Forced interaction great
	* Combined Negative Notes
		* Tracks ran out in 3p, felt bad
		* Last round feels like the second action is useless and if you’d don’t have the right card it feels bad. 
		* Station kanji (sp?) too big

* 2-player | 66 mins w/ teach | Score: Ken: 13 - Emily: 13 (Won on having more overall customers)
	* Played with same rulles as above but removed 8 customers, felt like it ended at right time
	* Negative Notes
		* Ran out of track
		* Because of wild rule, feels like late game card draw is less meaningful and bad draws feel bad
		* End feels a little flat because you just advertise (mention lure being weird)
	* Positive Notes
		* "Easy to learn and felt like a better than some of the game you (Ken) have bought."
	* Final Score breakdown
		* E- 6, 4, 4, 5
		* K- 5, 4, 4, 4,
		* E won on more customers overall
   
"...after I removed 8 customers (one of each resource type), the two-player game seemed to end at a much better moment."

For next playtest:

* Reduce customer count by 8

# Playtest #33

* Testing:
   * New icons on components
   * Customer paid for dept store cost is removed from game
   * 56 customers
   * Multiple customers drawn into same location
   * Double customers
   * Thief expansion
	* 1 new players (1 first game)

Clarifications:

* When paying a customer to upgrade, pay a single token (double or thief is OK)
* When drawing customers at start of turn, if a thief is drawn, keep drawing until a non-thief is drawn.
* When drawing 2 customers, draw until 2 non-thief customers are drawn.

Jeff:

* Assumed that the customer type to remove during scoring was going to be based on number of tokens rather than number of points.
   
For next playtest:

* When scoring, remove customer type that you have the most tokens of (rather than most points)

# Playtest #34 - GenCon

FEPH - First Exposure Playtest Hall

* Is there an advantage to being the player that triggers the last turn?
  * Not that we've noticed in playtests so far.

# Playtest #35 - GenCon

* Clarify in rules:
  * Passing through another player's station does not trigger income
  * You may pass through an empty station
  * Can wildcards be used to upgrade from Store -> Dept Store [make this explicit in rules)

"Drawing customers at start reminds me of Pandemic"

Passerby: "Is this Catan in Tokyo?" :-7

Consider adding legend on map that shows the customer info (# of each type)

# Playtest #36 - GenCon

* Amy reviewed the rulebook and found some places that needed clarification (yay!)

# Playtest #37 - GenCon

* Clarify: During Move action, you do not accumulate customers that you pass along the way.

Timestamps:

* 4:33 Game start
* 4:55 First dept store built
* 5:03 Third dept store built
* 5:30 Game finished (start scoring)

# Playtest #38 - GenCon

Rules clarifications:

* Only one store per station
* Only one track per connection
* Can move through empty stations (but not across missing track)

Discussed strategy of using card doubles to make a wildcard (build a store with the first one, 2nd becomes wild).

Noted that we will go through the deck ~3 times (shuffling twice)

Holly: Starts slow, but once it gets going it's fun

Timestamps:

* 8:33 Start
* 8:56 1st dept store
* 9:05 2nd dept store
* 9:06 3rd dept store
* 9:18 4th dept store
* 9:29 End

# Playtest #39 - GenCon

Timestamps:

* 2:24 Start
* 2:58 1st dept store (green)
* 3:05 2nd dept store (blue)
* 3:07 3rd dept store (red)
* 3:22 End
* 3:26 Finished scoring

# Playtest #40 - GenCon

Slow buildup until first dept store is build.

What about having an initial setup (like Catan)? This would give more first player advantage.

Passerby: "When will this be available?"

Timestamps:

* 6:45 Start (late)
* 7:22 1st dept store
* 7:25 2nd dept store
* 7:41 3rd dept store
* 7:46 4th dept store
* 7:51 Stopped with 7 customers remaining

# Playtest #41 - GenCon

Noted that first move is commonly Build + Expand

Rule clarifications:

* Matching customer to upgrade to a dept store must be one that was earned previously. It doesn't come from the board.
* "Can we look through the discard pile?" No, and note that we'll be going through the deck multiple times.
* "Can start move in empty station (without store)?" Yes
* "Can you refuse to take a customer?" No (see scoring discussion below)

Having 0 cards for the last round doesn't feel good.

"I wasn't sure I would like this game when I sat down, but I want to play again."

"Looks like Ticket to Ride, but doesn't play like it"

Update cards: The map has been updated to have double lines around dept store locations (in addition to the icon), but the cards have not. ([tracking issue](https://github.com/garykac/shinjuku/issues/3))

Timestamps:

* 8:10 Begin rules explanation
* 8:26 Start game
* 8:56 1st dept store
* 8:57 2nd dept store
* 9:04 3rd dept store
* 9:05 4th dept store
* 9:11 5th dept store
* 9:24 End

Scoring mini puzzle:

* On Krystal's last turn, she had the opportunity to acquire more customers with her Move action, but chose not to (she ended her Move early).
* She could have gained an additional Food customer
* Doing so would have caused her to have more Food tokens than any other type.
* Avoiding this Food customer resulted in her having a 3-way tie between Food, Clothing and Electonics for the most tokens, which allowed her to choose the one with the fewest points.
* Note that another player could have noticed that she avoided taking this Food customer and given her one on their Move action.

For next playtest:

* When last customer is drawn, that player finishes their turn and then it enters the Final Round.
* Every player takes an Income action at the beginning of the Final Round and then takes their turn.
* This serves to:
  * Eliminate the possibility of having 0 cards for the last turn
  * Places a "barrier" between the main game and the last turn so that it doesn't feel like the person who drew the last customer gets 2 final turns.
* ([tracking issue](https://github.com/garykac/shinjuku/issues/4)) to update the rules

# Playtest #42 - HyperboopiCon

Playing with princess expansion

Rule reminders (during game):

* Income ends your turn
* Once you start a move, you can stop at any time. Your aren't required to continue
* Be careful with terminology: stations vs stores
* Clarify Move must end with satisfying a customer. Can this info for on the player screen?

Need to fix map to clarify adjacent wards. Example, Ota and Koto.

Would like to be able to pick up customers along the way

Sverre would like more actions. Maybe skip next turn for an extra action. Maybe pay a customer for an extra action

For next playtest:

* Make Dept store locations black with white text to make them pop
* Is it possible to sacrifice something to get an extra action?

# Playtest #43 - Tokyo (Sangenjaya)

Playing with princess expansion

Map comments:

* Perhaps use Kichijoji (note: it's off the map in Mushashino)
* Futakotamagawa instead of Todoroki
	* Todoroki is tiny

Rule for determining first player doesn't work if everyone is in Tokyo. Change to last in Shinjuku station. Although that won't work if people play in Shinjuku station.

During early game: "Random customer placement - hard to plan"

* Note that this changes in mid-game

Rule reminders (during game):

* Only one store is allowed per station
* One player forgot stores were wild. Was relying on Princess for wilds.
	* Does using the Princess Mod distract from the core wildcard mechanism (stores) for the first game?

# Playtest #44 - Tokyo (Azabujuban)

Playing with princess expansion

Consider mentioning to new players not to overcommit to a single area (especially early in the game).

One player forgot (until reminded late in the game) that you don't score the customer type that you have the most of.

In this game, **lots** of customers arrived on the east side (around Edogawa), fewer on the west/south side (Ota/Setagaya). Odd random occurrence.

For next playtest:

* Don't use Princess Mod for initial teaching game

# Playtest #45

Clarification: You don't automatically gain matching customers that are in the ward where you build a store. You must take the Move action.

Note that the contrast between Sumida and Katsushika could be improved. Changing Katsushika to Green would fix this problem.

How can Income be sped up? New players take a long time deciding which cards to discard.

# Playtest #46

Testing:

* Paris Map
* 2 player
* Don't discard as part of Income

Removing discard from Income felt very good. Update rules to include.

# Playtest #47

Testing:

* London Map (first time)
* 2 player

Boroughs along border that are not part of the game should be grey (instead of colored).

Fast game: 11:35 - 12:18

Map too connected with too many close dept stores.

Too many customers arriving in Westminster. Yet too easy to avoid other player's dept stores.

Having Westminster be too large upsets the balance of the game.

Some of the stations on the map are too close together.

next:

* Consider a shared pool of neutral track that is used when a player runs out. Possibly only for double track,

* Rework the London map to use the pre-1965 metropolitan boroughs.
	* They were much smaller and covered just the central core of London (which is all we care about.
	* The board could them zoom in on the core of London and still have about 20 regions. This would allow more interesting stations to be included and they wouldn't be too close together.

# Playtest #48

* Testing:
	* Updated Tokyo map (additional station in Setagaya)
	* always use 8 stores and 3 dept stores
	* Track 9/player with additional neutral track
		* You may use neutral track instead of your track
		* Trying to determine if there can be a set amount of track that doesn't need to be adjusted based on player count.

Rules clarification:

* When double expanding through Yoyogi/Shinjuku, you need to play the card that matches the first track that you placed.
* Move:
	* may stop whereever you satisfy a customer
	* must continue at if you haven't satisfied

Josh: "I don't like this game" "This is a good game"

* note: first comment was expressing frustration with his position, not the game in general ^_^

Used 34 track in total

Possibly require that the 2nd track is neutral (if possible). To remove the decision and streamline game.

J: Should neutral track be available at more cost?

J: Is neutral track (and the decision) good for new players?

J: New player question:

* Where to place track?
* Can hints be placed on the map? Like connect dept stores

Another hint: don't commit to a part of the map too early.

Neutral track was interesting, but probably for an expansion.

* Next time:
	* Department store locations on the map need to be larger - hard to see when covered

# Playtest #49

* Testing
	* 10 track per player but you can move track on map

A: now you can snipe with track but building it and then moving it away when the other player needs it.

* fix: when track is moved, it is replaced with neutral track

Being able to move track breaks the Track story arc. No longer constrained because you can move from anywhere.

More likely to have fully connected sections of may since track can be moved (relatively low cost) to bypass players.

But it does allow the network to reach new customers that are dropped in new areas.

* next:
	* re-test drawing 2 customers into different locations

# Playtest #50

* Testing:
	* Placing double-customers in separate locations (instead of placing both in the same location)

J: why not order the actions?
(Re: the rule that Income must be the last action in a turn)

* Adds rule complexity. Is it worth it?
* A: could add a rondelle - perhaps an expansion

J: For the last half I wanted to do something but wasn't able to do it. Trying to get more video games. Probably should have tried for books.

* Didn't have a customer dist reference to know that Video Games were rare. There probably weren't any more to get.

Impact of having double-customers sent to different locations:

* Smaller clumps. Didn't have a clump of 4 and only as clumps of 3
* Fewer big gunshot moments.

Having more customers in the game:

* Perhaps try having more customers but arrive more often
* Have a customer that draws extras customers. There is an expansion for that. Should it be brought into core.
* How many customers would be needed to start the game with 2 customer draws
* How would that affect the game timer/timing?

What is Fun in this game?

* Big moves across board
* Needing to give other players a customer

A: A crazy change:

* Another free action: "walk" move customers 
* Like in Kaiju
* Feels too big for a free action
* Or move just a single customer
* That would address the problem with single customers on the board not worth picking up

* Todo:
	* Revert to placing 2 customers in same location
	* Consider adding more customers

# Playtest #51

* Testing:
	* New action: Move a single customer along a single segment of track - skipping stores
		* Can only move customer if they are alone in ward
		* Idea is to allow customers to be grouped my moving them together

Skipping stores feels odd

A: Does this rule change encourage suboptimal play?

Also, this is degenerate for 2 players:

* Can move customer back and forth
* cf. Ko rules in Go

A: change Move action - must satisfy at least 2 customers. To encourage bigger moves

A: Note: If small Move must follow track, then it can easily be moved back (because there is track).

* Small move is most useful as a 1st move followed by a real move.

J: "Gary, sometimes you make me sad"

New action is not powerful enough to use. Should a more powerful version be added/used?

Perhaps allowing a single customer to be extracted from a group and moved to a neighboring ward.

None. Next playtest will be with new players.

# Playtest #52 - Tabletop Network

* Testing:
	* New players

Rule clarifications:

* empty stations - can they be used? yes
* players may forget about store wildcards

"good player aids"

Q: seed board at start? But then need to worry about 1st player advantage
Scores (single/double = total):

Need tiebreaker when neither player has a dept store. Or if only 1 player has a dept store.

* todo:
	* Clarify tiebreaking rules.

# Playtest #53 - Tabletop Network

* Testing:
	* New players

What is the best way to hold cards? Maybe add an Index in the corner.

I: Once network is built, random where the customer arrives

What about final round just assume everyone has 2 wildcards

I: didn't give customers to other players very often

I felt too open, you could avoid other players to easily. Point in middle when you cared about other stores - but you could work around to avoid

I: what about spending 2 cards to upgrade to dept store?

* test:
	* just assume that everyone has 2 wildcards for final round

# Playtest #54 - BGGCon

* Testing:
	* New players

Stopped game halfway to focus on comments.

I: Discarding the most customers feels bad and is against the theme.

* And can be used to attack other players
* set collection: 2/3/4-sets give bonus of 3/5/8 points at end of game

I: explanation for track is confusing. counter-intuitive to expand from either side.

I: don't like Knizia scoring - feels bad

I: possibly add waiting area on map for customers, with a foot path leading to the stations

I: Move action says "Move ... from their ward", but a single customer can be picked up and dropped off at a store in the same ward. Clarify rule description

I: would like to refer to the player aid on the shield, but can't move it because it's hiding customers.

I: can you pick up customers along the way? No

I: For card: move map to bottom, and add index in top corner. so that you can splay the cards and make them easier to see.

I: suggestion: for customers to move along at least 1 track. it fits the theme. it removes the single customer match. adds more clumps, more moves along track

N: Wanted to place track early to avoid taking an Income action

I: random - cards are limited. the outer ring is valuable - other players will trigger

N: perhaps have "marketing" action to determine where customers will go

I: lack of control over random placement of customers

I: Avoided doing 3 card as wild because the rules explanation indicated that is was an "expensive" way to get wildcards.

* In rules explanation, I said, "Only 5 cards in hand, so 3 cards is expensive"

N: pay 1 card to place 2nd track?

I: Hand in game didn't feel like an average hand.

Bigger problem: cf Carcassonne. it should eliminate 2-space cities because they are too obvious

I: Change it so that Move must use track

I: Move must end at store. Misunderstood this rule at first.

I: Don't allow moving single customers

I: didn't like being able to stop while there were still customers that could be matched.

* If adjacent to a store that matches, then you must continue
* good for network. forces more good moves.
* annoyed by stopping just before a store:
	* E.g., Food -> Book -> Clothing
	* Move customers from Food -> Book, but stop there with unresolved Clothing customer
* blocking players by rules = bad; blocking by intention = better

I: Perhaps wilds could be more useful if they matched color

I: game needs to be heavier to support 3-card wild

* the flexibility of the 3 card wild means that you move more slowly (because you're spending more cards and need to take more Income)
* Strengthen draw action, eg: draw 3 choose 1
* cards are too strict, need to loosen it up
* game is not bettern when taking Income actions

I: last 3rd of game has slow velocity

I: what is the least fun turn? how to prevent it? what is the worst possible set of cards to start with and how can that be improved?

I: get network built faster

I: for the double track description: "2 connect segments of track as long as least one touches the card played"  "city of origin"

I: Compare with Concordia

I: Terminology

* Build -> "Open" store. WRT moving stores, is that needed?
* Upgrade
* Expand -> "Lay Track"
* Move: OK. Maybe "Ride" "Commute" "Shop" - although shop is ambiguous
* Income

I: Move action

* players need to move until the reach a terminus (based on current network)
* must move until you can't move - until you have to stop
* force long travel
* play a game where you can do any valid Move

I: Perhaps start game with hand limit of 8

* keep that limit until you reach 5 stores on the map

Ralph (from Eagle Gryphon games)

* distracting Japanese text on board - overwhelming flavor text
* Sakura icon could be printed on back side of store (to indicate dept stores). But screen printing double-sided is expensive

Todo:

* update cards: put index in corner so that cards can be splayed
* update description for Move so it is clear that customers can go to stores in the same ward where they start

