# Swift and Apple projects

Choose the project source of truth before adding tooling.

## Scaffold

- Use an Xcode project for an iOS, macOS, watchOS, or visionOS application. Use
  Swift Package Manager for libraries, command-line tools, and package-owned
  logic; do not substitute an executable Swift package for an iOS app.
- Use Xcode's generated project or a maintained generator such as XcodeGen when
  reproducibility warrants it. If XcodeGen owns structure, commit `project.yml`,
  document regeneration, and decide explicitly whether the generated project
  is committed for contributors without XcodeGen.
- Resolve the platform and deployment target from product intent and supported
  devices. Do not default every prototype to either the oldest possible target
  or the newest SDK-only target.
- Leave the development team, distribution identity, entitlements, bundle
  identifier, and store metadata unresolved until the owner supplies them.

## Local contract

- Record the required Xcode and Swift versions when compatibility matters.
- Keep the placeholder app minimal and use one shared scheme.
- Add SwiftFormat or SwiftLint only with checked-in configuration and a local
  install/bootstrap path. A tool that is not reproducible is not a gate.
- Add focused tests when the scaffold contains logic. A UI shell may use a
  signing-disabled simulator build as its exploration verification.
- For maintained apps, expose one command that runs format, lint, tests, and a
  representative `xcodebuild`. Keep Derived Data in a disposable path in CI.

## Automation

Use a macOS runner only for jobs that need Apple tooling. Configure Swift
Package dependency updates for the actual project or package directory. Add
signing, TestFlight, notarization, archives, and release jobs only for a
shipping profile with an explicit credential and environment design.

Never copy self-hosted runners, test-count baselines, signing scripts, or
TestFlight machinery from a larger app merely because it is another Swift
repository.
