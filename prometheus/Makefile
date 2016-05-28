VERSION=0.19.1
PWD=$(shell pwd)

all: rpm clean

rpm-el6:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/prometheus/releases/download/$(VERSION)/prometheus-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz prometheus-$(VERSION).linux-amd64.tar.gz prometheus-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/prometheus-el6.spec

rpm-el7:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/prometheus/releases/download/$(VERSION)/prometheus-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz prometheus-$(VERSION).linux-amd64.tar.gz prometheus-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/prometheus-el7.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/prometheus/rpmbuild/RPMS/x86_64/prometheus-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION)"
	rm "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64.tar.gz"
