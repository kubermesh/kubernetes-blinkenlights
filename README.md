# kubernetes-blinkenlights

![Docker Automated build](https://img.shields.io/docker/automated/kubermesh/kubernetes-blinkenlights.svg)

[Blinkenlights](https://en.wikipedia.org/wiki/Blinkenlights) for a kubernetes cluster!

## Installation

`kubectl apply -f https://github.com/kubermesh/kubermesh/blob/master/manifests/blinkenlights-daemonset.yaml`

## Hardware

Uses the [blink(1)](https://blink1.thingm.com/) USB Light

## What do the lights mean?

- white flash: start of the sequence
- green flash: a pod that's running
- red flash: a pod that's not running
