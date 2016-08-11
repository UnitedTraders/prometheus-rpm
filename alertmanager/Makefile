VERSION=0.3.0
PWD=$(shell pwd)
EL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3}')
FULL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3 "." $$4}')
RPM_NAME=alertmanager-$(VERSION)-1.$(FULL_VERSION).x86_64.rpm
RPM_FILE=$(PWD)/rpmbuild/RPMS/x86_64/$(RPM_NAME)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/alertmanager/releases/download/v$(VERSION)/alertmanager-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf alertmanager-$(VERSION).linux-amd64.tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz alertmanager-$(VERSION).linux-amd64.tar.gz alertmanager-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/alertmanager-$(EL_VERSION).spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=alertmanager -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/alertmanager/rpmbuild/RPMS/x86_64/alertmanager-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

deploy-bintray: rpm
	curl -T $(RPM_FILE) -u$(CREDENTIALS) https://api.bintray.com/content/$(REPOSITORY)/alertmanager/$(VERSION)/$(RPM_NAME)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/alertmanager*"
