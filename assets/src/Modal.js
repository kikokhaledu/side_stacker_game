import React from "react";

const Modal = (props) => {
  return (
    <div class="modal our-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header text-center" style={{ margin: "auto" }}>
            <h5 class="modal-title">Game Over!</h5>
          </div>
          <div class="modal-body">
            <p style={{ color: props.text.color }}>{props.text.content}</p>
          </div>
          <div class="modal-footer" style={{ margin: "auto" }}>
            <a href="/setup">
              <button
                type="button"
                class="btn btn-secondary"
                data-dismiss="modal"
              >
                Play Again
              </button>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Modal;
