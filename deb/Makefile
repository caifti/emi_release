PACKAGE = emi-release
NAME = emi-release
VERSION = 3.0.0
RELEASE = 2

####################################################################
# Distribution Makefile
####################################################################

.PHONY: configure install clean rpm

all: configure

####################################################################
# Install
####################################################################

install:
	@echo installing ...
	@mkdir -p $(prefix)/etc
	@mkdir -p $(prefix)/etc/apt
	@mkdir -p $(prefix)/etc/apt/sources.list.d
	@mkdir -p $(prefix)/etc/apt/preferences.d
	@install -m 0644 etc/emi-release $(prefix)/etc
	@install -m 0644 etc/apt/sources.list.d/emi3.list $(prefix)/etc/apt/sources.list.d
	@install -m 0644 etc/apt/preferences.d/emi3 $(prefix)/etc/apt/preferences.d

###########################################################$(DESTDIR)#########
# Build Distribution
####################################################################

rpm:
	@echo "> Creating rpm..."
	@mkdir -p  rpmbuild/RPMS/noarch
	@mkdir -p  rpmbuild/SRPMS/
	@mkdir -p  rpmbuild/SPECS/
	@mkdir -p  rpmbuild/SOURCES/
	@mkdir -p  rpmbuild/BUILD/
	@tar --gzip --exclude='*svn*' -cf rpmbuild/SOURCES/${PACKAGE}.src.tgz *
	@sed -e s/VV/$(VERSION)/ -e s/NNAME/$(NAME)/ -e s/RR/$(RELEASE)/ emi-release.spec > specfile_tmp.spec
	@rpmbuild -ba specfile_tmp.spec
	@rm -f specfile_tmp.spec

clean:
	@echo "> Cleaning..."
	@rm -rf rpmbuild
