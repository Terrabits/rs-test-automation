class Alert {
  set message(msg) {
    $('.alert').text(msg);
  }
  show() {
    $('.alert').removeClass('invisible');
  }
  hide() {
    $('.alert').addClass('invisible');
  }

  setTimer() {
    var callback = () => {
      this.timer = undefined;
      this.message = 'X';
      this.hide();
    };
    this.timer = setTimeout(callback, 5000);
  }
  clearTimer() {
    if (!this.timer) {
      return;
    }
    clearTimeout(this.timer);
    this.timer = false;
  }

  showMessage(msg) {
    this.clearTimer();
    this.message = msg;
    this.show();
    this.setTimer();
  }
}

module.exports = new Alert();
