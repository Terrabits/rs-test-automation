const fullResults   = window.nodeRequire(path.resolve(root_path, 'full-results'));
const simpleResults = window.nodeRequire(path.resolve(root_path, 'simple-results'));

class Results {
  show(display) {
    display = display.toLowerCase();
    if (display == "simple") {
      fullResults.hide();
      simpleResults.show();
    }
    else {
      simpleResults.hide();
      fullResults.show();
    }
    $('div#results').removeClass('hide');
  }
  hide() {
    fullResults.hide();
    simpleResults.hide();
    $('div#results').addClass('hide');
  }
  update(settings, data) {
    simpleResults.add(settings.serialNo, data);
    fullResults.url = settings.summarUrl();
  }
}
module.exports = new Results();
