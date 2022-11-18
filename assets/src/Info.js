import React from "react";

const Info = (props) => {
  return (
    <div className="info-panal">
      <h5 style={{ textAlign: "center" }}>
        <b>{props.player === 1 ? "Player 1" : "PLayer 2"}</b>
      </h5>
      <p>
        <b>Turn:</b> {props.is_turn ? "Your Turn" : "Their Turn"}
      </p>
      <p>
        <b>Opponent Connected:</b> {props.opponentConnected ? "Yes" : "No"}
      </p>
    </div>
  );
};

export default Info;
