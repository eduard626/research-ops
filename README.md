# Research ops 

I found myself wanting to train models or run compute-heavy code on a remote server (e..g, EC2 instances). I did some work before with AWS's boto3 and bash scripting, which worked at the time but still required a good amount of manual effort to get code working, track it, etc. Here I try explore some of the resources I have found interesting.

For clarity, my needs are mainly for research code, not really deployment or production code. 

## Hydra + Ray + Docker
I found [this](https://samuelstanton.github.io/blog/deploying-research-code/) blog post which explained things briefly but comprehensively (tho I haven't try things). It looks like is quite old but the tools are still supported, so I'll give it a go.


