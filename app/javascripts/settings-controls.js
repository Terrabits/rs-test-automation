
class SettingsControls {
  open() {
    $('#settings-drawer').drawer('show');
  }
  close() {
    $('#settings-drawer').drawer('hide');
  }
  disable() {
    $('#settings-cog').prop('disabled', true);
    $('#save-dir-button').prop('disabled', true);
    $('#select-all').prop('disabled', true);
    $('#global-limit').prop('disabled', true);
    $('#snp-files').prop('disabled', true);
    $('#csv-files').prop('disabled', true);
    $('#screenshots').prop('disabled', true);
    $('#per-test-limits').prop('disabled', true);
    $('#markers').prop('disabled', true);
    $('#html-summary').prop('disabled', true);
    $('#results-json').prop('disabled', true);
    $('#organize-by-file').prop('disabled', true);
    $('#project-csv').prop('disabled', true);
  }
  enable() {
    $('#settings-cog').prop('disabled', false);
    $('#save-dir-button').removeAttr('disabled');
    $('#select-all').removeAttr('disabled');
    $('#global-limit').removeAttr('disabled');
    $('#snp-files').removeAttr('disabled');
    $('#csv-files').removeAttr('disabled');
    $('#screenshots').removeAttr('disabled');
    $('#per-test-limits').removeAttr('disabled');
    $('#markers').removeAttr('disabled');
    $('#html-summary').removeAttr('disabled');
    $('#results-json').removeAttr('disabled');
    $('#organize-by-file').removeAttr('disabled');
    $('#project-csv').removeAttr('disabled');
  }
}

module.exports = new SettingsControls();
