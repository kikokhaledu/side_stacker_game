import React from "react";
import Row from "./Row";
import { is_turn } from "./game_utility";

function Board(props) {
  let counter = -1;
  const columns = props.board.map((col) => {
    counter += 1;
    return (
      <Row
        player={props.player}
        is_turn={is_turn(props.board, props.player)}
        value={col}
        key={counter}
        rowNum={counter}
        clickHandler={props.SendMove}
      />
    );
  });
  return (
    <div className="board" data-testid="game">
      {columns}
    </div>
  );
}

export default Board;
