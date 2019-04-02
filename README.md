# Word search engine
[![Build Status](https://travis-ci.com/jorgechato/word-search-engine.svg?token=x3vLcsQVEzf1kfJyx1Uv&branch=master)](https://travis-ci.com/jorgechato/word-search-engine)
[![Docker](https://img.shields.io/badge/docker-image-blue.svg)](https://hub.docker.com/r/jorgechato/word-search-engine)

Input:

- Query to search for (a word).
- Source where to search (webpage).

Output:

- Number of times the word exists in the html source.

Constrains:

- Count only the giving word, not another word containing.

## Architecture

TODO: architecture

## API

Base API contract is stored in the [doc](/doc/contract.json) folder.
You can see the UI in http://\<ENDPOINT\>:\<PORT\>/ and the live documentation in
http://\<ENDPOINT\>:\<PORT\>/swagger.json tho.

## Run

```bash
$ FLASK_APP=src/app flask run
# or
$ python src/app.py
```

```bash
$ curl -X PUT http://<ENDPOINT>:<PORT>/search \
      -H 'content-type: application/json' \
      -d @'base.template.json'
```

## Deploy

The deployment is automated by the CI/CD pipeline but you can always run it in
your local machine.

```bash
# Build docker
$ docker build -t word-search-engine:latest .
$ docker run -p 8000:8000 -e PORT=8000 --name word-search-engine word-search-engine:latest
```

Pull the latest version from [hub.docker](https://hub.docker.com/r/jorgechato/word-search-engine) from any machine with docker installed on it.
You can automate the process with Terraform, and a CI/CD pipeline if you are
using ECS or create a deploy/rollback in K8s

```bash
$ docker pull jorgechato/word-search-engine:latest
# example with k8s
# do not forget to export the ENV_VARIABLES for the DB connection first
$ kubectl apply -f deploy/k8s.yml
```

---

## Requirements

### Must have

- [python 3.x](https://www.python.org/downloads/)
- pip3

### Recommendation for development

- [anaconda](https://anaconda.org/anaconda/python)

#### Install dependencies

```bash
# with anaconda
$ conda env create -f environment.yml # create virtual environment
$ conda activate backend # enter VE
# or
$ source activate backend
(backend) $ conda deactivate # exit VE
```

---

## FAQ

**Can the word be part of any html tag, css or js embedded in the source code of
the page?**

See also:

* [business] MVP Questions ([#1][i1])

**Does the scrapping search take place in the hole site-map of the domain?**

No, the search engine only search in the endpoint provided by the requester.

**Why K8S and not AWS lambdas?**

**P 1**: When using Serverless platforms the first invocation of a function takes
some time since the code needs to be initialized. In this case we will need a fast
response since this service will be integrated with a stack of MS.

**P 2**: Kubernetes might provide better scalability features than some Serverless
platforms, since Kubernetes is more mature and provides even HA (high availability)
between different zones which not all Serverless platforms provide yet.
And we plan to expand our business to different zones.


**P 3**: it might be easier to use Kubernetes for more complex applications because
the platform is more mature. And since we are planning to use a database to
store the outcome of the logic, that make sense.


**P 4**: Serverless doesn’t automatically mean lower costs, like when your
applications need to run 24/7. There can also be some hidden costs like extra
costs for API management or the costs for the function invocations for tests.

**P 5**: The monitoring capabilities of Kubernetes applications are much more
mature.


[i1]: https://github.com/jorgechato/word-search-engine/issues/1
