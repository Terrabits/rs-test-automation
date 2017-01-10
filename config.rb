# Pages with no layout
page '/*.xml',        layout: false
page '/*.json',       layout: false
page '/*.txt',        layout: false

# General configuration
activate :sprockets
activate :pry

# Settings
set :source,        'gui'
set :build_dir,     'app'
set :relative_links, true

# Build-specific configuration
configure :build do
  # activate :minify_html
  # activate :minify_css
  # activate :minify_javascript
end
