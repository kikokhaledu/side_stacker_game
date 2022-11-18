export function is_turn(board, player) {
  //TODO No your turn if game is over
  let arrayOfSum = board.map((arr) => arr.reduce(countNonZeros, 0)); //0 makes it start at 0
  let sum = arrayOfSum.reduce(sumReducer);
  return sum % 2 == player - 1;
}

const countNonZeros = (accumulator, currentValue) =>
  accumulator + (currentValue == 0 ? 0 : 1);
const sumReducer = (accumulator, currentValue) => accumulator + currentValue;
