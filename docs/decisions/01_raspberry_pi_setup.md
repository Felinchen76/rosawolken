# ADR 001: Raspberry Pi as initial server

## Context

The application is intended for a family with
approximately two concurrent users.

Existing hardware includes a Raspberry Pi 4
and a 2 TB HDD for now.

## Decision

Use the Raspberry Pi as the initial server.

## Alternatives

- External VPS
- NAS
- Cloud storage

## Reasoning

The expected workload is low and existing hardware
is sufficient for the prototype.

## Consequences

+ No additional hardware cost
+ Full control
+ Good learning opportunity

- Single point of failure
- Limited hardware resources
- Backup must be handled separately