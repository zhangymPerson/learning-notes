FROM golang:1.17.5-alpine3.15 as runtime

WORKDIR /goproject
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags "-X main.version=`cat VERSION`"

FROM alpine:3.15 AS run
RUN apk update && apk add --no-cache ca-certificates
COPY --from=runtime /goproject/testscprint /goproject/bin/
COPY conf /goproject/conf/

WORKDIR /goproject/bin
ENTRYPOINT ["./testscprint"]
CMD ["-c", "../conf/", "-l", "../log"]