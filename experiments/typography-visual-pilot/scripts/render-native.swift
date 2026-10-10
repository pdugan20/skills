import AppKit
import SwiftUI
import Foundation

// Standalone macOS canvas. Compile with:
// swiftc -parse-as-library scripts/render-native.swift -o /tmp/typography-native
// /tmp/typography-native /absolute/path/to/experiments/typography-visual-pilot
struct Role: Decodable {
    let font: String
    let size: Double
    let weight: Double
    let leading: Double
    let tracking: Double

    var nativeFont: NSFont {
        let weights: [(Double, NSFont.Weight)] = [(100, .ultraLight), (200, .thin), (300, .light), (400, .regular), (500, .medium), (600, .semibold), (700, .bold), (800, .heavy), (900, .black)]
        let weight = weights.min(by: { abs($0.0 - self.weight) < abs($1.0 - self.weight) })!.1
        let base = NSFont.systemFont(ofSize: size, weight: weight)
        switch font {
        case "system": return base
        case "serif": return NSFont(descriptor: base.fontDescriptor.withDesign(.serif)!, size: size)!
        case "rounded": return NSFont(descriptor: base.fontDescriptor.withDesign(.rounded)!, size: size)!
        case "Georgia":
            // Georgia has regular/bold masters, not nine static weights.
            return NSFont(name: self.weight >= 600 ? "Georgia-Bold" : "Georgia", size: size)!
        default: fatalError("Unsupported native font: \(font)")
        }
    }
}

struct Spaces: Decodable {
    let titleAfter: Double
    let deckAfter: Double
    let sectionBefore: Double
    let rowGap: Double
    let paragraphAfter: Double
}
struct Treatment: Decodable {
    let roles: [String: Role]
    let space: Spaces
    let titleBreak: String
}

enum Palette {
    static func color(_ hex: UInt32) -> Color {
        Color(red: Double((hex >> 16) & 255) / 255, green: Double((hex >> 8) & 255) / 255, blue: Double(hex & 255) / 255)
    }
    static let paper = color(0xF6F3EB)
    static let ink = color(0x262A27)
    static let muted = color(0x626960)
    static let rule = color(0xCFCFC3)
    static let accent = color(0x52604E)
}

// TextKit determines wrapping using the same NSFont and em-to-point tracking
// as the SwiftUI Text output. It does not draw any pixels.
func wrappedLines(_ text: String, role: Role, width: CGFloat) -> [String] {
    let storage = NSTextStorage(string: text, attributes: [.font: role.nativeFont, .kern: role.tracking * role.size])
    let manager = NSLayoutManager()
    let container = NSTextContainer(size: NSSize(width: width, height: 100_000))
    container.lineFragmentPadding = 0
    container.lineBreakMode = .byWordWrapping
    manager.addTextContainer(container)
    storage.addLayoutManager(manager)
    manager.ensureLayout(for: container)
    var lines: [String] = []
    manager.enumerateLineFragments(forGlyphRange: manager.glyphRange(for: container)) { _, _, _, glyphRange, _ in
        let range = manager.characterRange(forGlyphRange: glyphRange, actualGlyphRange: nil)
        let line = (text as NSString).substring(with: range).trimmingCharacters(in: .whitespacesAndNewlines)
        if !line.isEmpty { lines.append(line) }
    }
    func normalized(_ value: String) -> String { value.split(whereSeparator: { $0.isWhitespace }).joined(separator: " ") }
    precondition(normalized(lines.joined(separator: " ")) == normalized(text), "TextKit wrapping changed or dropped copy")
    return lines
}

// SwiftUI's measured native first baseline, rather than a CSS line-height
// assumption, anchors each line. Baseline-to-baseline distance is size*leading.
// This supports tighter-than-natural leading without clamping or shrinking.
struct BaselineLines: Layout {
    let distance: CGFloat
    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        guard let first = subviews.first else { return .zero }
        let firstBaseline = first.dimensions(in: .unspecified)[.firstTextBaseline]
        var width: CGFloat = 0
        var height: CGFloat = 0
        for (index, view) in subviews.enumerated() {
            let dim = view.dimensions(in: .unspecified)
            width = max(width, dim.width)
            height = max(height, firstBaseline + CGFloat(index) * distance - dim[.firstTextBaseline] + dim.height)
        }
        return CGSize(width: width, height: height)
    }
    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        guard let first = subviews.first else { return }
        let firstBaseline = first.dimensions(in: .unspecified)[.firstTextBaseline]
        for (index, view) in subviews.enumerated() {
            let dim = view.dimensions(in: .unspecified)
            view.place(at: CGPoint(x: bounds.minX, y: bounds.minY + firstBaseline + CGFloat(index) * distance - dim[.firstTextBaseline]), anchor: .topLeading, proposal: .unspecified)
        }
    }
}

