web: gunicorn tpobot.wsgi
celery: env > .env; env GEM_HOME=$HOME/.ruby-gems env PATH=$PATH:$HOME/.ruby-gems/bin foreman start -f celeryProcfile
