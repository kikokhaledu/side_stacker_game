import React from "react";
import Piece from "./Piece";

class Row extends React.Component {
  constructor() {
    super();
    this.state = {
      hovering: false,
    };
    this.OnMouseExitHandler = this.OnMouseExitHandler.bind(this);
    this.OnMouseOverHandler = this.OnMouseOverHandler.bind(this);
  }

  OnMouseOverHandler() {
    this.setState({
      hovering: true,
    });
  }

  OnMouseExitHandler() {
    this.setState({
      hovering: false,
    });
  }

  render() {
    let valueCopy = this.props.value.slice();
    if (this.state.hovering && this.props.is_turn) {
      // const indexOfEmptyPiece = valueCopy[0];
      // if (indexOfEmptyPiece !== -1) {
      //   valueCopy[indexOfEmptyPiece] = this.props.player === 1 ? 3 : 4;
      // }
      valueCopy[0] = this.props.player === 1 ? 3 : 4;
      valueCopy[6] = this.props.player === 1 ? 3 : 4;
    }

    var key = 0;
    const pieces = valueCopy.map((item, index) => {
      key += 1;
      return (
        <Piece
          coordinates={{ row: this.props.rowNum, column: key - 1 }}
          clickHandler={this.props.clickHandler}
          key={key}
          value={item}
        />
      );
    });
    return (
      <div
        data-testid="row"
        className="row"
        onMouseOver={() => this.OnMouseOverHandler()}
        onMouseOut={() => this.OnMouseExitHandler()}
      >
        {pieces}
      </div>
    );
  }
}

export default Row;