struct RoleText: View {
    let text: String
    let role: Role
    var width: CGFloat = 374
    var color: Color = Palette.ink
    var body: some View {
        let lines = wrappedLines(text, role: role, width: width)
        BaselineLines(distance: role.size * role.leading) {
            ForEach(Array(lines.enumerated()), id: \.offset) { _, line in
                Text(verbatim: line)
                    .font(Font(role.nativeFont))
                    .tracking(role.tracking * role.size)
                    .foregroundStyle(color)
                    .fixedSize(horizontal: true, vertical: true)
            }
        }
    }
}

struct Block {
    let id: String
    let text: String
    let role: String
    let gapBefore: CGFloat
    var muted = false
}

final class Measurements {
    var frames: [[String: Any]] = []
    var issues: [String] = []
}

struct ArticleLayout: Layout {
    let blocks: [Block]
    let measurements: Measurements
    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        var height: CGFloat = 0
        for (index, view) in subviews.enumerated() {
            height += blocks[index].gapBefore + view.sizeThatFits(.unspecified).height
        }
        return CGSize(width: 374, height: height)
    }
    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        var y = bounds.minY
        measurements.frames = []
        measurements.issues = []
        for (index, view) in subviews.enumerated() {
            let block = blocks[index]
            let size = view.sizeThatFits(.unspecified)
            y += block.gapBefore
            view.place(at: CGPoint(x: bounds.minX, y: y), anchor: .topLeading, proposal: .unspecified)
            measurements.frames.append(["id": block.id, "x": Double(bounds.minX), "y": Double(y), "width": Double(size.width), "height": Double(size.height), "bottom": Double(y + size.height)])
            if size.width > 374.5 { measurements.issues.append("\(block.id): horizontal overflow \(size.width - 374)pt") }
            y += size.height
        }
        if y > 748 { measurements.issues.append("Article bottom \(y)pt crosses footer clearance boundary 748pt") }
        if y > 850 { measurements.issues.append("Article bottom \(y)pt exceeds canvas height 850pt") }
    }
}

struct NativeCanvas: View {
    let treatment: Treatment
    let measurements: Measurements
    var blocks: [Block] {
        let s = treatment.space
        return [
            Block(id: "eyebrow", text: "ESSAY · 8 MIN READ", role: "eyebrow", gapBefore: 0, muted: true),
            Block(id: "title", text: treatment.titleBreak == "after-art" ? "The art of\npaying attention" : "The art of paying attention", role: "title", gapBefore: 14),
            Block(id: "deck", text: "A walk without a destination can change the shape of a day.", role: "deck", gapBefore: s.titleAfter, muted: true),
            Block(id: "author", text: "By Nora Ellis", role: "meta", gapBefore: s.deckAfter),
            Block(id: "date", text: "October 10, 2026", role: "meta", gapBefore: 4, muted: true),
            Block(id: "section", text: "Opening note", role: "section", gapBefore: s.sectionBefore),
            Block(id: "paragraph-1", text: "We had walked this street a hundred times. That morning, with no appointment ahead of us, it seemed to contain an entirely different city.", role: "body", gapBefore: s.rowGap),
            Block(id: "paragraph-2", text: "There was a seam of light beneath the bookshop door, a pear tree leaning over a wall, the sound of someone practising a difficult piece of music. Nothing had changed. We had simply begun to notice.", role: "body", gapBefore: s.paragraphAfter)
        ]
    }
    var body: some View {
        ZStack(alignment: .topLeading) {
            Palette.paper
            HStack(alignment: .firstTextBaseline, spacing: 12) {
                RoleText(text: "Field Notes", role: treatment.roles["brand"]!, width: 210)
                Spacer(minLength: 12)
                RoleText(text: "Saved story", role: treatment.roles["meta"]!, width: 140, color: Palette.muted)
            }
            .frame(width: 374)
            .offset(x: 28, y: 28)
            Rectangle().fill(Palette.rule).frame(width: 374, height: 0.5).offset(x: 28, y: 76)
            ArticleLayout(blocks: blocks, measurements: measurements) {
                ForEach(Array(blocks.enumerated()), id: \.offset) { _, block in
                    RoleText(text: block.text, role: treatment.roles[block.role]!, color: block.muted ? Palette.muted : Palette.ink)
                }
            }
            .offset(x: 28, y: 112)
            Rectangle().fill(Palette.rule).frame(width: 374, height: 0.5).offset(x: 28, y: 764)
            RoleText(text: "Continue reading", role: treatment.roles["item"]!, color: Palette.accent).offset(x: 28, y: 783)
            RoleText(text: "Saved to your library", role: treatment.roles["meta"]!, color: Palette.muted).offset(x: 28, y: 813)
        }
        .frame(width: 430, height: 850, alignment: .topLeading)
        .clipped()
        .environment(\.colorScheme, .light)
    }
}

