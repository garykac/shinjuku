# Shinjuku

Shinjuku is a board game where you build department stores in Tokyo and the rail lines so that
customers can get to your stores.

**Note: This game is a work in progress**

## Background

If you've ever been to Tokyo, you've probably noticed (at least) two things about the rail transit:

* The train lines are not all owned by the same company, so a "rail pass" that works on all rail in the city doesn't exist 
* Many lines have names that match large department stores (e.g., Keio, Odakyu, Tokyu)

Many train operators in Tokyo are actually conglomerates that own large department stores and the train lines
to get customers to their stores.

In this game, you are playing the part of those conglomerates.

## The Map

The map contains train stations where you can build your stores.

Each station has a set of potential connections to other stations and a maximum build height for stores (1, 2, or 3 dots).

![](tokyo-map.png)

## The Cards

There are 23 different cards – one for each ward (区 or _ku_) in Tokyo.
There are multiple copies of each card based on the population of that ward.

![](images/shinjuku.png)

## How to Play

### Setup

For each player:

* Draw 3 cards into your hand
* Place 2 customers on the board (see below on how to do that)
* Place one of your stores (any kind) onto any empty station.

### Gameplay

During your turn, you can any of the following actions twice:

* Play a card from your hand and then:
  * Build a store at any empty station in that ward.
  * Upgrade a store that you have in that ward.
  * Lure customers from that ward to stores, following train tracks to connected stations.
* Build new track that connects to one of your stores or to your existing track. 
* Discard and draw new cards into your hand.

After taking your 2 actions:

* Place 1 customer on the board as a signal to the next player that they can take their turn
* Draw back up to 3 cards (if needed)

## Customers

### Placing Customers

New customers are added randomly to the board each turn. To do this:

* Draw a card to determine the location of the customer
* Draw a customer token to determine what the customer is looking for
* Place the customer token in the ward that matches the card

Note that the customer is located in the ward, not in any particular station.
Customers do not choose a station until they are being lured.

### Luring Customers

When you choose the action to "lure" customers to your store, do the following:

1. Gather *all* of the customers in the ward that matches the card played
2. Select their starting station within that ward
3. Satisfy customers that match the shops in that station
   * A single shop can satisfy a single customer that matches the shop type
   * A double shop can satisfy two customers that match the shop type
   * A department store can satisfy three customers that match any 3 different shop types.
4. Optionally, move all unsatisfied customers to another connected station and then repeat steps 3 & 4.

If there are no customers that match the store, then they can just pass that station by and continue to the next station.
But if a customer matches the shop, you *must* satisfy them with that store if possible.

In addition, you *must* end your train journey on a station with a store that satisfies at least one customer.

Any remaining unsatisfied customers are moved into the ward that contains the final station.

## Wildcards

Once you build a station in a ward, the cards for that ward become wildcards for you.
You can use your wildcards to match any ward.

Because the card frequency varies based on the population of that ward, some cards work better
as wildcards (because you're more likely to encounter them).

## Playtest images

* https://twitter.com/hackerblinks/status/1032744357642657792
