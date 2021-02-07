function createCard(face, suit) {
    const valid_faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'];
    const valid_suits = ['S', 'H', 'D', 'C'];
    if (!valid_faces.includes(face) || !valid_suits.includes(suit)){
        throw new Error('Error')
    }

    const suitToString = {
        'S': '\u2660',
        'H': '\u2665',
        'D': '\u2666',
        'C': '\u2663',
    };

    return {
        face,
        suit,
        toString() {
            return `${face}${suitToString[suit]}`;
        }
    };
}

myCard = createCard('A', '100').toString();
console.log(myCard);