@main
struct RenderNative {
    @MainActor static func main() throws {
        _ = NSApplication.shared
        let root = URL(fileURLWithPath: CommandLine.arguments.dropFirst().first ?? FileManager.default.currentDirectoryPath, isDirectory: true)
        let output = root.appendingPathComponent("renders", isDirectory: true)
        try FileManager.default.createDirectory(at: output, withIntermediateDirectories: true)
        let decoder = JSONDecoder()
        let before = try decoder.decode([String: Treatment].self, from: Data(contentsOf: root.appendingPathComponent("briefs/before.json")))
        var entries: [(String, String, Treatment)] = [("new", "before", before["native"]!), ("refine", "before", before["native"]!)]
        for arm in ["baseline", "impeccable", "original"] {
            let path = root.appendingPathComponent("treatments/\(arm).json")
            guard FileManager.default.fileExists(atPath: path.path) else {
                print("SKIP missing treatment \(arm)")
                continue
            }
            let values = try decoder.decode([String: Treatment].self, from: Data(contentsOf: path))
            for task in ["new", "refine"] {
                guard let value = values["native-\(task)"] else { fatalError("Missing native-\(task) in \(arm)") }
                entries.append((task, arm, value))
            }
        }
        var reports: [[String: Any]] = []
        for (task, arm, treatment) in entries {
            let measurement = Measurements()
            let canvas = NativeCanvas(treatment: treatment, measurements: measurement)
            let renderer = ImageRenderer(content: canvas)
            renderer.scale = 2
            renderer.proposedSize = ProposedViewSize(width: 430, height: 850)
            guard let cg = renderer.cgImage else { fatalError("ImageRenderer failed for \(arm) \(task)") }
            let bitmap = NSBitmapImageRep(cgImage: cg)
            guard let png = bitmap.representation(using: .png, properties: [:]) else { fatalError("PNG encoding failed") }
            let filename = "native-\(task)-\(arm).png"
            try png.write(to: output.appendingPathComponent(filename))
            // Layout bounds already include the canvas offset on this path.
            // Keep these measured coordinates: applying the offset twice would
            // falsely report footer collisions despite correctly drawn pixels.
            let frames = measurement.frames
            let issues = measurement.issues
            let articleBottom = (frames.last?["bottom"] as? Double) ?? 0
            var roleMetrics: [String: Any] = [:]
            for (name, role) in treatment.roles {
                let font = role.nativeFont
                let nativeAdvance = NSLayoutManager().defaultLineHeight(for: font)
                roleMetrics[name] = ["resolvedFont": font.fontName, "pointSize": font.pointSize, "ascender": font.ascender, "descender": font.descender, "nativeLeading": font.leading, "nativeLineHeight": nativeAdvance, "requestedBaselineAdvance": role.size * role.leading, "differenceFromNativeLineHeight": role.size * role.leading - nativeAdvance, "trackingPoints": role.size * role.tracking]
            }
            let wrappedCopy = canvas.blocks.map { block -> [String: Any] in
                let lines = wrappedLines(block.text, role: treatment.roles[block.role]!, width: 374)
                return ["id": block.id, "text": block.text, "lines": lines, "lineCount": lines.count, "baselineAdvance": treatment.roles[block.role]!.size * treatment.roles[block.role]!.leading]
            }
            reports.append(["file": filename, "case": task, "arm": arm, "canvasPoints": [430, 850], "pixels": [cg.width, cg.height], "scale": 2, "provenance": "Native SwiftUI macOS canvas; TextKit wraps strings, SwiftUI Text and ImageRenderer draw pixels. Not an iOS simulator.", "articleFrames": frames, "articleBottom": articleBottom, "issues": issues, "roleMetrics": roleMetrics, "wrappedCopy": wrappedCopy, "copyPreservation": "Whitespace-normalized input equals concatenated wrapped lines; asserted for every rendered text block."])
            print("\(filename) \(cg.width)×\(cg.height) articleBottom=\(articleBottom) issues=\(issues)")
        }
        let data = try JSONSerialization.data(withJSONObject: reports, options: [.prettyPrinted, .sortedKeys])
        try data.write(to: output.appendingPathComponent("native-render-report.json"))
    }
}
