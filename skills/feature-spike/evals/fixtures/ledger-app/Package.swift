// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "Ledger",
    platforms: [.macOS(.v14), .iOS(.v17)],
    targets: [
        .executableTarget(name: "LedgerApp", path: "Sources/LedgerApp"),
        .testTarget(name: "LedgerAppTests", dependencies: ["LedgerApp"], path: "Tests/LedgerAppTests"),
    ]
)
