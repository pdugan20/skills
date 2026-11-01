# Ledger

Personal budgeting app for iOS. The `LedgerApp` target holds the SwiftUI
interface and, today, the budgeting logic under `Sources/LedgerApp/Core`.

## Build and test

Use the wrapper so toolchain caches stay inside the checkout:

```sh
script/swift build
script/swift test
```

CI runs the unit tests on an iOS simulator for every pull request. Recent
test-step durations are in `docs/ci-test-times.csv`.
