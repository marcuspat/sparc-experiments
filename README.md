# SPARC Experiments

Personal exploration of SPARC and multi-agent frameworks in the context of DevOps automation and platform workflows.

## Goals

- Understand how SPARC-style agent stacks interact with system state
- Test agent loops that reason about infrastructure
- Explore prompting patterns for platform engineering tasks

## Tools

- LangGraph / AutoGen / CrewAI
- Prompt orchestration
- Notebook-based experimentation

## Status

Still in whiteboard + console mode. Notes and tests incoming.

## Try It Out

This repo includes a simple simulation of an agent loop that watches pod health and reacts to issues.

**`pod_watchdog.py`**

```bash
python pod_watchdog.py
```

This script simulates:

- Observing pod states (e.g., from `kubectl get pods`)
- Reasoning about errors like `CrashLoopBackOff`
- Printing a recommended action

📦 Currently uses mock data — ready to evolve into live `kubectl` parsing with `subprocess` or a K8s client.
