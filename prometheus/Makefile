VERSION=1.0.1
PWD=$(shell pwd)
EL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3}')
FULL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3 "." $$4}')
RPM_NAME=prometheus-$(VERSION)-1.$(FULL_VERSION).x86_64.rpm
RPM_FILE=$(PWD)/rpmbuild/RPMS/x86_64/$(RPM_NAME)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/prometheus/releases/download/v$(VERSION)/prometheus-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf prometheus-$(VERSION).linux-amd64.tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz prometheus-$(VERSION).linux-amd64.tar.gz prometheus-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/prometheus-$(EL_VERSION).spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus -F v=$(VERSION) -F p=RPM -F file=@$(RPM_EL7) -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

deploy-bintray: rpm
	curl -T $(RPM_FILE) -u$(CREDENTIALS) https://api.bintray.com/content/$(REPOSITORY)/prometheus/$(VERSION)/$(RPM_NAME)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus*"

