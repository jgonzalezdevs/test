interprete = @python3 manage.py

install:
	@pip3 install --upgrade pip
	@pip3 install -r beco/requirements.pip

migrations:
	$(interprete) makemigrations
	$(interprete) migrate

reset_db:
	$(interprete) flush --noinput

defaults:
	$(interprete) shell < management/defaults/users.py
	$(interprete) shell < management/defaults/permissions.py

seeder:
	$(interprete) shell < management/seeders/users.py

feeddb: defaults seeder
