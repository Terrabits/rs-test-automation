var del   = require('del');
var gulp  = require('gulp');
var shell = require('gulp-shell')


gulp.task('default', ['restart'], function() {
  // place code for your default task here
});
gulp.task('clean-mm', function() {
	return del([
		'app/**/*',
	    '!app/rstest'
    ]);
});
gulp.task('clean-py', function() {
	return del([
	    'app/rstest'
    ]);
});
gulp.task('clean', ['clean-mm', 'clean-py'], function() {
	return del([
	    'app/**/*'
    ]);
});
gulp.task('build-py',
	shell.task(['pyinstaller run.spec --distpath=\"app\"'])
);
gulp.task('build-mm',
	shell.task(['bundle exec middleman build --no-clean'])
);
gulp.task('build', ['build-py', 'build-mm'], function() {

});
gulp.task('rebuild-py', ['clean-py'],
	shell.task(['pyinstaller run.spec --distpath=\"app\"'])
);
gulp.task('rebuild-mm', ['clean-mm'],
	shell.task(['bundle exec middleman build --no-clean'])
);
gulp.task('rebuild', ['rebuild-py', 'rebuild-mm'], function() {

});
gulp.task('restart', ['rebuild'],
	shell.task(['npm start'])
);
gulp.task('repack', ['rebuild'],
	shell.task(['npm pack'])
);
gulp.task('redist', ['rebuild'],
	shell.task(['npm dist'])
);