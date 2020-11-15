# Kind

Run local Kubernetes clusters using Docker container "nodes".

## Setup

Make sure you have [Go](https://golang.org/doc/install) installed then run the following:

```bash
GO111MODULE="on" go get sigs.k8s.io/kind@v0.9.0
kind create cluster
```
