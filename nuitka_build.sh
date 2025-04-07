python -m nuitka \
	--standalone \
	--onefile \
	--windows-disable-console \
	--output-filename=nxp-uuu-qt-tool \
	--windows-icon-from-ico=src/Resources/icon/main.ico \
	--linux-icon=src/Resources/icon/main.png \
	--output-dir=dist \
	--remove-output \
	--show-progress \
	--show-memory \
	--lto=yes \
	--jobs=8 \
	--plugin-enable=pyqt6 \
	--follow-import-to=src,scripts \
	--nofollow-import-to=unittest,test \
	--python-flag=no_site \
	--python-flag=no_asserts \
	src/main.py
# --python-flag=no_warnings
