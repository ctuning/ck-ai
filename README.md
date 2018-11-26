# Collective Knowledge repository for unified AI components and workflows

[![compatibility](https://github.com/ctuning/ck-guide-images/blob/master/ck-compatible.svg)](https://github.com/ctuning/ck)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# Introduction
This is a [Collective Knowledge](http://cKnowledge.org) repository to unify and share 
AI workflows (code, data sets and models) as portable, customizable and reusable components 
with a common Python API and JSON meta-information.
Such workflows help to continuously optimize and co-design 
the whole SW/HW stack for AI/ML workloads across diverse platforms, frameworks, libraries, 
models and data sets (see [ACM ReQuEST tournaments](http://cKnowledge.org/request),
[MLPerf benchmark](http://mlperf.org) and the [public CK repository with crowdsourced expeirments](http://cKnowledge.org/repo))
while helping researchers and developers to adapt to technological chaos:

[![logo](http://cknowledge.org/images/ai-cloud-resize.png)](http://cKnowledge.org/ai)

You can browse reusable AI artifacts from this repository [online](http://cKnowledge.org/ai-artifacts).

CK supports the following AI frameworks: 
[TensorFlow](https://github.com/ctuning/ck-tensorflow),
[MXNet](https://github.com/ctuning/ck-mxnet),
[PyTorch](https://github.com/ctuning/ck-pytorch) 
[Caffe](https://github.com/dividiti/ck-caffe), 
[Caffe2](https://github.com/ctuning/ck-caffe2),
and [CNTK](https://github.com/ctuning/ck-cntk).



# Coordination of development
* [CK consortium](http://cKnowledge.org/partners.html)
* [ReQuEST consortium](http://cKnowledge.org/request.html)
* [cTuning Foundation](http://cTuning.org)
* [dividiti](http://dividiti.com)




# Installing and customizing CK

First you need to install Collective Knowledge framework (CK) as described 
[here](https://github.com/ctuning/ck#Installation). 

If you have never used CK, we also suggest you to check this
[CK getting started guide](https://github.com/ctuning/ck/wiki/First-Steps).

You may also want to check how to [customize your CK installation](https://github.com/ctuning/ck/wiki/Customization).
For example, you can force CK to install all packages (code, data sets and models) to your scratch file system 
instead of the default ${HOME}/CK-TOOLS by specifying the path using environment variable "CK_TOOLS"! 
You can also specify where to install all CK repositories instead of the default ${HOME}/CK 
using environment variable "CK_REPOS".




*Note that [CK](https://github.com/ctuning/ck/wiki) 
is a continuously evolving community project similar to Wikipedia,
so if you don't like something or something is not working, 
please do not hesitate to send your feedback
to the [public mailing list](https://groups.google.com/forum/#!forum/collective-knowledge),
open tickets in related [CK GitHub repositories](http://cKnowledge.org/shared-repos.html),
or even contribute patches, updates, new workflows and research components!*





# Installing and using this repository

You can pull this CK repo with all dependencies as follows:

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






# Related Publications 
See [CK publications](https://github.com/ctuning/ck/wiki/Publications).

## Next steps

We are gradually adding references about [all existing AI artifacts](http://cknowledge.org/repo/web.php?template=cknowledge&sort_by_uoa=yes&search_by_tags=tensorflow|caffe|caffe2|cntk|mxnet&aview=yes&ignore_without_alias=yes&archive_all=yes&force_limit=200&repo_list=ck-caffe,ck-tensorflow,ck-caffe2,ck-cntk,ck-pytorch,ck-mxnet,ck-mvnc) 
in the CK format including their installation, usage and optimization.
The [CK consortium](http://cKnowledge.org/partners.html) and [MLPerf](http://mlperf.org) are also working on a unification of all AI APIs and meta descriptions!

