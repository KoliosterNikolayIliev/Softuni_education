function solve() {
    const canCast = function (state) {
        return {
            cast: function (spell) {
                console.log(`${state.name} cast ${spell}`);
                return state.mana--;
            }
        };
    };

    const canFight = function (state) {
        return {
            fight: function () {
                console.log(`${state.name} slashes at the foe!`);
                return state.stamina--;
            }
        };
    };

    const fighter = function (name) {
        let state = {
            name:name,
            health: 100,
            stamina: 100
        };
        return Object.assign(state, canFight(state));
    };

    const mage = function (name) {
        let state = {
            name:name,
            health: 100,
            mana: 100
        };
        return Object.assign(state, canCast(state));
    };
    return {mage: mage, fighter: fighter};
}

let create = solve();
const scorcher = create.mage("Scorcher");
scorcher.cast("fireball");
scorcher.cast("thunder");
scorcher.cast("light");

const scorcher2 = create.fighter("Scorcher 2");
scorcher2.fight();

console.log(scorcher2.stamina);
console.log(scorcher.mana);
