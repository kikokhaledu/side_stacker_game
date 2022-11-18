import React from "react";
import Board from "./Board";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import { is_turn } from "./game_utility.js";
import Player from "./Player";
import Info from "./Info";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Modal from "./Modal";

const game_id = document.getElementById("game_id").textContent;
const game_link = document.getElementById("game_link").textContent;
const client = new W3CWebSocket(
  "ws://" + window.location.host + "/ws/" + game_id + "/"
);

class App extends React.Component {
  constructor() {
    super();
    this.state = {};
    this.SendMove = this.SendMove.bind(this);
  }

  componentDidMount() {
    client.onopen = () => {
      toast.info("🦄 Connected!", {
        position: "bottom-right",
        autoClose: 3000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    };
    client.onmessage = (message) => {
      console.log(message.data);
      const dataFromServer = JSON.parse(message.data);
      this.setState({
        board: dataFromServer.board,
        player: parseInt(dataFromServer.player.toString()),
        opponentConnected: dataFromServer.opponentConnected,
        gameStatus: dataFromServer.game_status,
        winner: parseInt(dataFromServer.winner),
      });
    };
    client.onclose = () => {
      toast.info("Disconnected!", {
        position: "bottom-right",
        autoClose: 3000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    };
  }

  SendMove(cord) {
    console.log(cord);
    if (is_turn(this.state.board, this.state.player)) {
      if (cord.column === 0 || cord.column === 6) {
        const data = {
          row: cord.row,
          side: cord.column === 0 ? "Left" : "Right",
          player: this.state.player,
        };
        console.log(data);
        client.send(JSON.stringify(data));
      } else {
        toast("Please Click on The First Or The Last Column", {
          position: "bottom-right",
          autoClose: 1000,
          hideProgressBar: true,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "dark",
        });
      }
    } else {
      toast("Not Your Turn!", {
        position: "bottom-right",
        autoClose: 500,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  }

  render() {
    if (!this.state.board) {
      console.log("board is null");
      return <h1>waiting to connect</h1>;
    }

    return (
      <div>
        <Info
          is_turn={is_turn(this.state.board, this.state.player)}
          opponentConnected={this.state.opponentConnected}
          player={this.state.player}
        />
        <Player
          is_turn={is_turn(this.state.board, 1)}
          isPlayer1={true}
          areYouThisPlayer={1 === this.state.player}
        />
        <Board
          board={this.state.board}
          player={this.state.player}
          SendMove={this.SendMove}
        />
        <Player
          is_turn={is_turn(this.state.board, 2)}
          isPlayer1={false}
          areYouThisPlayer={2 === this.state.player}
        />
        <ToastContainer />
        {this.state.gameStatus && (
          <Modal
            text={{
              content:
                parseInt(this.state.player) == parseInt(this.state.winner)
                  ? "You Won!"
                  : parseInt(this.state.winner) == 3
                  ? "It's a Draw"
                  : "You Lost!",
              color:
                parseInt(this.state.player) == parseInt(this.state.winner)
                  ? "green"
                  : parseInt(this.state.winner) == 3
                  ? "orange"
                  : "red",
            }}
          />
        )}
      </div>
    );
  }
}

export default App;
