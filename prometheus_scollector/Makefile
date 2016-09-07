VERSION=0.1.0
PWD=$(shell pwd)
EL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3}')
FULL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3 "." $$4}')
RPM_NAME=prometheus_scollector-$(VERSION)-1.$(FULL_VERSION).x86_64.rpm
RPM_FILE=$(PWD)/rpmbuild/RPMS/x86_64/$(RPM_NAME)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/go"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	export GOPATH="$(PWD)/rpmbuild/go" && /usr/bin/go get github.com/gitinsky-bot/prometheus_scollector
	cp "$(PWD)/rpmbuild/go/bin/prometheus_scollector" contrib
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/prometheus_scollector-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz prometheus_scollector-$(VERSION).linux-amd64.tar.gz prometheus_scollector-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/prometheus_scollector-$(EL_VERSION).spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus_scollector -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/prometheus_scollector/rpmbuild/RPMS/x86_64/prometheus_scollector-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

deploy-bintray: rpm
	curl -T $(RPM_FILE) -u$(CREDENTIALS) https://api.bintray.com/content/$(REPOSITORY)/prometheus_scollector/$(VERSION)/$(RPM_NAME)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus_scollector*"
