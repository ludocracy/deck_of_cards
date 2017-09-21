// 1. Make the function deck_o_cards assemble an array of cards using the provided suits and values arrays.
// Each card in the deck should be an object formatted as: {suit: 'hearts', value: 'A'}
function deck_o_cards(is_poker=false) {
  var values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'];
  var suits = ['hearts', 'diamonds', 'clubs', 'spades'];

  var cards = []; // deck
  var shuffledCards = []; // deck shuffled

  values.forEach(function (valueItem) {
    suits.forEach(function (suitItem) {
      cards.push({ value: valueItem, suit: suitItem });
    });
  });

  cards = shuffle(cards);

  let handSize = is_poker ? 5 : 1;
  let drawnCards = [];
  for (let i = 0; i < handSize; i++) {
    drawnCards.push(cards.pop());
  }

  console.log(`\nThe deck has ${cards.length} cards`);

  while(drawnCards.length !== 0) {
    let drawnCard = drawnCards.pop();
    console.log(`${is_poker ? '' : 'The top card is the '}${drawnCard.value} of ${drawnCard.suit}`);
  }
}



// Fisher-Yates Shuffle
// http://stackoverflow.com/a/6274398
function shuffle(array) {
    var counter = array.length, temp, index;

    // While there are elements in the array
    while (counter > 0) {
        // Pick a random index
        index = Math.floor(Math.random() * counter);

        // Decrease counter by 1
        counter--;

        // And swap the last element with it
        temp = array[counter];
        array[counter] = array[index];
        array[index] = temp;
    }

    return array;
}

deck_o_cards();

deck_o_cards(true);
