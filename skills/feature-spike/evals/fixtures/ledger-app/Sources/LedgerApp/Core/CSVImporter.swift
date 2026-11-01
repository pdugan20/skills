import Foundation

enum CSVImportError: Error, Equatable {
    case malformedRow(Int)
}

/// Parses bank exports with the header `date,amount_cents,category,memo`.
struct CSVImporter: Sendable {
    func parse(_ text: String) throws -> [Transaction] {
        let formatter = ISO8601DateFormatter()
        formatter.formatOptions = [.withFullDate]
        var transactions: [Transaction] = []
        for (index, line) in text.split(separator: "\n").enumerated() where index > 0 {
            let fields = line.split(separator: ",", omittingEmptySubsequences: false).map(String.init)
            guard fields.count == 4, let date = formatter.date(from: fields[0]), let cents = Int(fields[1]) else {
                throw CSVImportError.malformedRow(index + 1)
            }
            transactions.append(
                Transaction(id: UUID(), date: date, amountCents: cents, category: fields[2], memo: fields[3])
            )
        }
        return transactions
    }
}
