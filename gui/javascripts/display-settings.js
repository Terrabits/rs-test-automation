class DisplaySettings {
  constructor() {
    if (config.has('display-results')) {
      this.results = config.get('display-results');
    }
  }
  get results() {
    return $('#display-results').val();
  }
  set results(value) {
    config.set('display-results', value);
    $('#display-results').val(value);
  }
}

module.exports = DisplaySettings;
