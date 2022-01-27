# Concurrency

- Two or more operations executing at the same time(concurrently)

## Concurrent updates to non-concurrency-safe collections can lead to unexpected behavior and data loss

# Solutions

## Caller Synchronization
- The caller is responsible for ensuring all access tot he collection is performed ina concurrency-safe manner

Practical examples:

using locking in C#