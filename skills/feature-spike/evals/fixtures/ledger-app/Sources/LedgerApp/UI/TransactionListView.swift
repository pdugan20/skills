import SwiftUI

struct TransactionListView: View {
    let transactions: [Transaction]
    @State private var search = ""

    private var filtered: [Transaction] {
        search.isEmpty ? transactions : transactions.filter { $0.memo.localizedCaseInsensitiveContains(search) }
    }

    var body: some View {
        NavigationStack {
            List(filtered) { transaction in
                HStack {
                    VStack(alignment: .leading, spacing: 4) {
                        Text(transaction.memo).font(.headline)
                        Text(transaction.category).font(.caption).foregroundStyle(.secondary)
                    }
                    Spacer()
                    Text(transaction.date, style: .date).font(.caption)
                    Text(Double(transaction.amountCents) / 100, format: .currency(code: "USD"))
                        .monospacedDigit()
                }
            }
            .searchable(text: $search)
            .navigationTitle("Activity")
        }
    }
}
