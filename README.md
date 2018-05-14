# Collective Knowledge repository for AI

[![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-powered-by-ck.png)](https://github.com/ctuning/ck)
[![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-validated-by-the-community-simple.png)](http://cTuning.org)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## Introduction
This is an [on-going community project](http://cKnowledge.org/ai) to unify and automate AI research,
share AI artifacts as customizable and reusable components with JSON API using 
[open-source CK framework](http://github.com/ctuning/ck),
continuously [optimize and co-design the whole AI/SW/HW stack](http://cKnowledge.org/repo) 
across diverse hardware/models/data sets/libraries,
and help researchers adapt to a Cambrian AI/SW/HW explosion and technological chaos:

[![logo](http://cknowledge.org/images/ai-cloud-resize.png)](http://cKnowledge.org/ai)

You can browse reusable AI artifacts from this repository [online](http://cKnowledge.org/ai-artifacts).

Current AI artifacts are for [Caffe](https://github.com/dividiti/ck-caffe), 
[Caffe2](https://github.com/ctuning/ck-caffe2),
[TensorFlow](https://github.com/ctuning/ck-tensorflow),
[MXNet](https://github.com/ctuning/ck-mxnet)
and [CNTK](https://github.com/ctuning/ck-cntk).

See [cKnowledge.org/ai](http://cKnowledge.org/ai) and [cKnowledge.org/request](http://cKnowledge.org/request) for more details.

## Coordination of development
* [Open CK AI consortium](http://cKnowledge.org/partners.org)
* [dividiti](http://dividiti.com)
* [cTuning Foundation](http://cTuning.org)

## Minimal installation

The minimal installation requires:

* Python 2.7 or 3.3+ (limitation is mainly due to unitests)
* Git command line client.

### Linux/MacOS

You can install CK in your local user space simply as following:

```
$ git clone http://github.com/ctuning/ck ck-master
$ export PATH=$PWD/ck-master/bin:$PATH
$ export PYTHONPATH=$PWD/ck-master:$PYTHONPATH
```

You can also install CK via pip with sudo to avoid setting up environment variables yourself (skip sudo on Windows);

```
$ sudo pip install ck
```

### Windows

First you need to download and install a few dependencies from the following sites:

* Git: https://git-for-windows.github.io
* Minimal Python: https://www.python.org/downloads/windows

You can then install CK as following:
```
 $ git clone https://github.com/ctuning/ck.git ck
 $ set PATH={CURRENT PATH}\ck\bin;%PATH%
```

## Usage

Pull CK repo with all dependencies:

```
$ ck pull repo:ck-ai

$ ck ls ai-artifact

$ ck dashboard ai-artifact
```

Add new artifact description:
```
$ ck add ai-artifact:{AI alias}
```

Follow interactive instructions to add an artifact description.

Feel free to ask further questions via [CK public mailing list](http://groups.google.com/group/collective-knowledge).

## Related Publications with long term vision

```
@inproceedings{cm:29db2248aba45e59:cd11e3a188574d80,
    url = {http://arxiv.org/abs/1506.06256},
    title = {{Collective Mind, Part II: Towards Performance- and Cost-Aware Software Engineering as a Natural Science.}},
    author = {Fursin, Grigori and Memon, Abdul and Guillon, Christophe and Lokhmotov, Anton},
    booktitle = {{18th International Workshop on Compilers for Parallel Computing (CPC'15)}},
    publisher = {ArXiv},
    year = {2015},
    month = January,
    pdf = {http://arxiv.org/pdf/1506.06256v1}
}

```

## Next steps

We gradually add references about [all existing CK artifacts](http://cknowledge.org/repo/web.php?template=cknowledge&sort_by_uoa=yes&search_by_tags=tensorflow|caffe|caffe2|cntk|mxnet&aview=yes&ignore_without_alias=yes&archive_all=yes&force_limit=200&repo_list=ck-caffe,ck-tensorflow,ck-caffe2,ck-cntk,ck-mxnet,ck-mvnc) 
including their installation, usage and optimization.
The [CK AI consortium](http://cKnowledge.org/partners.html) is also working on a unification of all AI APIs 
and meta descriptions - join us!
