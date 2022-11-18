import React from "react";

function Piece(props) {
  var classN;
  switch (props.value) {
    case 0:
      classN = "open-piece";
      break;
    case 1:
      classN = "player-one-piece";
      break;
    case 2:
      classN = "player-two-piece";
      break;
    case 3:
      classN = "player-one-piece-possible";
      break;
    case 4:
      classN = "player-two-piece-possible";
      break;
    default:
      throw "Value Not Handled";
  }

  classN += " piece";

  return (
    <div
      className="boarder"
      onClick={() => props.clickHandler(props.coordinates)}
    >
      <div className={classN} data-testid="piece" />
    </div>
  );
}

export default Piece;
