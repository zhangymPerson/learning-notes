# init project path
WORKROOT := $(shell pwd)
OUTDIR   := $(WORKROOT)/output

# init environment variables
export PATH        := $(shell go env GOPATH)/bin:$(PATH)
export GO111MODULE := on

# project name
PROJECT_NAME=test_script

# init command params
GO           := go
GOBUILD      := $(GO) build
GOTEST       := $(GO) test
GOVET        := $(GO) vet
GOGET        := $(GO) get
GOGEN        := $(GO) generate
GOCLEAN      := $(GO) clean
GOINSTALL    := $(GO) install
GOFLAGS      := -race
STATICCHECK  := staticcheck
PIP          := pip3
PIPINSTALL   := $(PIP) install

# init arch
ARCH := $(shell getconf LONG_BIT)
ifeq ($(ARCH),64)
	GOTEST += $(GOFLAGS)
endif

# init project version
PROJECT_VERSION ?= $(shell cat VERSION)
# init git commit id
GIT_COMMIT ?= $(shell git rev-parse HEAD)

# init project packages
PROJECT_PKGS := $(shell go list ./...)

# go install package
# $(1) package name
# $(2) package address
define INSTALL_PKG
	@echo installing $(1)
	$(GOINSTALL) $(2)
	@echo $(1) installed
endef

define PIP_INSTALL_PKG
	@echo installing $(1)
	$(PIPINSTALL) $(1)
	@echo $(1) installed
endef

# make compile, go build
compile: test build
build:
	$(GOBUILD) -o $(PROJECT_NAME) -ldflags "-X main.version=$(PROJECT_VERSION) -X main.commit=$(GIT_COMMIT) -extldflags=-static"

# make compile-strip, go build without symbols and DWARFs
compile-strip: test build-strip
build-strip:
	$(GOBUILD) -o $(PROJECT_NAME) -ldflags "-X main.version=$(PROJECT_VERSION) -X main.commit=$(GIT_COMMIT) -extldflags=-static -s -w"

# make test, test your code
test: test-case vet-case
test-case:
	$(GOTEST) -cover ./...
vet-case:
	${GOVET} ./...

# make coverage for codecov
coverage:
	echo -n > coverage.txt
	for pkg in $(PROJECT_PKGS) ; do $(GOTEST) -coverprofile=profile.out -covermode=atomic $${pkg} && cat profile.out >> coverage.txt; done

# make package
package:build
	mkdir -p $(OUTDIR)/bin
	mv $(PROJECT_NAME)  $(OUTDIR)/bin
	cp -r conf $(OUTDIR)


# make docker
docker:
	docker build \
		-t $(PROJECT_VERSION):$(PROJECT_VERSION) \
		-f Dockerfile \
		.

# make clean
clean:
	$(GOCLEAN)
	rm -rf $(OUTDIR)
	rm -rf $(WORKROOT)/$(PROJECT_NAME)

# avoid filename conflict and speed up build 
.PHONY: all compile test package clean build